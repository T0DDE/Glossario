# Glossario Acronimi

## Indice

- [AFRR](#afrr)
- [AMR](#amr)
- [BRP](#brp)
- [BZB](#bzb)
- [CACM](#cacm)
- [CCM](#ccm)
- [CCR](#ccr)
- [CID](#cid)
- [CMM](#cmm)
- [CNEC](#cnec)
- [CRIDA](#crida)
- [CVA](#cva)
- [CZC](#czc)
- [DACC](#dacc)
- [DQC](#dqc)
- [FAT](#fat)
- [FB](#fb)
- [FCA](#fca)
- [FCR](#fcr)
- [FRM](#frm)
- [FTR](#ftr)
- [GCT](#gct)
- [GLSK](#glsk)
- [GSK](#gsk)
- [IBWT](#ibwt)
- [IDA](#ida)
- [IGM](#igm)
- [IL SIDC SI ARTICOLA IN DUE COMPONENTI PRINCIPALI:](#il-sidc-si-articola-in-due-componenti-principali)
- [IVA](#iva)
- [LT SM](#lt-sm)
- [LTA](#lta)
- [MFRR](#mfrr)
- [NEMO](#nemo)
- [NPF](#npf)
- [NTC](#ntc)
- [PTDF](#ptdf)
- [PTE](#pte)
- [PTR](#ptr)
- [PUN](#pun)
- [RAM](#ram)
- [RCC](#rcc)
- [RR](#rr)
- [RSC](#rsc)
- [SDAC](#sdac)
- [SIDC](#sidc)
- [SOB](#sob)
- [SOGL](#sogl)
- [TERRE](#terre)
- [TSO](#tso)
- [TTF](#ttf)

---

## AFRR
**Significato:** automatic Frequency Restoration Reserves

Nell'ambito delle riserve per il bilanciamento, sono pargonabili alla **riserva secondaria**: si attivano automaticamente dal TSO entro **5** minuti dal verificarsi di uno sbilanciamento in frequenza. Le aFRR aiutano a ripristinare l'equilibrio del sistema dispacciando generazione o carico aggiuntivi, o riducendoli. Si costruisce sulla risposta inizializzata dalla Frequency Containment Reserve (FCR), e continua finché la frequenza non ritorna al valore nominale.

---

## AMR
**Significato:** Adjustment for Minimum RAM

---

## BRP
**Significato:** Balance Responsible Parties

---

## BZB
**Significato:** Bidding Zone Borders

---

## CACM
**Significato:** Capacity Allocation and Congestion Managment

---

## CCM
**Significato:** Capacity Calculation Methodology

Metodologia di calcolo della capacità disponibile tra i Paesi (nel lungo termine, per la LT CCM), che permette di trasformare i vincoli fisici della rete in un valore di capacità che sia sicuro e utilizzabile dal mercato.

---

## CCR
**Significato:** Capacity Calculation Region

Sono definite nell'articolo 2 del regolamento CACM come quelle "aree geografiche in cui viene applicato un calcolo di capacità coordinato". Il CCR definisce quindi il set di Bidding Zone Borders (BZB) tra i quali i compiti di calcolo della capacità sono coordinati dai TSO.

---

## CID
**Significato:** Congestion Income Distribution

---

## CMM
**Significato:** Capacity Management Module

---

## CNEC
**Significato:** Critical Network Elements and Contingenties

Lista di elementi "critici" della rete (e contingenze N-1). Elementi rilevanti della rete per scambi cross-zonali.

---

## CRIDA
**Significato:** Complementary Regional IntraDay Auction

Rappresentano una implementazione anticipata a livello regionale della metodologia europea per l'IntraDay Cross Zonal Capacity Pricing, ai sensi dell'art.55 del CACM.
Le CRIDA permettono di fornire **segnali di prezzo della capacità interzonale** nel timeframe intraday, e di estrarre la **rendita da congestioneéé derivante dall'allocazione della capacità.
Orari delle CRIDA:
- apertura alle 15:00 D-1 (ore negoziabili 0:00-24:00 D) con la capacità residua del mercato del giorno prima;​
- seconda asta alle 22:00 D-1 (ore negoziabili 0:00-24:00 D) con la capacità disponibile in esito al processo di ricalcolo IDCC1;​
- terza asta alle 10:00 D (ore negoziabili 12:00-24:00 D) con la capacità disponibile in esito al processo di ricalcolo IDCC2.
Durante l'esecuzione delle CRIDA, il *continuous trading* viene interrotto.

---

## CVA
**Significato:** Coordinated Validation Adjustment

---

## CZC
**Significato:** Cross Zonal Capacity

---

## DACC
**Significato:** Day Ahead Capacity Calculation

Il processo di calcolo della capacità che si avvia nel D-2 e determina l'NTC per le frontiere: FR-IT, CH-IT, AT-IT, e SI-IT, che verrà utilizzato per il mercato MGP.

---

## DQC
**Significato:** Data Quality Check

---

## FAT
**Significato:** Full Activation Time

Il tempo che trascorre tra la comunicazione degli esiti all'operatore e la piena esecuzione del comando di bilanciamento.

---

## FB
**Significato:** Flow Based

---

## FCA
**Significato:** Forward Capacity Allocation

Il regolamento FCA, che disciplina il mercato a termine dell’energia elettrica. L’FCA copre i timeframe annuale e mensile e stabilisce come i TSO calcolano in anticipo la capacità disponibile tra Paesi e la mettono a disposizione del mercato tramite aste esplicite, utilizzando una piattaforma unica europea.​
L’obiettivo è garantire capacità affidabile e fornire agli operatori strumenti per coprirsi dal rischio nei mercati forward.

---

## FCR
**Significato:** Frequency Containment Reserve

Nell'ambito delle riserve per il bilanciamento, sono pargonabili alla **riserva primaria**: sono la prima linea di difesa quando la frequenza di rete devia dai 50Hz. Quando cala o sale sopra la banda accettabile, chi fornisce FCR risponde automaticamente aumentando o diminuendo l'output di potenza entro **30** secondi, sostenendo tale risposta per almeno **15** minuti.
  L'FCR è un servizio completamente automatizzato e decentralizzato, per cui ogni asset misura indipendentemente la frequenza di rete e reagisce senza alcuna istruzione dal TSO.
  Il mercato FCR opera attraverso un'asta giornaliera, divisa in 6 periodi di 4h per il giorno seguente. Le offerte devono essere simmetriche, che significa che i partecipanti offrono stessa capacità a scendere e a salire. Tutte le offerte acettate vengono chiuse a un *clearing price* uniforme (corrispondente all'offerta accettata a prezzo più alto), per assicurare una compensazione giusta.
nota: FCR paga solo per la *disponibilità di capacità*, non per l'effettivo utilizzo di energia. L'offerta minima è di **1 MW**, con offerte categorizzate in **divisibili** e **non divisibili** (queste ultime con un massimo di **25 MW**).

---

## FRM
**Significato:** Flow Reliability Margin

---

## FTR
**Significato:** Financial Transmission Rights

Un prodotto che da diritti finanziari basati sulla differenza di prezzo (o spread) tra zone. Può essere di due tipi:
- FTR options: Il detentore ha solo il diritto di incassare lo spread positivo. **Non paga nulla se lo spread è negativo**.
- FTR obligations: Il detentore riceve lo spread quando è positivo, ma **deve pagarlo quando è negativo**.

---

## GCT
**Significato:** Gate Closure Time

---

## GLSK
**Significato:** Generation and Load Shift Keys

"Traduce" i cambiamenti in Net Position (NP) in cambiamenti nella generazione/consumo nodali.

---

## GSK
**Significato:** Generation Shift Key

---

## IBWT
**Significato:** Italian Border Working Table

---

## IDA
**Significato:** IntraDay Auctions

Le IDA sono organizzate come aste *implicite* dove gli ordini raccolti vengono accoppiati, e la Cross Zonal Capacity (CZC) viene allocata simultaneamente per diversi Bidding Zone Borders (BZB).
  Le IDA tengono conto di tutti gli ordini validi sottomessi per le rispettive aste, e determinano i *clearing price* per le BZ rilevanti in base agli ordini accoppiati.
  Sono la parte ad asta del Single IntraDay Coupling (SIDC), e completano il mercato SIDC che prima era basato solamente su metodi di trading continuo (come XBID). Sono state implementate in Europa il 13 giugno 2024, al fine di permettere di dare prezzi alla capacità transfrontaliera nel timeframe intragiornaliero.
  Il loro scopo è quello di *armonizzare* il calcolo e l'allocazione delle capacità transfrontaliere per rifletterne la carenza in un dato momento, e quindi mandare un segnale di prezzo adeguato al mercato.
  **Orari**:
- **IDA1**: Gate Closure Time for market parties at D-1 15h. Allocated period D [0h-24h];
- **IDA2**: Gate Closure Time for market parties at D-1 22h. Allocated period D [0h-24h];
- **IDA3**: Gate Closure Time for market parties at D 10h. Allocated period D [12h-24h].

---

## IGM
**Significato:** Individual Grid Model

Riflette lo stato del sistema di trasmissione che ci si aspetta, oltre ai livelli di generazione, carico, e nodali.

---

## IL SIDC SI ARTICOLA IN DUE COMPONENTI PRINCIPALI:
**Significato:** - **XBID Continuous Trading**

Mercato intraday continuo europeo basato sul principio del *first come, first served*.  
  Gli ordini vengono abbinati in tempo reale dal **Continuous Trading Matching Algorithm** del MCO (Market Coupling Operator), nel rispetto della capacità transfrontaliera disponibile (CZC – Cross Zonal Capacity) e degli eventuali vincoli di allocazione (*Allocation Constraints*).  
  Il trading continuo è disponibile dalla **Intraday Gate Opening (IDO)** fino alla **Intraday Gate Closure (IDC)**, generalmente fissata a un’ora prima della consegna dell’energia.  
- **IDA – Intraday Auctions**  
  Aste intraday europee implicite introdotte per integrare il continuous trading e migliorare l’efficienza allocativa del mercato.  
  Le IDA consentono un accoppiamento simultaneo di energia e capacità transfrontaliera attraverso aste pan-europee svolte in specifiche finestre temporali durante la giornata operativa.  
  A differenza del continuous trading, il meccanismo d’asta mira alla massimizzazione del *social welfare*.  
Nel contesto italiano, gli operatori possono sottomettere al SIDC offerte per portafoglio e sono tenuti a nominare entro H-1 le corrispondenti posizioni sulle singole unità.  
Il SIDC rappresenta uno degli strumenti fondamentali dell’integrazione del mercato elettrico europeo, contribuendo alla sicurezza del sistema, alla flessibilità operativa e all’integrazione delle energie rinnovabili.

---

## IVA
**Significato:** Individual Validation Adjustment

---

## LT SM
**Significato:** Long-Term Splitting Methodology

Metodologia che permette di trasformare la capacità calcolata in prodotti commerciali, definendo come suddividere la capacità tra i diversi timeframe, e come strutturare i prodotti da offrire nelle aste. 
Si passa in questo modo dalla rete fisica a un prodotto di mercato, in modo coerente, trasparente e armonizzato a livello europeo.

---

## LTA
**Significato:** Long-term Allocated Capacities

---

## MFRR
**Significato:** manual Frequency Restoration Reserves

Nell'ambito delle riserve per il bilanciamento, sono pargonabili alla **riserva terziaria rotante**: sono utilizzate quando si verificano sbilanciamenti più lunghi o importanti. A differenza della *automatic* FRR, la mFRR è attivata tipicamente manualmente o semi-manualmente dal TSO, ed è designata a supportare o sostituire l'aFRR se lo sbilancio in frequenza persiste. 
La mFRR deve essere completamente attiva entro **12.5 minuti** dal segnale del TSO, e la consegna deve durare almeno **5** minuti.

---

## NEMO
**Significato:** Nominated Electricity Market Operator

Un NEMO è un'entità designata per svolgere compiti relativi a SDAC o SIDC. I NEMO cooperano su base contrattuale.

---

## NPF
**Significato:** Net Position Forecasting

---

## NTC
**Significato:** Net Transfer Capacity

---

## PTDF
**Significato:** Power Transfer Distribution Factor

---

## PTE
**Significato:** Programmazione Territoriale Efficiente

---

## PTR
**Significato:** Physical Transmission Rights

Un prodotto capacità che da diritto di uso fisico della capacità prenotata. Se non nominato, la capacità non utilizzata può essere resa disponibile per il day-ahead, con remunerazione Use It Or Sell It (UIOSI).
Le tipologie di PTR messi all'asta sono:
- Yearly base with reduction periods
- Montly base with reduction periods
- Monthly peak with reduction periods
- Daily base with reduction periods
- Intraday

---

## PUN
**Significato:** Prezzo Unico Nazionale

Si definisce come media dei prezzi di ogni zona ponderata per la percentuale di energia acquistata in ciascuna zona rispetto all'energia totale acquistata.
  Tutte le **offerte di acquisto** vengono valorizzate con il PUN indipendentemente dalla zona, mentre tutte le **offerte di vendita** vengono valorizzate con il prezzo determinato dall'esito del mercato nella singola zona.
Quindi:
- I consumatori non subiscono nessuna penalizzazione;
- I produttori sono incentivati a realizzare nuovi centri di produzione nelle zone ad alto costo (quelle con scarsità di offerta), contribuendo a migliorare la distribuzione dei centri di produzione​.

---

## RAM
**Significato:** Remaining Available Margin

---

## RCC
**Significato:** Regional Coordination Center

Gli RCC sono definiti dalla Electricity Regulation, e sostituiscono i Regional Security Coordinators (RSC) previsti dalla System Operation Guideline.
Gli RCC ricoprono il ruolo dei RSC, oltre a dei compiti di system operation, relativi ai mercati, e alla preparazione ai rischi.
I loro compiti includono:
- supportare la valutazione della coerenza dei piani di difesa e di ripristino dei TSO;
- svolgere il coordinamento regionale della pianificazione delle interruzioni;
- effettuare analisi successive alle operazioni e ai disturbi della rete;
- formare e certificare il personale che lavora per gli RCC.
Nello svolgimento delle loro attività, gli RCC contribuiscono al raggiungimento degli obiettivi per il 2030 e il 2050 stabiliti dai quadri delle politiche climatiche ed energetiche, in particolare per quanto riguarda il rafforzamento della sicurezza dell’approvvigionamento e dell’efficienza, nonché l’aumento dell’elettrificazione del settore energetico.

---

## RR
**Significato:** Replacement Reserves

Nell'ambito delle riserve di bilanciamento, corrispondono grossomodo alla riserva terziaria di sostituzione definita nel Codice di Rete Italiano (CRI).
Il processo RR relativo all'ora **H** si articola nelle seguenti operazioni:
- **Fino ad H-55'**: gli operatori di mercato sottomettono le loro offerte aggiornate per il mercato di bilanciamento;
- **Da H-55' ad H-40'**: i TSO calcolano il loro fabbisogno di energia di bilanciamento da RR, effettuano le analisi di sicurezza, e calcolano gli ATC disponibili.
- **Da H-40' ad H-32'**: la Piattaforma RR processerà le offerte ed i fabbisogni sottomessi dai TSO. La soluzione elaborata terrà conto delle restrizioni imposte dagli ATC tra le diverse zone;
- **Entro H-30'**: la piattaforma RR comunicherà i risultati (offerte accettate, fabbisogni soddisfatti ed ATC residui) ai TSO che a loro volta li comunicheranno agli operatori di mercato.

---

## RSC
**Significato:** Regional Security Coordinator

Gli RSC si sono evoluti in Regional Coordination Centers (RCC) in Europa, migliorando la coordinazione dei TSO.

---

## SDAC
**Significato:** Single Day Ahead Coupling

Un progetto gestito dai NEMO e dai TSO dei paesi europei che vi prendono parte. Si tratta di un mercato in asta a prezzo marginale zonale, che si svolge alle 12 del giorno precedente a quello oggetto di negoziazione.

---

## SIDC
**Significato:** Single IntraDay Coupling

Il SIDC (Single Intraday Coupling) è il meccanismo europeo di integrazione del mercato intraday dell’energia elettrica, gestito congiuntamente dai NEMO (Nominated Electricity Market Operators) e dai TSO (Transmission System Operators) dei paesi partecipanti.

---

## SOB
**Significato:** Shared Order Book

Si tratta del modulo che gestisce gli ordini (le offerte): ciascun ordine è identificato da quantità, prezzo e timestamp. L'order book è visibile agli operatori: gli ordini sono selezionabili in base alla capacità disponibile (non sono visibili gli ordini di altre aree di mercato che fisicamente non possono essere accoppiati) e secondo la **price-time priority**

---

## SOGL
**Significato:** System Operation GuideLines

Secondo i principi delle SOGL i TSDO hanno l'obbligo di dimensionare i propri fabbisogni di riserva.

---

## TERRE
**Significato:** Trans European Replacement Reserves Exchange

Il progetto TERRE nasce per implementare scambi di Replacement Reserves (RR) in linea con l'Electricity Balancing GuideLine (EBGL). TERRE fornisce il *framework tecnico e operativo* e definisce le regole di mercato per governare il funzionamento dei **mercati del bilanciamento**. Delinea le regole di procura della capacità di bilanciamento, di allocazione della capacità di trasmissione per scambi transfrontalieri, per l'attivazione dell'energia di bilanciamento, e per il regolamento finanziario dei Balance Responsible Parties (BRP), i responsabili di bilanciamento.

---

## TSO
**Significato:** Transmission System Operator

Il gestore del sistema di trasmissione (in inglese Transmission System Operator o TSO) è un ente preposto alla trasmissione dell'energia sotto forma di gas naturale o di energia elettrica, usando opportune infrastrutture, a livello nazionale o regionale.

---

## TTF
**Significato:** Technical Task Force

Si tratta di un gruppo di lavoro permanente Italian Border Working Table (IBWT) composto da Terna e i TSO confinanti.

---
