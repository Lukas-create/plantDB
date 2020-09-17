import pandas as pd
import platform
import numpy as np
from plant import Plant
def habitat_search(Spalte, eintrag):
    df = pd.read_csv('Pflanzendaten.csv', encoding='unicode_escape')
    if platform.system() == 'Linux':
        df = pd.read_csv('Pflanzendaten.csv')
    else:
        df = pd.read_csv('Pflanzendaten.csv', encoding='unicode_escape')
    df1 = df.dropna()
    df2 = df1.to_numpy()
    def search(Spalte,eintrag,df):
        df2 = df.to_numpy()
        Spalte=df[Spalte]
        Name=df['NameSpez']
        for i in range(len(Spalte)):
            if Spalte[i]==eintrag:
                plant = Plant(df2[i, 0], df2[i, 1], df2[i, 2], df2[i, 3], df2[i, 4], df2[i, 5])
                plant.print_habitat()
        else:
            print(' ')

    search(Spalte, eintrag, df1)
