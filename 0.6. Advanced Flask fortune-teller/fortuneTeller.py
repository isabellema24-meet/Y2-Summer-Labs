from flask import Flask, render_template
import random

app = Flask(__name__,
template_folder='templates')
fortune_types = ["Iasa will host a rage room where you can smash all the food" , "you will meditate with Lilach" , 
"you will accidentally stay out after curfew and run into Abdallah at 23:01" , "you will go swim in the ocean and encounter Jojo siwa" , "you'll be cursed with only being able to eat the shakshuka in IASA"]

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/future")
def future():
	fortune = random.choice(fortune_types)
	return render_template("future.html", fortune = fortune)

	
@app.route("/personalFuture")
def personalFuture():
	return render_template("personal.html", fortune)

	



if __name__ == '__main__':
	app.run(debug=True)