from flask import Flask, render_template , request, url_for, redirect , session
import random

app = Flask(__name__,
template_folder='templates')
fortune_types = ["Iasa will host a rage room where you can smash all the food" , "you will meditate with Lilach" , 
"you will accidentally stay out after curfew and run into Abdallah at 23:01" , "you will go swim in the ocean and encounter Jojo siwa" , "you'll be cursed with only being able to eat the shakshuka in IASA"]

@app.route("/home" , methods = ['GET' , 'POST'])
def home():
    if request.method == 'GET' :
        return render_template("homeDup.html" )
    else:
        month= request.form['birth month']
        return redirect(url_for('future' , bday = month))

@app.route('/future/<string:bday>')
def future(bday):
    birth = len(bday)
    fortuna = ''
    if birth > 4:
        return render_template("futureDup.html" , fortuna= random.choice(fortune_types))
    else:
        fortuna = fortune_types[birth-1]
        return render_template("futureDup.html" , fortuna = fortune_types[birth-1])

@app.route('/' , methods= "GET" , "POST")
def login()
    if request.method == "POST":
        session['name'] = request.form['name']
        session['birth month'] = request.form['birth month']
        return redirect(url_for('home'))
    
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)