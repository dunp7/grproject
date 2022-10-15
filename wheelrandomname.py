import random
import pandas as pd
import imp_data as ipd
def choose_random_game(a):
    #choose random name of game
    i = random.randint(0,len(a)-1)
    return a[i]
def display_infor(a):
#     #hien thong tin tro choi
    for i in range(len(ipd.listgame)):
        if a == ipd.listgame[i]:
            return ipd.x[i]





