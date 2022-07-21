
import json
from flask import Flask,jsonify
from requests import request
import module_relay as mt

app = Flask(__name__)


@app.route('/prova')
def helloworld():
    return jsonify({"about": " Helloworld !"})

@app.route('/status', methods=['GET', 'POST'] )   #rotta per la get delle temperature
def get_status():
    # if (request.method == 'GET'):             -- controllare perchè non funziona if 
        json_temps = json.dumps(mt.get_stat())   # dump della lista delle temperature presa in module_temp.py
        return json_temps

@app.route('/set_relay/<int:id_relay>', methods=[ 'GET','POST'])
def set_r(id_relay):
    json_r = json.dumps(mt.set_stat(id_relay))
    return json_r


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5001)