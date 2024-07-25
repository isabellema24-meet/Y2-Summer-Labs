from flask import Flask, render_template , request, url_for, redirect 
from flask import session 
import pyrebase
app = Flask(__name__, template_folder='templates', static_folder='static')
firebaseConfig = {
  'apiKey': "AIzaSyDgt3F2V2NdtHoh13dZSc-YTxI5EELDzNg",
  'authDomain': "cosmicexplorer-b4d28.firebaseapp.com",
  'projectId': "cosmicexplorer-b4d28",
  'storageBucket': "cosmicexplorer-b4d28.appspot.com",
  'messagingSenderId': "9149658492",
  'appId': "1:9149658492:web:02bd41fbd0d43f395e60f9",
  'measurementId': "G-DD46TR2XFN",
  "databaseURL" : "https://cosmicexplorer-b4d28-default-rtdb.europe-west1.firebasedatabase.app/"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
app.config['SECRET_KEY']= 'super-secret-key'
db = firebase.database()

@app.route('/' , methods = ["GET" , 'POST'])
def home():
	return render_template("welcome.html")

@app.route('/su' , methods = ["GET" , 'POST'])
def signup():
	if request.method == "POST":
		try:
			name= request.form['name']
			email = request.form['email']
			password = request.form['password']
			session['user'] = auth.create_user_with_email_and_password(email , password)
			info = { "name" : name , "email" : email, "password" : password}
			UID = session["user"]["localId"]
			print(UID)
			db.child("users").child(UID).set(info)
			return redirect(url_for('main'))
		except Exception as e:
			print(e)
			return render_template('signup.html')
	return render_template("signup.html")

@app.route('/login' , methods = ["GET" , 'POST'])
def login():
	if request.method == "POST":
		try:
			email = session['email']
			password= session['password']
			email = request.form['email']
			password = request.form['password']
			session['user'] = auth.sign_in_with_email_and_password(email , password)
			return redirect(url_for('main'))
		except Exception as e:
			print(f"An error occurred: {e}")
	return render_template("login.html")

@app.route('/main' , methods = ["GET" , 'POST'])
def main():
	if request.method == 'POST':
		return redirect(url_for('signout'))
	return render_template("main.html")

@app.route('/galaxies' , methods = ["GET" , 'POST'])
def galaxy():
	return render_template("galaxies.html")

@app.route('/nebulas' , methods = ["GET" , 'POST'])
def nebula():
	return render_template("nebulas.html")

@app.route('/dwarf-planets' , methods = ["GET" , 'POST'])
def dp():
	return render_template("dwarfPlantes.html")

@app.route('/solar-system' , methods = ["GET" , 'POST'])
def solar():
	return render_template("solar-system.html")

@app.route('/black-holes' , methods = ["GET" , 'POST'])
def bh():
	return render_template("black-holes.html")

@app.route('/so' , methods = ['GET' , 'POST'])
def signout():
	if request.method == 'POST':
		feedback = request.form['feedback']
		fb = {"feedback" : feedback}
		UID = session["user"]["localId"]
		db.child("feedback").child(UID).update(fb)
		info = db.child('feedback').get().val()
		return render_template('welcome.html',info = info)
	return render_template("signout.html")



if __name__ == '__main__':
    app.run(debug=True)
