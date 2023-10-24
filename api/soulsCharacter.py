from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.soulsCharacter import SoulsCharacter

soulsCharacter_bp = Blueprint("soulsCharacter", __name__)
soulsCharacter_api = Api(soulsCharacter_bp)

class SoulsCharacterAPI(Resource):
    def get(self):
        id = request.args.get("id")
        soulsCharacter = db.session.query(SoulsCharacter).get(id)
        if soulsCharacter:
            return soulsCharacter.to_dict()
        return {"message": "not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True, type=str)
        parser.add_argument("gender", required=True, type=str)
        parser.add_argument("age", required=True, type=int)
        parser.add_argument("class_name", required=True, type=str)
        parser.add_argument("health", required=True, type=int)
        parser.add_argument("attack", required=True, type=int)
        parser.add_argument("resistance", required=True, type=int)
        parser.add_argument("power", required=True, type=int)
        args = parser.parse_args()
        soulsCharacter = SoulsCharacter(args["name"], args["gender"], args["age"], args["class_name"], args["health"], args["attack"], args["resistance"], args["power"])

        try:
            db.session.add(soulsCharacter)
            db.session.commit()
            return soulsCharacter.to_dict(), 201
        except Exception as exception:
            db.session.rollback()
            return {"message":f"error {exception}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        parser.add_argument("name", type=str)
        parser.add_argument("gender", type=str)
        parser.add_argument("age", type=int)
        parser.add_argument("class_name", type=str)
        parser.add_argument("health", type=int)
        parser.add_argument("attack", type=int)
        parser.add_argument("resistance", type=int)
        parser.add_argument("power", type=int)
        args = parser.parse_args()
        
        try:
            soulsCharacter = db.session.query(SoulsCharacter).get(args["id"])
            if soulsCharacter:
                if args["name"] is not None:
                    soulsCharacter.name = args["name"]
                if args["gender"] is not None:
                    soulsCharacter.gender = args["gender"]
                if args["age"] is not None:
                    soulsCharacter.age = args["age"]
                if args["class_name"] is not None:
                    soulsCharacter.class_name = args["class_name"]
                if args["health"] is not None:
                    soulsCharacter.health = args["health"]
                if args["attack"] is not None:
                    soulsCharacter.attack = args["attack"]
                if args["resistance"] is not None:
                    soulsCharacter.resistance = args["resistance"]
                if args["power"] is not None:
                    soulsCharacter.power = args["power"]
                db.session.commit()
                return soulsCharacter.to_dict(), 200
            else:
                return {"message": "not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"error {exception}"}, 500
    
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            soulsCharacter = db.session.query(SoulsCharacter).get(args["id"])
            if soulsCharacter:
                db.session.delete(soulsCharacter)
                db.session.commit()
                return soulsCharacter.to_dict()
            else:
                return {"message": "not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"error {exception}"}, 500

class SoulsCharacterListAPI(Resource):
    def get(self):
        soulsCharacter = db.session.query(SoulsCharacter).all()
        return [soul.to_dict() for soul in soulsCharacter]

soulsCharacter_api.add_resource(SoulsCharacterAPI, "/soulsCharacter")
soulsCharacter_api.add_resource(SoulsCharacterListAPI, "/soulsCharacterList")