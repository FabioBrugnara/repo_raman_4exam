import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from functions import import_pure_spectra

labels=np.loadtxt("../data/CLUSTERING_labels.txt")
data = pd.read_csv("../data/CLUSTERING_data_centres.csv")
data.drop(labels='Unnamed: 0',inplace=True,axis=1)

pure_material_names, pure_materials=import_pure_spectra('../../data/raw/Database Raman/BANK_LIST.dat','../../data/raw/Database Raman/')

# interpolazione dei dati
pure_materials_interpoled=pd.DataFrame(data.wn.copy())
for temp in pure_material_names:
    pure_materials_interpoled=pure_materials_interpoled.join(pd.DataFrame(np.interp(data.wn, pure_materials[temp+'_wn'] ,pure_materials[temp+'_I']),columns=[temp]))

#Normalizzazione
for i in pure_material_names:
    pure_materials_interpoled[i]=pure_materials_interpoled[i]/np.trapz(abs(pure_materials_interpoled[i].dropna()), x=pure_materials_interpoled.wn)

# fit 
ols=LinearRegression(positive=True)
N_cluster=len(data.columns)-1
coeff=[]
intercept=[]
for i in range(N_cluster):
    ols.fit(pure_materials_interpoled[pure_material_names], data[str(i)]) #ottimizziamo il modello (lineare) su i dati di training
    coeff.append(ols.coef_)
    intercept.append(ols.intercept_)

fig, axs = plt.subplots(nrows = N_cluster,figsize = (16,38))
for i in enumerate(range(N_cluster)):
    axs[i[0]].plot(data.wn,data[str(i[0])])
    axs[i[0]].plot(pure_materials_interpoled.wn,intercept[i[0]]+np.sum(pure_materials_interpoled[pure_material_names] * coeff[i[0]] ,axis=1))
    axs[i[0]].set_title('Cluster ' + str(i[0]))
    axs[i[0]].legend(['centroide','fit'], loc='upper right')
plt.savefig("../../reports/figures/final_FIT.png",format = 'png')

# determinazione abbondanza materiale

weights=[np.count_nonzero(labels==i) for i in range(len(data.columns)-1)]
abb_notnormalized=[coeff[i]*weights[i] for i in range(len(data.columns)-1)]
abb=sum(abb_notnormalized)/(sum(abb_notnormalized).sum())

abb_table=pd.DataFrame({'names':pure_material_names,'abbundances':abb})
abb_table.sort_values('abbundances',ascending=False,inplace=True, ignore_index=True)

abb_table.to_csv("../data/abb_table.csv")