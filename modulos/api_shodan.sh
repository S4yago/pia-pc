#!/bin/bash

get_data() {
  echo -e "\n[!] Haciendo una busqueda en la IP: $IP"
  data=$(curl --silent -X GET "https://api.shodan.io/shodan/host/$IP?key=$API_KEY")
  echo "$data" | jq -j '"[+] Dirección: ", .ip_str, "\n",
                        "[+] Pais: ", .country_code, "\n",
                        "[+] Ciudad: ", .city, "\n",
                        "[+] ISP: ", .isp, "\n",
                        "[+] Organización: ", .org, "\n",
                        "[+] Puertos: ", .ports' > ./data/shodan/"$IP".txt
  echo -e "\n\nEL RESTO DE LA INFORMACIÓN EN FORMATO JSON\n\n $data" >> ./data/shodan/"$IP".txt
}

API_KEY=$1
FILE_PATH=$2
COUNT=$(wc -w "$FILE_PATH" | cut -d' ' -f1)

[ -d ./data/shodan ] || mkdir ./data/shodan

for ((i = 1; i <= COUNT; i++ )); do
  IP=$(sed -n "$i"p "$FILE_PATH")
  get_data
done
