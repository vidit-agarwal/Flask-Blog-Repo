from flask import Flask , render_template , url_for
app = Flask(__name__)

posts = [
    {
        'author' : 'Vidit Agarwal' ,
        'title' : 'Blog Post' ,
        'content' : 'This is the first blog of the site' ,
        'date_posted' : 'April 21, 2018'
    } ,
    {
        'author' : 'Swetabh Pathak' ,
        'title' : 'Elucidata Information' ,
        'content' : 'I am the Co-Founder and the Directior of the Elucidata Inc' ,
        'date_posted' : 'Jan 11, 2015'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html' , posts=posts)

@app.route("/about")
def about():
    return render_template('about.html' , title='About') 


#if __name__ == '__main__' :
 #   app.run(debug=True)