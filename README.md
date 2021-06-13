# Progetto di Data Science: Analisi di spettri Raman
*Fabio Brugnara e Andrea Pegoretti*

In questo progetto abbiamo lavorato con gli spettri Raman eseguiti su un campione di materiale incognito. Lo scopo del progetto è quello di identificare la composizione del materiale sfruttando gli spettri di diversi materiali puri.

Una spiegazione dettagliata del progetto e dei suoi vari step è contenuta nei notebooks [EDA.ipynb](https://github.com/FabioBrugnara/repo_raman/blob/main/notebooks/EDA.ipynb), [CLUSTERING.ipynb](https://github.com/FabioBrugnara/repo_raman/blob/main/notebooks/CLUSTERING.ipynb) e [FIT.ipynb](https://github.com/FabioBrugnara/repo_raman/blob/main/notebooks/FIT.ipynb) (in './notebooks'). Qui abbiamo utilizzato il primo set di dati (S1) presente nella cartella './data/raw'. Per comprendere a fondo il progetto fare riferimento a questi notebooks.

In questi notebooks si trova

1. l'**Exploratory Data Analysis** e la preparazione dei dati ([EDA.ipynb](https://github.com/FabioBrugnara/repo_raman/blob/main/notebooks/EDA.ipynb))
2. il **clustering** degli spettri utilizzato per verificare se esiste una correlazione spaziale tra gli spettri e per preparare i dati al fit ([CLUSTERING.ipynb](https://github.com/FabioBrugnara/repo_raman/blob/main/notebooks/CLUSTERING.ipynb))
3. il fit agli spettri puri e il risultato finale: **le abbondanze presenti nel campione** ([FIT.ipynb](https://github.com/FabioBrugnara/repo_raman/blob/main/notebooks/FIT.ipynb))

## Automatizzazione con make

Abbiamo infine implementato un'automatizzazione dell'analisi utilizzando make.

- **make eda_cluster_fit**	Effettua tutta l'analisi in automatico, richiede di inserire il nome del file di dati da utilizzare (dati con background rimosso), che deve essere inserito nella directory ./data/raw (con invio si utilizza i dati del sample S1 di default). Il file dei dati deve essere strutturato come quelli già presenti (vedi [EDA.ipynb](https://github.com/FabioBrugnara/repo_raman/blob/main/notebooks/EDA.ipynb))

- **make visualization** Fa il run di [report.ipynb](https://github.com/FabioBrugnara/repo_raman/blob/main/report/report.ipynb) ('./report'), che è il notebook contenente l'Exploratory Data Analysis e la presentazione dei risultati provenienti dall'analisi automatizzata effettuata con il comando **make eda_cluster_fit**. Salva inoltre il notebook nella stessa cartella in formato html. Infine, se firefox è installato sul computer, lo apre in automatico.

- **make create_environment** Se sul proprio computer e' presente un installazione conda eseguire con make questo comando altrimenti sara' necessario creare un environment virtuale con pyhton (per farlo e' necessario avere installato pip). Per inizializzare l'environment eseguire sulla shell i seguenti comandi.
```console
    pip install virtualenv
    virtualenv name_of_the_env
```
Per attivare l'environment:
```console
    source name_of_the_env/bin/activate
```
per disattivare l'environment:
```console
    deactivate
```
- **make test_environment** Verifica se l'envirorment è settato correttamente

- **make requirements** Installa le dipendenze necessarie

