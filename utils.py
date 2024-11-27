from tqdm import tqdm
import time

def load(ran : int, msg : str):
    print(" ")
    for i in tqdm(range(ran), desc=msg):
        time.sleep(0.05) 

