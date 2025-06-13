from flask import Flask, render_template_string
import frontmatter
import markdown
from jinja2 import Template

app = Flask(__name__)

@app.route("/")
def show_page():
    # Markdown + metadata'yı yükle
    post = frontmatter.load("about.md")

    # Metadata ile içerikteki {{ }} alanlarını doldur
    template = Template(post.content)
    rendered_content = template.render(**post.metadata)

    # Markdown'dan HTML'ye dönüştür
    html_content = markdown.markdown(rendered_content)

    # Tümünü bir template'e göm
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{ title }}</title>
        <meta charset="utf-8">
    </head>
    <body>
        {{ jinja_content|safe }}
    </body>
    </html>
    """, title=post.metadata.get('title', 'Sayfa'), jinja_content=html_content, )

if __name__ == "__main__":
    app.run(debug=True)
