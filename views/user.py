from flask import jsonify, request
from werkzeug.security import generate_password_hash
from model.db_models import Users, db
from model.schemas import UsersSchema

def create_user(): 
    post_data = request.get_json()
    user = Users.query.filter_by(email = post_data.get("email")).first()
    if not user:
        try:
            user = Users(
                first_name= post_data.get('first_name'),
                last_name= post_data.get('last_name'),
                email = post_data.get('email'),
                password = generate_password_hash(post_data.get('password'))
            )
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            jsonify({"error":"{e}"})
    return jsonify({'Message': "error"})

def get_all_users(): #users
    try:
        users = Users.query.filter().all()
        schema = UsersSchema(many=True)
        data = schema.dump(users)
        return jsonify({'Data': data})
    except Exception as e:
        return jsonify({"error":"{e}"})


def get_user(id): #users id or name
    pass



def edit_user(id):
    pass

def delete_user(id):
    try:
        user = Users.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

        return jsonify("Message:" "Deleted succesfully")
        
    except Exception as e:
        jsonify({"error":"{e}"})