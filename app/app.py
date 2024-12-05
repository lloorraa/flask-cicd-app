from flask import Flask, render_template, request
from models import db, Item
import os

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form.get('name')
    if name:
        new_item = Item(name=name)
        db.session.add(new_item)
        db.session.commit()
    return index()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
