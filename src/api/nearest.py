from flask import Flask, request
import json

application = Flask(__name__)

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)


@application.route('/nearest', methods=['POST'])
def hello_world():

    if request.method == 'POST' and request.is_json:

        latitude = request.json['latitude']
        longitude = request.json['longitude']
        precision = request.json['precision']

        jumps = nearest_jumps(latitude, longitude, precision)
        return json.dumps(jumps);

    return 'It must be method=POST and mimetype=application/json'



def nearest_jumps(latitude, longitude, precision):

    jumps = [
                {
                    'id': 76,
                    'latitude': 43.3674647,
                    'longitude': -8.438327,
                    'distance': 290,
                    'mean': "bus",
                    'info': {
                        'address': "Ronda de Outeiro, 54"
                        }
                    },
				{ 
					'id': 34,
					'latitude': 43.3848483,
					'longitude': -8.433362,
					'distance': 434,
					'mean': "bike",
					'info': {
						'address': "Estacion de trens"
						}
					},
				{ 
					'id': 77,
					'latitude': 43.383848,
					'longitude': -8.433838,
					'distance': 560,
					'mean': "bus",
					'info': {
						'address': "Alfonso Molina, 112"
						}
					}
            ]

    return jumps

