from flask import Flask, render_template

app = Flask(__name__,
            static_url_path="",
            static_folder="static",
            template_folder="templates"
        )

@app.route("/")
def home():
    return "<h1>Gitcollab</h1><p>Página inicial (home)</p>"

if __name__ == "__main__":
    # Importante desactivar esto en producción
    app.run(debug=True)
