# full api :- https://image-generation.perchance.org/api/generate?prompt={prompt}&seed=-1&resolution=512x768&guidanceScale=7&negativePrompt=&channel=ai-character-generator&subChannel=public&userKey=250a34644844c24e59b3adbda85f50d7362865cadcda70ea36a0f6946f83a08f&adAccessCode=a602bec928b76bb00a61e2f77e2e867341acc28a975d1b81d1474316fb4610fd&requestId=0.4140676407551427&__cacheBust=0.3979393155120885
# get gen image api :- https://image-generation.perchance.org/api/downloadTemporaryImage?imageId={imageid}

import PIL.Image
import config
import calls
import os
from colors import write, WARNING, GOOD, ERROR, art, skullart
from style import style
import time
from utils import load
import random

def pickstyles(prompt):
    x = 1
    style_keys = list(style.keys())

    for i in style_keys:
        write(f"{x} - {i}", GOOD)
        x += 1
 
    style_idx = 1
    
    try:
        style_idx = int(input("Pick a style press enter for no-style \n👉 "))

        if(style_idx > len(style)):
            write("Invalid style pick from the list", ERROR)
            return pickstyles(prompt)

    except ValueError:
        write("Invalid style", ERROR)
        return pickstyles(prompt)

    except TypeError:
        write("Invalid style", ERROR)
        return pickstyles(prompt)

    return (prompt + "," + style[style_keys[style_idx - 1]][0], style[style_keys[style_idx - 1]][1])

def verificationandstuff():
    write("Starting user verification", WARNING)
    res = calls.check_ownership_of_generator(config.CHECK_GENERATOR_OWNERSHIP_API, config.get_check_generator_ownership_payload())

    #adaccess_code_response = calls.get_adaccesscode(config.ADACCESSCODE_API, config.get_adaccesscode_payload())

    verified = False

    while not verified:
        usr_veri = calls.check_user_verification(config.CHECK_USER_VERIFICATION_API, config.get_check_user_verification_payload(config.USER_KEY))

        if(usr_veri != str and usr_veri.json()["status"] == "not_verified"):
            verify_usr = calls.verify_user(config.VERIFY_USER_API, config.get_verify_user_payload())

            if(verify_usr.json()["status"] == "failed_verification"):
                write(f"Failed to verify user {verify_usr.json()["reason"]}", ERROR)
        
                write("Retrying...", WARNING) 

        if(usr_veri != str and usr_veri.json()["status"] == "verified"):
            write("User verification successfull", GOOD)
            verified = True

        time.sleep(2)

def askprompt():
    write(art, GOOD) 

    prompt = ""
    while prompt == "":
        prompt = input("type quit/q to exit \n👉 ")

        if(prompt.lower() == "quit" or prompt.lower() == "q"): 
            exit(0)

    return pickstyles(prompt)

def generate():
    prompt = askprompt()

    gen_img = calls.generate_img(config.GENERATOR_API, config.get_generator_payload(prompt[0], prompt[1], config.USER_KEY, config.ADACCESSCODE))
    load(random.randint(1,150), "Generating ")

    if(gen_img.json()["status"] == "success"):
        image_data = calls.get_generated_img(config.DOWNLOAD_IMAGE_API, config.get_image_payload(gen_img.json()["imageId"]))
        load(random.randint(1,10), "Downloading ")

        return ("generated_image" + str(int(time.time())) + "." + gen_img.json()["fileExtension"], image_data)
    else:
        write(f"Faled to generate image {gen_img.json()["status"]}", ERROR)
    
    return None

def saveimageandshow(image_data):
    if image_data == None:
        return

    fullpath = os.path.join("logs/", image_data[0])

    with open(fullpath, "wb") as file:
        file.write(image_data[1].content)
        load(10, "Saving ")
        write(f"Saved as {image_data[0]}", GOOD)

    img = PIL.Image.open(fullpath)
    img.show()

def main():
    verificationandstuff()

    while True:
        saveimageandshow(generate())
        input("Press Enter to continue")

if __name__ == "__main__":
   load(random.randint(1,50), "Loading model  ")
   load(random.randint(1,30), "Loading weights")
   load(random.randint(1,20), "Checking Apis  ")

   write(skullart, WARNING)

   main()