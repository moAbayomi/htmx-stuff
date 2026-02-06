from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/swappy")
def swappy():
    return """
        <p id="p1" hx-swap-oob="innerHTML:#p1" >replaced p1 bitch</p>
        <p id="p2" hx-swap-oob="innerHTML:#p2" >replaced p2 bitch</p>
        <p>i am pressed.i am excited</p>
    
    """

@app.route("/trigger")
def trigger():
    res = Response("")
    res.headers["HX-Trigger"] = "heheh"

    return res

@app.route("/upload")
def upload():
    return """
        wow this is the reckoning ski. you cannot escape. you will definitely not escape. we will find you. and you will end up in trouble bro. you will end up in deep trouble and you will be put to shame and we will strip you naked and al the bad things. you will cry. your eye go peel .you will try to find refuge but you wont find any. but inside of your heart of hearts you will know/realize that you deserve this. this is the punishment of your sins!
    """

if __name__ == "__main__":
    app.run(debug=True)

