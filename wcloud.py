import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup 
import requests 
import re 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS
import wordcloud 

st.markdown("Word Cloud  - App ")

st.sidebar.header("Select Link")
links = ["https://seaportai.com/blog-predictive-maintenance","https://seaportai.com/2019/04/22/healthcare-analytics/","https://seaportai.com/blog-rpameetsai/","https://seaportai.com/covid-19/"]

URL= st.sidebar.selectbox("Links", links)

st.sidebar.header("Select no. of Words")
words = st.sidebar.selectbox("No. of Words",range(10,100,10))


if URL is not None :
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content,"html.parser")
    table = soup.find('div', attrs={'id':'main-content'})
    text = table.text 
    cleaned_text = re.sub("\t","", text )
    cleaned_texts = re.split("\n", cleaned_text)
    cleaned_textss = "".join(cleaned_texts)

    st.write("Word Cloud plot")
    stopwords = set(STOPWORDS)
    wordscloud = WordCloud(background_color="white",max_words=words,stopwords=stopwords).generate(cleaned_textss)

    plt.imshow(wordscloud, interpolation='bilinear')
    plt.axis('off')
    plt.show() 
    st.pyplot() 


