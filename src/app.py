from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_paginate import Pagination
from models import Users, Inventory, Base
from sqlalchemy import create_engine

app = Flask(__name__)


engine = create_engine("sqlite:///olxmini.db")
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
var = DBsession()


@app.route("/", methods=["GET"])
def index():
    inventory = var.query(Inventory).order_by('-inventories_id').all()[:3]
    inventory_count = var.query(Inventory).count()  # [:6]
    # search = False
    # q = request.args.get('q')
    # if q:
    #     search = True

    # page = request.args.get('page', type=int, default=9)

    # # Users = User.find(...)
    # pagination = Pagination(page=page,
    #                         total=inventory_count,
    #                         search=search, record_name='inventories')


    # , pagination=pagination,
    return render_template(
        'index.html', inventory=inventory)


@app.route('/details')
@app.route('/details/<int:inventories_id>')
def view_particulars(inventories_id):
    inventory = var.query(Inventory).filter_by(
        inventories_id=inventories_id).one()
    user = var.query(Users).filter_by(seller_id=inventories_id)
    return render_template('details.html', inventory=inventory, user=user)


@app.route('/add', methods=["GET", "POST"])
def add_item():
    if request.method == "GET":
        # the list of comments that we've defined as a variable further up will
        # be available inside our template
        return render_template("add.html")
    elif request.method == "POST":
        title = request.form["titleView"]
        desc = request.form["descView"]
        name = request.form["nameView"]
        number = request.form["numberView"]
        neigh = request.form["neighbourView"]
        email = request.form["emailView"]

# setting up an instance of the tables that we are going to run, data we
# will need to store.
        users = Users(name=name, mobile_number=number,
                      neighbourhood=neigh, email_address=email)
        inventory = Inventory(p_title=title, p_desc=desc,
                              p_price=25, var=users)

        var.add(users)
        var.add(inventory)
        var.commit()
    return redirect(url_for('index'))


# web: gunicorn -w 4 -b "0.0.0.0: $PORT" app:app

# This extracts the stuff that was typed into the textarea in the page
# from the browser's request
app.run(debug=True, host='0.0.0.0', port=8080)
