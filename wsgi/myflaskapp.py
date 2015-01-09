from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "OPENSHIFT PASS 환경에서 파이썬 웹서비스를 어떻게..."

if __name__ == "__main__":
    app.run()

