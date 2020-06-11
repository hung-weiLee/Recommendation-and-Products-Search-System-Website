# coding: utf-8
from amazon_website import db


class Product(db.Model):
    __tablename__ = 'product'
    Id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    group = db.Column(db.String(255), nullable=False)
    salesrank = db.Column(db.INTEGER, nullable=False)
    ASIN = db.Column(db.String(255), nullable=False)
    categories = db.relationship("Category", backref="product")
    items = db.relationship("Item", backref="product")
    reviews = db.relationship("Review", backref="product")
    similar = db.relationship("Similar", backref="product")

    def __init__(self, Id, title, group, salesrank, ASIN):
        self.Id = Id
        self.title = title
        self.group = group
        self.salesrank = salesrank
        self.ASIN = ASIN

    def __str__(self):
        return str(self.title) + '_' + str(self.group) + '_' + str(self.salesrank) + '_' + str(self.ASIN)

    def __repr__(self):
        return '<Product %r>' % self.title


class Category(db.Model):
    __tablename__ = 'categories'

    Id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    product_Id = db.Column(db.Integer, db.ForeignKey("product.Id"))

    def __str__(self):
        return str(self.name)


class Item(db.Model):
    __tablename__ = 'items'

    Id = db.Column(db.INTEGER, primary_key=True)
    product_Id = db.Column(db.Integer, db.ForeignKey("product.Id"))
    create_time = db.Column(db.DateTime)
    cutomer_Id = db.Column(db.String(255))
    rating = db.Column(db.INTEGER)
    votes = db.Column(db.INTEGER)
    helpful = db.Column(db.INTEGER)


class Review(db.Model):
    __tablename__ = 'reviews'

    Id = db.Column(db.INTEGER, primary_key=True)
    product_Id = db.Column(db.Integer, db.ForeignKey("product.Id"))
    total = db.Column(db.INTEGER)
    downloaded = db.Column(db.INTEGER)
    avg_rating = db.Column(db.INTEGER)

    def __str__(self):
        return str(self.Id) + '_' + str(self.product_Id) + '_' + str(self.total) + '_' + str(
            self.downloaded) + '_' + str(self.avg_rating)


class Similar(db.Model):
    __tablename__ = 'similar'

    Id = db.Column(db.INTEGER, primary_key=True)
    product_Id = db.Column(db.Integer, db.ForeignKey("product.Id"))
    ASIN = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return str(self.product_Id)+" "+str(self.Id)+" "+str(self.ASIN)

class Samples(db.Model):
    __tablename__ = 'samples'

    product_Id = db.Column(db.INTEGER, primary_key=True)
    vector = db.Column(db.String(255), nullable=False)
    score = db.Column(db.INTEGER)

    def __str__(self):
        return str(self.product_Id)+" "+str(self.vector)+" "+str(self.score)
