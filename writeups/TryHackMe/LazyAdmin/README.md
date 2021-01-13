# LazyAdmin

## scanning

```bash
sudo nmap -p- -sS --open -vvv --min-rate 5000 10.10.224.91 -oG allPorts
sudo nmap -p 22,80 -sS -sC -sV 10.10.224.91 -oN targeted
```

![224951.png](224951.png)

## 80

