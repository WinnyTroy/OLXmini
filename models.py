from app import db


class Users(db.Model):
    __tablename__ = 'users'

    seller_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    mobile_number= db.Column(db.String())
    neighbourhood = db.Column(db.String())
    email_address = db.Column(db.String())



    def __init__(self, seller_id, name, mobile_number, neighbourhood, email_address):
        self.seller_id = seller_id
        self.name = name
        self.mobile_number = mobile_number
        self.neighbourhood = neighbourhood
        self.email_address = email_address

    def __repr__(self):
            return '<User %r>' % self.username




class Inventory(db.Model):
    __tablename__ = 'inventories'

    inventories_id = db.Column(db.Integer, primary_key=True)
    p_title = db.Column(db.String())
    p_desc = db.Column(db.String())
    p_price = db.Column(db.String())


    # initialises the model, creating instances for each field
    def __init__(self, inventories_id, p_title, p_desc, p_price):
        self.inventories_id = inventories_id
        self.p_title = p_title
        self.p_desc = p_desc
        self.p_price = p_price


       # represent the object when we query for it.
    def __repr__(self):
        return '<id {}>'.format(self.id)
