from flask import Flask, render_template, request
import requests

blog_endpoint = "https://api.npoint.io/05bd5c3eb3e254d1a9d9"
response = requests.get(blog_endpoint)
DATA = response.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", data=DATA)


@app.route("/<int:id>")
def show_detail(id):
    display_detail = None
    for item in DATA:
        if item['id'] == id:
            display_detail = item
    return render_template("post.html", item=display_detail)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return receive_data()
    else:
        return render_template("contact.html")


# @app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print('\n', data['name'], '\n', data['email'], '\n', data['phone'], '\n', data['message'])
    return "<h1>Successfully sent your message.</h1>"


if __name__ == "__main__":
    app.run(debug=True)
