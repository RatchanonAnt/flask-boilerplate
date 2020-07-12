from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def root():
    return "Yor see my Pikachu?"

@app.route('/new_one')
def new_one_funtion():
    username = request.args.get('name')
    print(username)
    return "Hi" + username

@app.route('/sum')
def my_sum():
   a =request.args.get('a')
   a =int(a)
   b =request.args.get('b')
   b =int(b)
   return str (a+b)

@app.route('/mypage')
def mypage():
    username = request.args.get('name')
    return render_template('home.html',name = username)

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5000)