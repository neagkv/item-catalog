from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show all categories
@app.route('/')
@app.route('/category/')
def showCategories():
    categories = session.query(Category).all()
    # return "This page will show all categories"
    return render_template('categories.html', categories=categories)


    # Show a restaurant menu
@app.route('/category/<int:category_id>/')
@app.route('/restaurant/<int:category_id>/item/')
def showItems(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(
        category_id=category_id).all()
    return render_template('items.html', items=items, category=category)
    # return 'This page is the items for categories %s' % category_id







if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
