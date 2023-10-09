from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

from model.souls import Data


souls2_api = Blueprint('souls2_api', __name__, url_prefix='/api/souls')
api = Api(souls2_api)

class DataResource(Resource):
    def get(self, object_id):
        try:
            data_object = Data.get_by_id(object_id)
            
            if data_object:
                serialized_data = data_object.to_dict()
                
                return jsonify(serialized_data), 200
            else:
                return jsonify({'error': "object not found"}), 404
        except Exception as e:
            return jsonify({'error': "object not found"}), 500
api.add_resource(DataResource, '/<int:object_id>')

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprints(souls_api)
    app.run(debug=True)