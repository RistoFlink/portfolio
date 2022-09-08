from flask import Flask, render_template, abort



def create_app():
    app = Flask(__name__)
    projects = [
        {
            "name": "Habit tracking app with Python and MongoDB",
            "thumb": "img/habit-tracking.png",
            "hero": "img/habit-tracker-code.png",
            "categories": ["python", "web", "mongodb"],
            "slug": "habit-tracking",
            "prod": "https://rflink-habit-tracker.herokuapp.com"
        },
        {
            "name": "Microblog with Python and MongoDB",
            "thumb": "img/habit-tracking.png",
            "hero": "img/microblog.png",
            "categories": ["python", "web", "mongodb"],
            "slug": "microblog",
            "prod": "https://rflink-microblog-app.herokuapp.com"
        },
        {
            "name": "Expanding an online store into the Estonian market",
            "thumb": "img/habit-tracking.png",
            "hero": "img/habit-tracking-hero.png",
            "categories": ["writing"],
            "slug": "thesis",
            "prod": "https://urn.fi/URN:NBN:fi:amk-2020100721092"
        }
    ]

    slug_to_project = {project["slug"]: project for project in projects}

    @app.route("/")
    def home():
        return render_template("home.html", projects = projects)

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        return render_template(f"project_{slug}.html", project = slug_to_project[slug])

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404
        
    return app