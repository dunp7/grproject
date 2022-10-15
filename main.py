import streamlit as st
import imp_data as ipd
import wheelrandomname as wrn
import pandas as pd
st.header('Let me choose your game ')
st.subheader('A random generator')
#Hien ra so tro choi ng dung muon
num = [i for i in range(0,101,5)]
seln = st.select_slider('Select the number of games',options=num)
#Cho ng dung chon tro choi
lg = ipd.listgame
options = st.multiselect('Choose game',lg)
if len(options) == seln:
    # lay random
    if st.button('Take 1 random game'):
        game = wrn.choose_random_game(options)
        st.title(game)

# hien ra tat ca thong tin tro choi len man hinh
#     disp = wrn.display_infor(game)
#     st.caption('This is all in4 you need')
#     df = pd.DataFrame(disp)
#     st.dataframe(df)
