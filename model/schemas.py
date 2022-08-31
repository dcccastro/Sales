from marshmallow import Schema, fields

class UsersSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    password = fields.String()

class PostsSchema(Schema):
    id = fields.Integer()
    author_id = fields.Integer()
    created_at = fields.DateTime()
    vehicle_id = fields.Integer()
    post_link = fields.String()
    description = fields.String()

class VehicleSchema(Schema):
    id = fields.Integer()
    make_id = fields.Integer()
    model = fields.String()
    year = fields.String()
    gear = fields.String()
    mileage = fields.Integer()
    gas_type = fields.String()
    color = fields.String()

class MakeSchema(Schema):
    id = fields.Integer()
    make_name = fields.String()
    category = fields.String()