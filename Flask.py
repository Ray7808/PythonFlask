#server.py
from flask import Flask
from flask import render_template, request
import config # 配置文件


app = Flask(__name__)
app.config.from_object(config)


@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(f"Now the request number is {request.values}")
        print(f"Hello, your first name is {request.values['inputFirstName']}")
        print(f"Hello, your last name is {request.values['inputLastName']}") 
        print(f"Hello, your email is {request.values['inputEmail']}") 
        print(f"Hello, your password is {request.values['inputPassword']}")  

    return render_template("/index.html")



if __name__ == '__main__':
    app.run() # 開發階段也可以使用app.run(debug=True)