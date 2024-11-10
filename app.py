from flask import Flask, render_template, request

# Flask App Here
app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port="80", host="0.0.0.0")