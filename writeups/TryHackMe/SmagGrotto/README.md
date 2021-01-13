#  SMAG GROTTO

## scanning

```bash
furious 22,80 10.10.173.35
nmap -sC -sV -p 22,80 10.10.173.35 -oN targeted
```

![225438.png](225438.png)

## 80

```bash
wfuzz -c --hc 403,404 -t 100 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt http://10.10.173.35/FUZZ
```

![234505.png](234505.png)

we download the pcap file

![232506.png](232506.png)

We found 4 things

1. A login page: **login.php**
2. hostname: **development.smag.thm**
3. username: **helpdesk**
4. password: **cH4nG3M3_n0w**

![232917.png](232917.png)

So we modify the hosts file in our machine to enter to the login page and use the credentials we found.

![234923.png](234923.png)

we make a reverse shell in php to conect, so we have to wait with:

```bash
nc -lvp 4545
```



![002503.png](002503.png)

![005608.png](005608.png)

We are going to change the file to enter to the user jake.

![003118.png](003118.png)

```bash
sudo ssh -i /.ssh/id_rsa jake@10.10.30.100
cat /home/jake/user.txt
```

![005526.png](005526.png)

we use the following commands

![005238.png](005238.png)