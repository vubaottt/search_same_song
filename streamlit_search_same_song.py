import streamlit as sl
import pandas as pd
import re

def convert_object_to_list(data):
    data = data.replace('[ ', "")
    data = data.replace('[', "")
    data = data.replace(' ]', "")
    data = data.replace(']', "")
    data = data.strip()
    data = re.sub(' +', ' ', data)
    tokens = data.split(" ")
    result = []
    for token in tokens:
        result.append(int(token))
    return result

df_data = pd.read_csv('data.csv')
df_result = pd.read_csv('result.csv')
df_result['list_index'] = df_result.apply(lambda x: convert_object_to_list(x['similarities_id']), axis=1)
df_spring = pd.read_csv('spring_song.csv')
df_summer = pd.read_csv('summer_song.csv')
df_winter = pd.read_csv('winter_song.csv')

menu = ["Overview", "Data Crawed", "Search Same Song"]
choice = sl.sidebar.selectbox('Menu', menu)
if choice == 'Overview':
    sl.subheader("Overview")
    sl.write("""
    #### Add later
    """)
elif choice == "Data Crawed":
    sl.subheader("Data Crawed")
    sl.write("##### Spring song({} songs)".format(len(df_spring)))
    sl.table(df_spring)
    sl.write("##### Summer song({} songs)".format(len(df_summer)))
    sl.table(df_summer)
    sl.write("##### Winter song({} songs)".format(len(df_winter)))
    sl.table(df_winter)
elif choice == 'Search Same Song':
    sl.subheader("Search Same Song")
    menu_song = df_data['name'].tolist()
    menu_song.sort()
    choice_song = sl.sidebar.selectbox('Search Song', menu_song)
    index_search_song = df_data.index[df_data['name'] == choice_song].tolist()
    index_top_5_similar = df_result.iloc[index_search_song[0]]
    top_5_similar = df_data.iloc[index_top_5_similar['list_index']]
    sl.write("#### Top 5 songs with similar content:")
    sl.table(top_5_similar)
