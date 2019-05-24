from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, default='')
    email = db.Column(db.String(120), unique=True, nullable=False, default='')
    first_name = db.Column(db.String(120), unique=False, nullable=False, default='')
    last_name = db.Column(db.String(120), unique=False, nullable=False, default='')
    phone = db.Column(db.String(120), unique=True, nullable=False, default='')
    # cart = db.relationship('Cart', backref='person', lazy=True)

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone

        }

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_date=db.Column(db.String(80), unique=True, nullable=False, default='')
    # person_id = db.Column(db.Integer, db.ForeignKey('person.id'),nullable=False)
    # cart_item = db.relationship('CartItem', backref='cart', lazy=True)

    def __repr__(self):
        return '<Cart %r>' % self.create_date

    def serialize(self):
        return {
            "create_date": self.create_date,
            # "person_id": self.person_id

        }

# class CartItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # cart_id=db.Column(db.Integer,db.ForeignKey('cart.id'), unique=True, nullable=False, default='')
#     product_id = db.Column(db.Integer,nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     price = db.Column(db.Integer ,nullable=False)
   
    

#     def __repr__(self):
#         return '<CartItem %r>' % self.cart_id

#     def serialize(self):
#         return {
#             # "cart_id": self.cart_id,
#             "product_id": self.product_id,
#             "quantity": self.quantity,
#             "price": self.price

#         }