# Activitat: Experimentació amb Neural Networks

## Introducció
En aquesta activitat, explorareu l'impacte de modificar l'arquitectura d'una xarxa neuronal. Específicament, variareu el "learning rate" i la quantitat de capes ocultes i la quantitat de neurones per capa per determinar com això afecta el rendiment del model.

## Objectius
- Comprendre com la modificació de l'arquitectura d'una xarxa neuronal influeix en el seu rendiment.
- Experimentar amb el valor del "learning rate" en una xarxa neuronal.
- Experimentar amb el nombre de capes ocultes i la quantitat de neurones per capa en una xarxa neuronal.
- Analitzar i interpretar els resultats obtinguts després d'ajustar l'arquitectura de la xarxa.


## Context
Ens trobem en un centre de recerca com el Centre de Visió per Computador i us han encomanat a vosaltres i a un equip d'enginyeres i d'enginyers que implementeu una inteligència artificial que sigui capaç de classificar imatges de dígits. És a dir que volen una IA que si li passem una imatge d'un nombre entre el 0 i el 9 ens digui quin nombre és.

Com que sou nous en el departament de recerca us han preparat la IA ja implementada, però us expliquen que les IA tenen molts paràmetres i que s'han d'ajustar de manera diferent per a cada problema...

La vostra tasca és aconseguir trobar quins paràmetres faran que la IA aconsegueixi els resultats més alts possibles, i justificar mitjançant una presentació oral els experiments realitzats i els resultats obtinguts.

## Què hem de fer?

L'activitat consisteix en l'experimentació amb xarxes neuronals per avaluar l'efecte de variar els paràmetres en la seva arquitectura. Aquests experiments s'hauran d'explicar en una petita presentació o pòster. També haureu de respondre el dia de la presentació a una pregunta que heu d'escollir i preparar-vos.

### Part 1: Realització dels experiments

1. **Experiments:**
   - Utilitzant el següent enllaç accediu al classificador d'imatges proporcionat: https://abel-gr.github.io/Docencia/IA/A4/
   - Modifiqueu el learning rate i la quantitat de capes ocultes i neurones per capa de la xarxa i aneu escrivint els valors utilitzats i els resultats obtinguts en un full o document.
   - Exploreu diverses configuracions per tractar d'obtenir *l'accuracy* més alta possible en el conjunt de test.

### Part 2: Preguntes sobre la teoria i de reflexió

1. **Selecció d'una pregunta (per parella):**
   - Entre les preguntes proporcionades, cada parella seleccionarà una per a la seva presentació:

   1. Què és la confusion matrix i què representen els seus valors?
   1. Què és *l'accuracy* i com es calcula? Es pot calcular a partir de la confusion matrix?
   1. Què són els processos de *feedforward* i *backpropagation*?
   1. Què és el learning rate i com afecta al rendiment de la xarxa neuronal que sigui massa petit? I massa gran?
   1. Què és la mètrica del *recall*? Es pot calcular a partir de la confusion matrix?
   1. Què és la separació entre els conjunts de *train* i *test* en el context de la IA i per què és important?
   1. Què és la *object detection* i per a quines tasques s'utilitza? En què es diferencia amb la *semantic segmentation*?
   1. Quines aplicacions té la IA en la medicina? Possa exemples concrets.
   1. Quines aplicacions té la IA en l'educació? Possa exemples concrets.
   1. Què és una xarxa neuronal?
   1. Quins projectes recents que utilitzen IA trobes per Internet i que et criden l'atenció? Com funcionen?
   1. Com funciona ChatGPT?
   1. La IA està regulada per llei? I quines intencions hi ha per regular-la en el futur?
   1. Quines són les limitacions de la IA? És a dir, què li costa fer a una IA o què no és capaç de fer?
   1. La IA necessita molts volums de dades? per què?
   1. Quins són els objectius dels investigadors i de les investigadores per la recerca de la IA en els propers anys?
   1. Quina altra mètrica de rendiment es pot utilitzar juntament amb *l'accuracy* per avaluar el rendiment d'un model?
   1. Quins problemes poden sorgir quan s'augmenta la complexitat d'una xarxa neuronal?
   1. Quines empreses són les més punteres en recerca en IA? Quins projectes han desenvolupat? Quins projectes volen desenvolupar en un futur o hi estan desenvolupant actualment?
   1. Com funciona una xarxa neuronal i com aprèn?

### Part 3: Presentació

1. **Preparar la presentació:**
   - Prepareu una presentació que resumeixi els experiments realitzats i els resultats obtinguts en la primera part així com la resposta a la pregunta de la part dos de l'activitat en un màxim de tres diapositives o un pòster.

1. **Elevator Pitch:**
   - Cada parella farà una presentació de dos minuts (un minut per persona).
   - El dia de la presentació una de les dues persones de la parella haurà d'explicar de manera breu, clara i concisa els experiments realitzats i els resultats obtinguts.
   - L'altra persona de la parella haurà de respondre a la pregunta de la segona part de l'activitat tractant d'explicar-la amb les seves pròpies paraules.


## Rúbrica

| Criteri                         | Assoliment Satisfactori (1 punt)       | Assoliment Notable (2 punts)           | Assoliment Excel·lent (3 punts)                   |
|---------------------------------|-----------------------------------------|---------------------------------------|---------------------------------------------------|
| Temps (Nota individual) | La seva presentació s'ajusta a aproximadament un minut (40-80 segons). | La seva presentació s'ajusta a aproximadament un minut (45-75 segons). | La seva presentació s'ajusta a aproximadament un minut (55-65 segons).  |
| Expressió Oral (Nota individual) | Parla sense llegir.  | Parla sense llegir, s'expressa amb claredat.  | Parla sense llegir, s'expressa amb fluïdesa i claredat. |
| Experiments Realitzats (Nota individual) | Detalla els canvis d'arquitectura i de paràmetres i les seves variacions en les mètriques de rendiment.     | Detalla els canvis d'arquitectura i de paràmetres i les seves variacions en les mètriques de rendiment, demostrant una comprensió de les proves realitzades i dels canvis.  | Aprofundeix en l'anàlisi dels resultats, proporcionant una comprensió substancial dels experiments realitzats i dels seus resultats. Utilitza els resultats per guiar la cerca de paràmetres o per millorar els valors utilitzats o justifica els resultats obtinguts a partir dels paràmetres utilitzats.  |
| Resposta a la pregunta assignada (Nota individual) | Respon a la pregunta assignada amb exemples concrets i precisió. | Respon a la pregunta assignada amb exemples concrets, precisió i comprensió dels temes. | Respon a la pregunta assignada amb exemples concrets, precisió, demostrant una comprensió del tema, proporcionant una resposta completa, coherent i entenedora.  |
| Resultats dels Experiments (Nota grupal) | Realitza els experiments amb precisió i registra els resultats de manera adequada, demostrant una comprensió de les proves realitzades.  | Realitza una quantitat substancial d'experiments, amb precisió en els resultats i l'anàlisi dels canvis, demostrant comprensió dels experiments realitzats.  | Ofereix una visió clara i substancial dels resultats, amb conclusions significatives i un fort coneixement dels experiments. |
| Qualitat del Pòster o Presentació (Nota grupal) | Presenta informació clara i ben estructurada, utilitzant elements visuals per a una millor comprensió.  | Utilitza elements visuals i gràfics per una presentació atractiva i comprensible. Aporta una presentació visual que facilita la comprensió i interpretació dels resultats, utilitzant elements visuals significatius. | Demostra creativitat i originalitat en la presentació, oferint una visió professional. Presenta una visió que reforça visualment les conclusions de manera clara. |