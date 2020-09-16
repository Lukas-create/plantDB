import pandas as pd
import platform
import numpy as np
from plant import Plant
def habitat_search(Spalte, eintrag):
    #bisher alle spezifischen Arten und Daten nur placeholder
    df = pd.read_csv('Pflanzendaten.csv', encoding='unicode_escape')
    if platform.system() == 'Linux':
        df = pd.read_csv('Pflanzendaten.csv')
    else:
        df = pd.read_csv('Pflanzendaten.csv', encoding='unicode_escape')
    #print(df['Habitat'])
    df1 = df.dropna()
    df2 = df1.to_numpy()
    #print(df.columns)
    #print (df.type())
    def search(Spalte,eintrag,df):
        df2 = df.to_numpy()
        #print(df.head(0))
        Spalte=df[Spalte]
        #df(skip[0])
        Name=df['NameSpez']
        for i in range(len(Spalte)):
            if Spalte[i]==eintrag:
                #print(Name[i])
                #print(df2[i, :])
                plant = Plant(df2[i, 0], df2[i, 1], df2[i, 2], df2[i, 3], df2[i, 4], df2[i, 5])
                plant.print_habitat()
        else:
            print(' ')

    search(Spalte, eintrag, df1)

    #search(Spalte, eintrag, df1)
