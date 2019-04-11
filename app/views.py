from flask import Blueprint, Response
from models import User, Group

api = Blueprint('api', __name__)

@api.route("/api/ldap/users/<name>", methods=['GET'])
def get_users_by_name(name):
    users = User.get_users_by_id(name)
    return Response(response=users, status=200)
    
@api.route("/api/ldap/users", methods=['GET'])
def get_users():
    users = User.get_users()
    return Response(response=users, status=200)
    
@api.route("/api/ldap/groups", methods=['GET'])
def get_groups():
    groups = Group.get_groups()
    return Response(response=groups, status=200)