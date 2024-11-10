from flask import Flask, render_template

app = Flask(__name__)

nav = [
    { "title": "Главная", "URL": "/" },
    { "title": "Zeus описание", "URL": "/zeus" },
    { "title": "Witch Doctor описание", "URL": "/witch_doctor" },
    { "title": "Skywrath Mage описание", "URL": "/skywrath_mage" },
    { "title": "Глоссарий Dota 2 (Герои и Их Способности)", "URL": "/glossary" },
    { "title": "Сведения об авторе", "URL": "/about_me" }
    
]

@app.context_processor
def global_context():
    return {
        "nav": nav
    }

@app.route("/")
def main():
    return render_template("main.html", name="Главная")

@app.route("/zeus")
def zeus():
    return render_template("zeus.html", name="Zeus описание")


@app.route("/witch_doctor")
def wd():
    return render_template("witch_doctor.html", name="Witch Doctor описание")

@app.route("/skywrath_mage")
def sm():
    return render_template("skywrath_mage.html", name="Skywrath Mage описание")

@app.route("/glossary")
def glossary():
    return render_template("glossary.html", name="Глоссарий Dota 2 (Герои и Их Способности)")

@app.route("/about_me")
def about_me():
    return render_template("about_me.html", name="Сведения об авторе")

if __name__ == '__main__':
    app.run(debug=True)