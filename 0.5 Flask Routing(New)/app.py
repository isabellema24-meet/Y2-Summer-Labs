from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return (
        "<html><h1>Welcome to the Gallery!</h1><p>In this gallery you will find pictures of <a href= '/food/' >FOOD</a> , <a href= '/pet/'>PETS</a> and <a href= '/outer_space/'>OUTER SPACE</a> </p></html>"
        )
@app.route('/food/')
def food():
    return(
    "<html><h1>Food category</h1><h2>Food1</h2><h2>Food2</h2><h2>Food3</h2></html>"


        )
@app.route('/pet/')
def pet():

@app.route('/outer_space/')
def outer_space():

if __name__ == '__main__':
    app.run(debug=True)
