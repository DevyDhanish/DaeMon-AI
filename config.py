import random

GENERATOR_API = "https://image-generation.perchance.org/api/generate"
DOWNLOAD_IMAGE_API = "https://image-generation.perchance.org/api/downloadTemporaryImage"
CHECK_USER_VERIFICATION_API = "https://image-generation.perchance.org/api/checkUserVerificationStatus"
VERIFY_USER_API = "https://image-generation.perchance.org/api/verifyUser"
ADACCESSCODE_API = "https://perchance.org/api/getAccessCodeForAdPoweredStuff"
CHECK_GENERATOR_OWNERSHIP_API = "https://perchance.org/api/checkGeneratorOwnership"

SESSION_TOKEN = "4iiftOiI22gj5WdBv2RMx9P9v4O0fp5KNZ4PWkz3GZV1HqfMDAeWHC6Q7qpqOQ08Kg0g8fGq2AwyERdMwrT6q4gnSLdTBjJ4kLsdwwjEk8N9KyppjvZgMqZ17sXlj3QpoaRu31tBIwNWQZgmPxdCKa8sDaDqA7t8xwniEHP5KMn7ZIXwqRpq0YV3tsnzHoWSDFfiHivs"
USER_KEY = "250a34644844c24e59b3adbda85f50d7362865cadcda70ea36a0f6946f83a08f"
TOKEN = "0.xc82O7VzHmHrWapMzungNGVax_Vu1K2DNIsf-zMuV_1kwIGYLQWY9cWKagNz9AcZXr_oO_pQEmX0K4_mtL5Q_wC-4qDd6UR730ewzGU30NcsQ6yC__oMPenx0lEvFm2JlkGaavxgOv-rAND8JXnf_X7P5TfiHFeMnZdxA4kWSIa1a7xSYKYi-pDUGmY_0RwNew5FNAIH_QsaV0XwsNevBMcfiJwf391vQhDKhvYY0SWZHHS_aN2KWrdRWgII_ylZEROPsW6XJe1KFlvARpEAS75famPDb8KKkb7tXxigJXqN9SYFIW1Ai2ZTUyxH1pifeOmy7_pABDRQmimgUIVEO87SykgQDSbnnkCRh-mEZMN4e47c9iAMFQ08tf42R3i9PFQLstmkKx-lwL4TFJrjYEr_teuTL8cab2rxUsw3BKIOoqiskBDL524Z5IJk4oJT6Ae_TqU8LGRbR3x7c44pIYiZGrXvZDN5OZEMR7nQ7EnLs2k1syo8LbmZPSm65HY3e_2BSPqXwDjGkaylv73mPGY_Z6VXkzJnAAm03wwUV0CPNZBFImdgqrU4d3cYdt2ARGXDhjltHqhMu-rJJ9ZaNeUpTu0y_cOiJ2yTM57DbzzSSsu4ST3ThJuhPh6o47IgnLYeJLHrctQ6lkD9knjbQhqXRTzGqxojChMSj1yPCo23GG6yBizOq67Di1PNaRNp80GuRuJhbg5OycVFuAEJDfdTbEn3iJgMGWYfzUPn7q0VqAI95KcT7N-Qwm-uj9iq4aww73yhmFn6wQWlhVYzF5FjCio9ud4MOtA5KL-f900.pFxCbbU3oFSpsS1A40uZwA.350e2ce872f00e93a1cb4adb6aa5535183940a47b5c05dfe52a241bfdc8994cd"
ADACCESSCODE = "2c31583d0f7df4fa9c2029f6557d1226be6718ca1474b9077dcb3a2afaa374f6"

def set_adaccesscode(code : str):
    global ADACCESSCODE
    ADACCESSCODE = code

def set_user_key(key : str):
    global USER_KEY
    USER_KEY = key

def get_check_generator_ownership_payload():
    return {
        "email" : "kmdhanish2018@gmail.com",
        "generatorName" : "ai-character-generator",
        "sessionToken" : SESSION_TOKEN
    }

def get_generator_payload(prompt : str, neg_prompt : str, user_key : str, ad_access_code : str):
    return {
        "prompt": prompt,
        "seed": -1,
        "resolution": "512x768",
        "guidanceScale": 7,
        "negativePrompt": neg_prompt,
        "channel": "ai-character-generator",
        "subChannel": "public",
        "userKey": user_key,
        "adAccessCode": ad_access_code,
        "requestId": 0.731124965931998,
        "__cacheBust": random.random()
    }

def get_check_user_verification_payload(user_key: str):
    return {
    "userKey" : user_key,
    "__cacheBust" : random.random()
}

def get_verify_user_payload():
    return {
    #"token" : TOKEN,
    "thread" : random.randint(1,5),
    "__cacheBust" : random.random()
}

def get_adaccesscode_payload():
    return {
        "__cacheBust": 2887824
    }

def get_image_payload(image_id : str):
    return {
        "imageId" : image_id
    }