#server.py
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("/index.html")

if __name__ == '__main__':
    app.run() # 開發階段也可以使用app.run(debug=True)