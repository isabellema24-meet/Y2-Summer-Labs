from flask import Flask, render_template , request, url_for, redirect 
from flask import session 
import pyrebase

Config = {
  "apiKey": "AIzaSyCBgBzqZw0OWPnza-irB00SuO8dc5BQXXY",
  "authDomain": "authentication-lab-d7b42.firebaseapp.com",
  "projectId": "authentication-lab-d7b42",
  "storageBucket": "authentication-lab-d7b42.appspot.com",
  "messagingSenderId": "464754632527",
  "appId": "1:464754632527:web:390aaf207c9dd22ddc473a",
  "measurementId": "G-Y7R8RP0WF1",
  "databaseURL":""
}

app = Flask(__name__, template_folder='templates', static_folder='static')

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
app.config['SECRET_KEY']= 'super-secret-key'

@app.route('/signin' , methods = ['GET' , 'POST'])
def signin():
	if request.method == "POST":
		email = session['email']
		password= session['password']
		email = request.form['email']
		password = request.form['password']
		session['quotes'] = []
		return redirect(url_for('home'))
		session['user'] = auth.sign_in_with_email_and_password(email , password)
	else:
		return render_template("signin.html")

@app.route('/home'  , methods = ['GET' , 'POST'])
def home():
	return render_template("home.html")

@app.route('/thanks'  , methods = ['GET' , 'POST'])
def thanks():
	return render_template("thanks.html")

@app.route('/display'  , methods = ['GET' , 'POST'])
def display():
	return render_template("display.html")

@app.route('/'  , methods = ['GET' , 'POST'])
def singup():
	if request.method == "POST":
		try:
			email= session['email']
			password = session['password']
			email = request.form['email']
			password = request.form['password']
			session['quotes'] = []
			session['user'] = auth.create_user_with_email_and_password(email , password)
			return redirect(url_for('home'))
		except:
			print("error")
			return render_template('signup.html')
	return render_template("signup.html")
@app.route('/signout' , methods = ['GET' , 'POST'])
def signout():
	return redirect(url_for("signin"))


if __name__ == '__main__':
    app.run(debug=True)
