# Visualização

# Importe as bibliotecas necessárias
import Analise_exploratoria as ae
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
from wordcloud import WordCloud

# Use fundo preto para os gráficos
plt.style.use("dark_background")

# Recebe um dataframe e cria um gráfico de barras para a popularidade das músicas mais ouvidas 
def most_listened_plot(dataframe):
    data = ae.most_listened(dataframe)
    plot = sns.barplot(data=data, x="Popularity", y=data.index.get_level_values(1), color = 'g')
    plot.set(title='Mais ouvidas')
    plt.show()
      
def least_listened_plot(dataframe):
    data = ae.least_listened(dataframe)
    sns.barplot(data=data, x="Popularity", y=data.index.get_level_values(1))
    plt.show()
    
def longest_plot(dataframe):
    data = ae.longest(dataframe)
    sns.barplot(data=data, x="Duration", y=data.index.get_level_values(1))
    plt.show() 
    
def shortest_plot(dataframe):
    data = ae.shortest(dataframe)
    sns.barplot(data=data, x="Duration", y=data.index.get_level_values(1))
    plt.show()

  
def common_words_by_lyrics_plot(dataframe):
    resultado = ae.common_words_by_lyrics(dataframe)
    frequency = {}
    for tupla in resultado: 
        frequency[tupla[0]] = tupla[1]
    wc = WordCloud(background_color="white", max_words=1000)
    wc.generate_from_frequencies(frequency)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    
    
    
def common_words_by_song_plot(dataframe):
    resultado = ae.common_words_by_song(dataframe)
    frequency = {}
    for tupla in resultado: 
        frequency[tupla[0]] = tupla[1]
    wc = WordCloud(background_color="white", max_words=1000)
    wc.generate_from_frequencies(frequency)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    
    
def common_words_by_album_plot(dataframe):
    resultado = ae.common_words_by_album(dataframe)
    frequency = {}
    for tupla in resultado: 
        frequency[tupla[0]] = tupla[1]
    wc = WordCloud(background_color="white", max_words=1000)
    wc.generate_from_frequencies(frequency)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
