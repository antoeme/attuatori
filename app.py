
import json
from flask import Flask,jsonify
from requests import request
import module_relay as mt
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "daniele": generate_password_hash("Cisco123"),
    "antonio": generate_password_hash("Dtlab123")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/prova')
def helloworld():
    return jsonify({"about": " Helloworld !"})

@app.route('/status', methods=['GET'] )   #rotta per la get delle temperature
@auth.login_required
def get_status():
    json_temps = json.dumps(mt.get_stat())   # dump della lista delle temperature presa in module_temp.py
    return json_temps

@app.route('/set_relay/<int:id_relay>', methods=[ 'GET','POST'])
@auth.login_required
def set_r(id_relay):
    if(id_relay != 1) and (id_relay != 2):  #controllare nel caso in cui si inserisce un carattere
        return ("Errore: ID del relay errato")
    else:
        json_r = json.dumps(mt.set_stat(id_relay))
        return json_r

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5001)