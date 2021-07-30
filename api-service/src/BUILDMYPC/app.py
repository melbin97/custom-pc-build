from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "welcome to Custom PC Build!!"

app.run(debug=True)
