from flask import Flask, render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///OLXmini.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

comments = []


@app.route("/",methods=["GET"])
def index():
    return render_template('index.html',comments=comments)


@app.route('/details')
def view_particulars():
    return render_template('details.html')


@app.route('/add', methods=["GET", "POST"])
def add_item():
    if request.method == "GET":
        # the list of comments that we've defined as a variable further up will be available inside our template
        return render_template("add.html", comments=comments)
    elif request.method == "POST":
        comments.append(request.form["titleView"])
        comments.append(request.form["descView"])
        comments.append(request.form["nameView"])
        comments.append(request.form["numberView"])
        comments.append(request.form["neighbourView"])
        comments.append(request.form["emailView"])

        print comments
        return redirect(url_for('index'))

# This extracts the stuff that was typed into the textarea in the page from the browser's request
app.run(debug=True, host='0.0.0.0', port=8000)
