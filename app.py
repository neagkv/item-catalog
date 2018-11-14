from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *

app = Flask(__name__)

engine = create_engine('sqlite:///items.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



# Show all categories
@app.route('/')
@app.route('/category/')
def showCategories():
    category = session.query(Category).first()
    items = session.query(Category)
    output = ''
    for i in items:
        output += i.name
        output += '</br>'
    return output


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
