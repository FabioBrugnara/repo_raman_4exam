# Come abbiamo pensato di organizzare il progetto

### Suddivisione in 4 notebook
- EDA + preprocessing
- Clustering
- Fit
- Visualization

### EDA
1. Import dei dati
	- data --> names, "wn r1c1"
	- pure_materials --> pure_materials_name, questi sono i dati dei materiali puri.
	
2. Mostrare spettri puri.
	- Per numeri d'onda superiori (**va trovato meglio il punto**) a 1250 $cm^{-1}$ per tutti gli spettri non ci sono picchi.
	- Gli spettri relativamente alle altezze dei picchi non presentano un offset rilevante.
	- Le FWHM dei picchi sono, certe volte importanti: fino a 100 $cm^{-1}$.
	- Gli spettro fino a circa (**va trovato meglio il punto**) 1250 $cm^{-1}$ sono densamente popolati.
	- **sono bellissimi, non c'e' nemmeno un po' di rumore**
	- **Normalizzare gli spettri per poterli confrontare**, far vedere dei plot.
	
3. Mostrare gli spettri sperimentali.
	- primi 5 con il bkg.
	- tutti con il bkg
	- primi 5 senza rumore.
	- tutti senza rumore.
	- **occhio al rumore**
	- normalizzazione degi spettri.
	- **alcuni spettri non hanno significato fisico**
	
4. Preprocessing
	- Normalizzazione degli spettri sperimentali.
	- Eliminaizone dell'offset.
	- **Eliminazione dei dati non fisici** Lo facciamo ora o gli teniamo e vediamo se l'algoritmo li trova da se?
	- tolgliere il rumore, abbiamo calcolato il $\sigma$ sulla coda, **ipotesi che il rumore sia lo stesso a tutte le frequenze**
	- eliminazione coda dove non ci sono picchi
	- Rinormalizzazzione, se si toglie la coda le aree non sono piu' normalizzate ad 1.

### Clustering
1. Scelta dell'algoritmo. **DBSCAN/OPTICS**
	- basata sulla riproducibilita' del tutto.
	- trasporre i dati quando si clusterizzano. le features diventano le lunghezze d'onda e non le intensita'.
2. Plot della griglia, vedere (anche solo in modo visivo) se i nostri cluster correlano con la posizione sulla griglia.

### FIT
1. Interpolazione lineare (scegliere $\lambda$ intere).
2. Fit necessita' (?) di creare una funzione che lo faccia come vogliamo noi. **Limitazioni sui coefficienti: in numero e maggiori di zero**.
