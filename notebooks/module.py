#Quì mettiamo tutte le funzioni utilizzate

import matplotlib.pyplot as plt

def raman_plot():
    """
    Funzione che serve per settare la dimensione dell'immgine e i label degli assi per un plot di spettro Raman.
    """
    import matplotlib.pyplot as plt
    plt.figure(figsize=(16,6))
    plt.xlabel("wave number [1/cm]")
    plt.ylabel("Intensity")
