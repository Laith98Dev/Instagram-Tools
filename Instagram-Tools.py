try: 
    import requests
    import uuid
    import time
    import colorama
except Exception as e:
    print(e)

logo = (colorama.Fore.RED + """
Created By
 _           _ _   _    ___   ___  _____             
| |         (_) | | |  / _ \ / _ \|  __ \            
| |     __ _ _| |_| |_| (_) | (_) | |  | | _____   __
| |    / _` | | __| '_ \__, |> _ <| |  | |/ _ \ \ / /
| |___| (_| | | |_| | | |/ /| (_) | |__| |  __/\ V / 
|______\__,_|_|\__|_| |_/_/  \___/|_____/ \___| \_/   """+Style.RESET_ALL);
     
print(logo)


print(colorama.Fore.YELLOW+""" Hey, please login to continue """)

user = input('Username: ')

password = input('Password: ')

target_url = input('Story url: ') 

def login():
    global target_url
    
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
    
    print(loginreq.text)
    
    if loginreq.text.find("is_private") >= 0:
        print(colorama.Fore.YELLOW+"Login Successfully")
        
        r.headers.update({'X-CSRFToken': loginreq.cookies['csrftoken']})
        
        url_id = "https://www.instagram.com/{}/?__a=1".format(target_url)
        
        url_get_user_id = r.get(url_id).json()
        
        print(url_get_user_id)
    else:
        print(colorama.Fore.RED+"Failed Login Check your data!!")
        
