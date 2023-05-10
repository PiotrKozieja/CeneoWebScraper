from app import app
@app.route("/")
@app.route("/index")
def index():
    return"Hello world!"
@app.route("/name", defult= {/name/<name>})
def name(name):
    return f"Hello {name}"