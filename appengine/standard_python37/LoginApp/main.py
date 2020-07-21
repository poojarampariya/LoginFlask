from flask import Flask,request,render_template
import pickle5 as pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")
database={'joey':'123','rachel':'456','monica':'789'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('home.html',name=name1)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
