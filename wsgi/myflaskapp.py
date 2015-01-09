from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "OPENSHIFT PASS With FLASK WEB APPLICATION"

if __name__ == "__main__":
    app.run()

