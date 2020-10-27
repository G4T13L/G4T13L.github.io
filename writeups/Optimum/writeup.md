# Optimum

## scanning

```bash
sudo nmap -p- -sS --open -vvv --min-rate 5000 10.10.10.8 -oG allPorts -n -Pn
nmap -sC -sV -p 80 -Pn -n 10.10.10.8 -oN targeted
```
![204738.png](204738.png)

## 