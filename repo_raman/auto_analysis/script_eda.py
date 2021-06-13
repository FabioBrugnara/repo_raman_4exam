import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import sys
#sys.path.append('~/Desktop/repo_raman/')
#from functions.functions import *
from functions import define_names, import_pure_spectra, raman_plot
font = {'size': 15}

data_name = input("\nInsert the name of your data, the data should be placed in the path './data/raw'. \nPress 1 for default value -> 'S1_bkg_mapA_11x11.txt'\nPress 2 for default value -> 'S2_bkg_mapA_11x11.txt'.\nOtherwise type the name of your data:")
if data_name == '1':
    data_name = "S1_bkg_mapA_11x11.txt"
if data_name == '2':
    data_name = "S2_bkg_mapA_11x11.txt"


elimina = input("\nDo you want to use the 'elimination of non physical spectrums' (see the EDA notebook for details) (recommended for S2, bad datas)? (y/n)")
if elimina=='y':
    bb = input("\nSet the bound for the 'non physical spectrum selection' made on the tail of the spectrums'(see the EDA notebook for details)? (enter for default: bound=0.001)")
    if len(bb)<1:
        bb=0.001
    else:
        bb=float(bb)
    



raw_data_path = "../../data/raw/" + data_name
names=define_names()
data = pd.read_csv(raw_data_path, delim_whitespace=True, names=names)
pure_material_names, pure_materials=import_pure_spectra('../../data/raw/Database Raman/BANK_LIST.dat','../../data/raw/Database Raman/')

# normalizzazione spettri puri
for i in pure_material_names:
    pure_materials[i+'_I']=pure_materials[i+'_I']/np.trapz(abs(pure_materials[i+'_I'].dropna()), x=pure_materials[i+'_wn'].dropna())

raman_plot()
plt.rc('font',**font)
for i in range(len(pure_material_names)):
    plt.plot(pure_materials[pure_material_names[i]+'_wn'],pure_materials[pure_material_names[i]+'_I'])
    plt.plot([1230,1230],[-0.004,0.08])
plt.savefig("../../reports/figures/pure_normalized_specrtums.png",format = 'png')

raman_plot()
plt.rc('font',**font)
plt.plot(data.wn,data.r1c1)
plt.plot(data.wn,data.r1c2)
plt.plot(data.wn,data.r1c3)
plt.legend(['row 1 column 1','row 1 column 2','row 1 column 3'])
plt.savefig("../../reports/figures/first_spectrums.png",format = 'png')

raman_plot()
plt.rc('font',**font)
for temp in names[1:]:
    plt.plot(data.wn,data[temp])
plt.savefig("../../reports/figures/all_spectrums.png",format = 'png')

# rimozione dell'offset
wn_soglia=1250
for i in enumerate(data.wn):
    if wn_soglia==i[1]:
        element_soglia=i[0]

for temp in names[1:]:
    offset=data[temp][element_soglia::].mean()
    data[temp]=data[temp]-offset

# normalizzazione spettri sample
for i in names[1:]:
    data[i]=data[i]/np.trapz(abs(data[i][:element_soglia]), x=data['wn'][0:element_soglia])

# eliminazione spettri brutti
if elimina=='y':
    for temp in names[1:]:
        maxx=max(data[temp][element_soglia:])
        if maxx>bb :
            for i in enumerate(data[temp]):
                data[temp][i[0]]=0

data[0:element_soglia].to_csv("../data/EDA_processed_data.csv")