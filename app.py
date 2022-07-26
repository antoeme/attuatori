
import json
from flask import Flask, jsonify
import requests
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth as aut

from os import getenv
from dotenv import load_dotenv


URL_RELAY = getenv("URL_RELAY") 
URL_SET_RELAY = getenv("URL_SET_RELAY") #bisogna appendere "1" o "2" per decidere quale relay cambiare
# USERNAME = getenv("USERNAME") or "admin"
# PASSWORD = getenv("PASSWORD") or "dtl4b1tc2022!"
USERNAME = "admin"
PASSWORD = "dtl4b1tc2022!"

# load environment variables from '.env' file
load_dotenv()

def get_stat():
    result = requests.get(str(URL_RELAY), auth=aut(USERNAME,PASSWORD))   
    doc = BeautifulSoup(result.text,"html.parser")

    tags = doc.find_all("p")

    s = str(tags[0].string) #estrae contenuto tags <p> .. <\p>
    
    l= s.split()   #divide la stringa in lista 
    l.pop(0)    #elimino primo elemento 
    status = {}

    for i in range(2):
        status["Relay"+str(i+1)] = int(l[i])
    return(status)

def set_stat(r):
    url = str(URL_SET_RELAY) + str(r)
    result = requests.get(url,auth=aut(USERNAME,PASSWORD)) 
    return "cambiato stato relay " + str(r)


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


@app.route('/prova', methods=['GET'] )   
@auth.login_required
def prova():
    return jsonify("prova")


@app.route('/status', methods=['GET'] )   #rotta per la get dello stato dei relay
#@auth.login_required
def get_status():
    json_temps = json.dumps(get_stat())   # dump della lista dello stato dei relay
    return json_temps

@app.route('/set_relay/<int:id_relay>', methods=[ 'GET','POST'])
@auth.login_required
def set_r(id_relay):
    if(id_relay != 1) and (id_relay != 2):  
        return ("Errore: ID del relay errato")
    else:
        json_r = json.dumps(set_stat(id_relay))
        return json_r

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True,port=5001)