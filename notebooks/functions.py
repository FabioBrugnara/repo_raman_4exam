#Quì mettiamo tutte le funzioni utilizzate

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def raman_plot():
    """
    Funzione che serve per settare la dimensione dell'immgine e i label degli assi per un plot di spettro Raman.
    """
    plt.figure(figsize=(16,6))
    plt.xlabel("wave number [1/cm]")
    plt.ylabel("Intensity")

def define_names(r=11,c=11):
    """
    Funzione che definisce i nomi delle coordinate degli spettri sul sample. I nomi sono del tipo r1c1,r1c2, ecc.
    Come default usa 11 colonne e 11 righe. Il primo nome è wn, che sta per wave number.
    """
    #definisco i nomi da assegnare ai punti delli spettri di sampling
    #wn -> wave number  r -> row c -> columns
    names = ['wn']+[f'r{k}c{i}' for k in range(1,r+1) for i in range(1,c+1)]
    return names

def import_pure_spectra(element_list,directory):
    """
    Funzione per importare gli spettri puri.
    element_list: direcory del file contenente la lista dei file con gli spettri dei materiali puri. Il file deve essere del tipo
    -Abelite.txt
    -Quarzo.txt
    La funzione prende i nomi, salvandoli nella variabile pure_material_names. Poi prende i file (.txt) contenuti nella directory directory che devono essere due colonne (wn e intensità) separate da uno spazio.Restituisce un pandas dataframe.
    Attenzione ai NaN se i file non hanno la stessa lunghezza
    """

    # gli spettri Raman dei materiali puri hanno ognuno uno wn diverso, generiamo dunque un dataframe vuoto delle
    # dimensioni corrette (del materiale con più dati), e poi aggiungiamo 2 colonne per spettro con wn e l'intensità (probabilmente c'è un 
    # metodo migliore)

    # definisco i nomi dei vari materiali usando il file che li contiene tutti
    pure_material_names=[]
    with open(element_list) as f:
        pure_material_names=[i[1:len(i)-5] for i in f.readlines()]
    l=[]
    # calcolo la dimensione del materiale puro con più dati
    for i in range(len(pure_material_names)):
        l.append(pd.read_csv(directory+pure_material_names[i]+'.txt', delim_whitespace=True, names=[pure_material_names[i]+'_wl',pure_material_names[i]+'_I']).size)
    max_size=int(max(l)/2)
    # genero un dataframe vuoto per poter usare il metodo join
    pure_materials = pd.DataFrame(np.zeros(max_size),columns=['empty'])
    # importiamo i dati: nome_I (intensità) e nome_wn
    for i in range(len(pure_material_names)):
        pure_materials=pure_materials.join(pd.read_csv('../data/raw/Database Raman/'+pure_material_names[i]+'.txt', delim_whitespace=True, names=[pure_material_names[i]+'_wn',pure_material_names[i]+'_I']))
    
    pure_materials.drop('empty', axis = 1,inplace=True)
    return pure_material_names,pure_materials