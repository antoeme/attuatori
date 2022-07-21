
import string
from urllib import response
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth

url_relays = "http://10.10.10.82/relays.cgi"
url_set_relay = "http://10.10.10.82/relays.cgi?relay="  #bisogna appendere "1" o "2" per decidere quale relay cambiare
username = "admin"
password = "dtl4b1tc2022!"
#with open("StatusRelays.html","r") as f:


def get_stat():
    result = requests.get(url_relays,auth=HTTPBasicAuth(username,password))   
    doc = BeautifulSoup(result.text,"html.parser")

    tags = doc.find_all("p")

    s = str(tags[0].string) #estrae contenuto tags <p> .. <\p>
    #print(s)
    l= s.split()   #divide la stringa in lista 
    l.pop(0)    #elimino primo elemento 
    status = {}

    for i in range(2):
        status["Relay"+str(i+1)] = int(l[i])
    return(status)

def set_stat(r):
    url = url_set_relay + str(r)
    result = requests.get(url,auth=HTTPBasicAuth(username,password)) 
    return "cambiato stato relay" + str(r)

#stat = set_stat(2)
# print(stat)









