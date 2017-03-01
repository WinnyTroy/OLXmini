from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    seller_id = Column(Integer, autoincrement=True,
                       primary_key=True, unique=True,)
    name = Column(String())
    mobile_number = Column(String())
    neighbourhood = Column(String())
    email_address = Column(String())

    def __init__(self, name, mobile_number, neighbourhood, email_address):
        self.name = name
        self.mobile_number = mobile_number
        self.neighbourhood = neighbourhood
        self.email_address = email_address

    def __repr__(self):
        return '<User %r>' % self.seller_id

    def __str__(self):
        return '<User %r>' % self.seller_id


class Inventory(Base):
    __tablename__ = 'inventories'

    inventories_id = Column(Integer, autoincrement=True,
                            primary_key=True, unique=True)
    p_title = Column(String())
    p_desc = Column(String())
    p_price = Column(String())

    user_id = Column(Integer, ForeignKey("users.seller_id"))
    var = relationship(Users)

    # initialises the model, creating instances for each field
    def __init__(self, p_title, p_desc, p_price, var):
        self.p_title = p_title
        self.p_desc = p_desc
        self.p_price = p_price
        self.var = var

       # represent the object when we query for it.
    def __repr__(self):
        return '<id {}, Title %s, Description %s, Price %s >'.format(self.inventories_id, self.p_title, self.p_desc,
                                                                     self.p_price)


engine = create_engine("sqlite:///olxmini.db")
Base.metadata.create_all(engine)
