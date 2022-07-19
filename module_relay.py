
import string
from bs4 import BeautifulSoup
import requests

#url = "StatusTemperature.html"
with open("StatusRelays.html","r") as f:
    doc = BeautifulSoup(f,"html.parser")

#result = requests.get(url)

#print(doc.prettify())
tags = doc.find_all("p")
s = str(tags[0].string) #estrae contenuto tags <p> .. <\p>
print(s)
l= s.split()   #divide la stringa in lista 
l.pop(0)    #elimino primo elemento 
status = []

for i in range(2):
    status.append(l[i])
print(status)







