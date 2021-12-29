from flask import Flask, render_template
from modules import RediProject


app = Flask(__name__)

list = ("Score","Subreddit", "Title")

RedditData = RediProject.getRedData()



@app.route("/")
def index():
    
    return render_template("table.html", 
    heading = list,
    data = RedditData.values)