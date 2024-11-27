import requests
from colors import write, WARNING, GOOD, ERROR

def trytoprint(res):
    try:
        if(res.status_code == 200):
            write(str(res.json()), GOOD)
            return res
    except requests.exceptions.JSONDecodeError:
        return res

def req(url : str, payload : dict, method : str):
    write(str(payload), WARNING)
    match method:
        case "post":
            res = requests.post(url, params=payload)
            return trytoprint(res)

        case "get":
            res = requests.get(url, params=payload)
            return trytoprint(res)

        case _:
            write("Unknow method of request", ERROR)
        
    return ""

def check_ownership_of_generator(url : str, payload : dict = None):
    #res = requests.post(url, params=payload)
    return req(url, payload, "post")
    
def get_adaccesscode(url : str, payload : dict):

    #res = requests.get(url, params=payload)
    return req(url, payload, "get")
    
def check_user_verification(url : str, payload : dict):
    #res = requests.post(url, params=payload)
    return req(url, payload, "post")

def verify_user(url : str, payload : dict):
    #res = requests.get(url, params=payload)
    return req(url, payload, "get")
    
def generate_img(url : str, payload : dict):
    #res = requests.post(url, params=payload)
    return req(url, payload, "post")

def get_generated_img(url : str, payload : dict):
    #res = requests.get(url, params=payload)
    return req(url, payload, "get")
   
def get_image(url : str, payload : dict):
    #res = requests.get(url, params=payload)
    return req(url, payload, "get")