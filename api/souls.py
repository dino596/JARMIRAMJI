import flask
import flask_restful

import model

# blueprint to organize the code
souls_api = flask.Blueprint('souls_api', __name__, url_prefix = '/api/souls')
api = flask_restful.Api(souls_api)

class testAPI:

    # reads the data
    class _Get(flask_restful.Resource):

        # reads from data_id if given
        def get(self, data_id = None):
            if data_id:
                number = model.souls.data.get(data_id)
                if number:
                    return {'id': data_id, 'data': number}
                else:
                    return {'error': 'Not Found'}
            else:
                return {'data': model.souls.data}
        
    # adds to the data
    class _Add(flask_restful.Resource):
        def post(self):

            # gets key: value from get_json()
            item = flask.request.get_json()
            key = item.get('key')
            value = item.get('value')
            if key and value:

                # adds a new id in data
                id = max(model.souls.data.keys()) + 1
                model.souls.data[id] = {key: value}
                return {'success': model.souls.data[id]}
            else:
                return {'error': 'Invalid Data'}

    # delete from the data
    class _Delete(flask_restful.Resource):
        def delete(self, data_id):
            if data_id in model.souls.data:
                del model.souls.data[data_id]
                return {'success': data_id}
            else:
                return {'error': "Not Found"}
    
    # building RESTapi routes
    api.add_resource(_Get, '/get/<int:data_id>')
    api.add_resource(_Add, '/add')
    api.add_resource(_Delete, '/delete/<int:data_id>')

def damage(attack, resistance, power):
    basicattack = attack
    enhancedattack = attack * power
    ultimateattack = attack * power * power

    baiscattackdamage = basicattack/resistance
    enhancedattackdamage = enhancedattack/resistance
    ultimateattackdamage = ultimateattack/resistance
    return

class soulsAPI:
    pass

app = flask.Flask(__name__)
if __name__ == "__main__":
    app.run(port=5001)