import views.user
from flask import Blueprint

bp = Blueprint('user_route', __name__)

@bp.route('/users/create/', methods=['POST'])
def create_user():
    return views.user.create_user()

@bp.route('/users/', methods=['GET'])
def get_users():
    return views.user.get_all_users()

@bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    return views.user.delete_user()
