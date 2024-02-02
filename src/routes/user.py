from flask import Blueprint, render_template, request, url_for, redirect
from models.user_model import UserModel
from models.entities.user_entitie import User
from uuid import uuid4
import datetime

main = Blueprint('users_blueprint', __name__)

@main.route('/', methods=["GET"])
def index():
    users = UserModel.getUsers()
    return render_template("index.html", users=users)
    

@main.route('/add', methods=["POST"])
def addUser():
    if request.method == "POST":
        id = uuid4()
        name = request.form["name"]
        email = request.form["email"]
        date = datetime.datetime.now()
        user = User(id, name, email, date)

        UserModel.addUser(user)
        return redirect(url_for('users_blueprint.index'))

@main.route('/delete/<id>')
def deleteUser(id):
    UserModel.deleteUser(id)
    return redirect(url_for('users_blueprint.index'))

@main.route('/edit/<id>', methods=["GET", "POST"])
def getUser(id):
    user = UserModel.getUser(id)
    return render_template('editar.html', user=user)

@main.route('/edit/update/<id>', methods=["GET", "POST", "UPDATE"])
def updateUser(id):
    id = id
    name = request.form["name"]
    email = request.form["email"]
    date = UserModel.getUserDate(id)
    user = User(id, name, email, date)
    resp = UserModel.updateUser(user)
    if resp == 1:
        return redirect(url_for('users_blueprint.index'))
    else:
        return "UPDATE USER ERROR"