import os
from pathlib import Path

from flask import Flask, abort, render_template_string, request

try:
    import markdown as mdlib
except ImportError:
    mdlib = None

APP_TITLE = "MD Docs Browser"
BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)

TEMPLATE = """<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>{{ title }}{% if current_name %} - {{ current_name }}{% endif %}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    :root { color-scheme: light dark; }
    body { margin:0; font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; }
    .layout { display:flex; min-height:100vh; }
    .sidebar {
      width: 320px; max-width: 85vw;
      border-right: 1px solid rgba(127,127,127,.35);
      padding: 16px;
      box-sizing: border-box;
      position: sticky; top: 0; height: 100vh; overflow:auto;
    }
    .content { flex:1; padding: 18px 22px; box-sizing: border-box; }
    .title { font-weight: 700; font-size: 16px; margin-bottom: 12px; }
    .search { width: 100%; padding: 10px 12px; margin-bottom: 12px; border-radius: 10px;
      border: 1px solid rgba(127,127,127,.35); background: transparent; }
    a.item {
      display:block; padding: 8px 10px; border-radius: 10px; text-decoration:none;
      border: 1px solid transparent; margin: 4px 0;
    }
    a.item:hover { border-color: rgba(127,127,127,.35); }
    a.item.active { border-color: rgba(127,127,127,.55); font-weight: 600; }
    .hint { font-size: 12px; opacity: .75; margin-top: 10px; line-height: 1.3; }
    .card {
      border: 1px solid rgba(127,127,127,.35);
      border-radius: 14px; padding: 14px 16px; max-width: 1100px;
    }
    pre, code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
    pre { padding: 12px; border-radius: 12px; overflow:auto; border: 1px solid rgba(127,127,127,.25); }
    h1,h2,h3 { margin-top: 1.2em; }
    table { border-collapse: collapse; }
    th, td { border: 1px solid rgba(127,127,127,.35); padding: 6px 10px; }
  </style>
</head>
<body>
  <div class="layout">
    <div class="sidebar">
      <div class="title">{{ title }}</div>

      <form method="get" action="/" style="margin:0;">
        <input class="search" type="text" name="q" value="{{ q }}" placeholder="Filter docs..." />
      </form>

      {% for f in files %}
        <a class="item {% if f == current_name %}active{% endif %}" href="/?doc={{ f }}{% if q %}&q={{ q|urlencode }}{% endif %}">
          {{ f }}
        </a>
      {% endfor %}

      <div class="hint">
        Folder: <code>{{ base_dir }}</code><br/>
        {% if not markdown_enabled %}
          Markdown renderer not installed: showing raw text.
        {% endif %}
      </div>
    </div>

    <div class="content">
      <div class="card">
        {% if current_name %}
          <div style="display:flex; gap:10px; align-items:baseline; flex-wrap:wrap;">
            <h2 style="margin:0;">{{ current_name }}</h2>
          </div>
          <hr style="border:none; border-top:1px solid rgba(127,127,127,.35); margin:12px 0;" />
          <div class="md">
            {{ content|safe }}
          </div>
        {% else %}
          <h2 style="margin-top:0;">Select a document</h2>
          <p>Pick a <code>.md</code> file from the left menu.</p>
        {% endif %}
      </div>
    </div>
  </div>
</body>
</html>
"""

def list_md_files(query: str | None) -> list[str]:
    files = sorted([p.name for p in BASE_DIR.glob("*.md")])
    if query:
        q = query.lower()
        files = [f for f in files if q in f.lower()]
    return files

def safe_read_md(name: str) -> str:
    # prevent path traversal: only allow files in BASE_DIR with .md extension
    if not name or "/" in name or "\\" in name or name.startswith(".") or not name.lower().endswith(".md"):
        raise FileNotFoundError("Invalid doc name.")
    path = (BASE_DIR / name).resolve()
    if path.parent != BASE_DIR:
        raise FileNotFoundError("Doc not in base directory.")
    if not path.exists() or not path.is_file():
        raise FileNotFoundError("Doc not found.")
    return path.read_text(encoding="utf-8", errors="replace")

def render_markdown(text: str) -> str:
    if mdlib is None:
        # fallback: raw
        esc = (
            text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
        )
        return f"<pre>{esc}</pre>"
    return mdlib.markdown(
        text,
        extensions=["fenced_code", "tables"],
        output_format="html5",
    )

@app.route("/", methods=["GET"])
def index():
    doc = request.args.get("doc", "").strip()
    q = request.args.get("q", "").strip()
    files = list_md_files(q)

    current_name = doc if doc in files else (files[0] if files else "")
    content_html = ""
    if current_name:
        try:
            content_md = safe_read_md(current_name)
            content_html = render_markdown(content_md)
        except FileNotFoundError:
            abort(404)

    return render_template_string(
        TEMPLATE,
        title=APP_TITLE,
        files=files,
        current_name=current_name if current_name else "",
        content=content_html,
        q=q,
        base_dir=str(BASE_DIR),
        markdown_enabled=(mdlib is not None),
    )

if __name__ == "__main__":
    # Use 0.0.0.0 to allow LAN access; change to 127.0.0.1 if you want local only.
    app.run(host="127.0.0.1", port=5173, debug=True)
