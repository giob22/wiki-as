---
tipo: entità
categoria: algoritmo
paradigma: "programmazione sul DAG: un passo in avanti e uno all'indietro in ordine topologico"
fonti_pdf: ["14 - Backpropagation.pdf#page=7", "14 - Backpropagation.pdf#page=8", "14 - Backpropagation.pdf#page=9", "14 - Backpropagation.pdf#page=10", "14 - Backpropagation.pdf#page=22", "14 - Backpropagation.pdf#page=23", "14 - Backpropagation.pdf#page=24"]
---

# Backpropagation

## Problema risolto · [[14 - Backpropagation.pdf#page=7|p. 7]]

- **Input:** un [[grafo-computazionale]] (DAG per layer) con una funzione scalare di costo $C$ e i valori degli input.
- **Output:** il valore di $C$ e il **gradiente** $\nabla C$, cioè le derivate $\partial C/\partial z_v$ rispetto a tutti i nodi (in particolare agli input o ai parametri).

Perché serve (p. 7): si supponga una rete con un milione di parametri $w_1, \dots, w_n$ e una funzione scalare di costo $C$, e si voglia $\nabla C = (\partial C/\partial w_1, \partial C/\partial w_2, \dots, \partial C/\partial w_n)$. Calcolare ogni derivata separatamente **può ripetere gran parte dei calcoli**: come riutilizzare le quantità intermedie già disponibili? L'idea è **dividere la computazione in due momenti separati**: un passaggio in avanti per i valori, un passaggio all'indietro per tutte le derivate.

## Idea · [[14 - Backpropagation.pdf#page=8|p. 8]]–[[14 - Backpropagation.pdf#page=10|10]]

**Regola della catena su un grafo** (p. 8). Sia $x$ una variabile interna del grafo e $C$ l'uscita finale. Se $x$ influenza $C$ tramite i successori $y_1, \dots, y_k$, allora

$$
\frac{\partial C}{\partial x} = \sum_{j} \left( \frac{\partial C}{\partial y_j} \cdot \frac{\partial y_j}{\partial x} \right)
$$

Nel grafo $x$ è un nodo e gli $y_j$ sono i suoi successori diretti. Una volta note le derivate $\partial C/\partial y_j$, si può risalire a $\partial C/\partial x$: questo è il principio di base della backpropagation sul grafo.

**Passo forward** (p. 9). Dati i valori iniziali $x_1, \dots, x_n$ nel layer 0, per $\ell = 0, 1, \dots, L$ e per ogni nodo $v$ del layer $\ell$: se $v$ è di input, $value[v]$ è fornito dall'esterno; altrimenti $value[v] = f_v(value[u] \text{ per } u \in pred[v])$. Alla fine si ha il valore di ogni nodo, in particolare di $C$; i $value[v]$ si **memorizzano** per usarli nel passo backward.

**Passo backward** (p. 10). Si pone $\delta_v = 0$ per tutti i nodi $v$ e, per il nodo di uscita, $\delta_C = 1$ (oppure $\delta_C = d\,Costo/dC$ se c'è una funzione di costo esterna). Per $\ell = L, L-1, \dots, 0$ e per ogni nodo $v$ del layer $\ell$, per ogni predecessore $u$ di $v$:

$$
\delta_u \mathrel{+}= \delta_v \cdot \frac{\partial z_v}{\partial z_u}
$$

Al termine, per i nodi di input $x_i$ si ha $\delta_{x_i} = \partial C / \partial x_i$. Nella slide $\delta[v] = \partial C/\partial z_v$.

## Pseudocodice · [[14 - Backpropagation.pdf#page=22|p. 22]]

$Ord$ è un ordine topologico di $G$ ([[ordinamento-topologico]]); $pred[v]$ sono i predecessori di $v$; $value[v]$ è il valore; $\delta[v]$ è la derivata del costo rispetto al valore di $v$. Le righe sono quelle della slide in notazione del corso (la slide usa `for ... in` in stile Python).

```
FORWARD
1  for v in Ord
2      if v è un input
3          then value[v] ← input[v]
4          else args ← [value[u] for u in pred[v]]
5               value[v] ← f_v(args)

BACKWARD
6  for v in V: δ[v] ← 0
7  δ[C] ← 1
8  for v in reverse(Ord)
9      for u in pred[v]
10         dlocal ← ∂f_v/∂z_u
11         δ[u] += δ[v] · dlocal
```

La derivata locale è valutata usando i valori del forward. Per un DAG per layer, $Ord$ può essere semplicemente l'ordine dei layer. I numeri di riga sono miei; nell'animazione la numerazione è diversa (12 righe, perché le intestazioni FORWARD e BACKWARD occupano una riga ciascuna).

![[14-backpropagation-p22-pseudocodice.png]]

## Esempio di esecuzione · [[14 - Backpropagation.pdf#page=11|p. 11]]–[[14 - Backpropagation.pdf#page=21|21]]

![[animazione-backpropagation.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero forward e backward sul grafo di p. 5, $C(a, b) = \tfrac{1}{2}(\sin(ab) + b - 1)^2$ nel punto $(2, 3)$, con gli stessi 5 + 5 passi delle slide: i valori $val$ in blu, gli accumulatori $\delta$ in rosso.

Le slide fanno il forward in 5 passi (pp. 11–15) e il backward in 5 (pp. 16–20), poi controllano il risultato con la regola della catena (p. 21).

![[14-backpropagation-p11-esempio-forward-1.png]]

**Forward** (seno in radianti):

| Passo | Nodo | Valore |
|---|---|---|
| 1 (p. 11) | $a$, $b$ | $value[a] = 2$, $value[b] = 3$ |
| 2 (p. 12) | $c$ | $2 \cdot 3 = 6$ |
| 3 (p. 13) | $d$ | $\sin(6) \approx -0{,}2794$ |
| 4 (p. 14) | $e$ | $\sin(6) + 3 \approx 2{,}7206$ ($b$ è riutilizzato senza ricalcolarlo) |
| 5 (p. 15) | $C$ | $\tfrac{1}{2}(\sin(6) + 2)^2 \approx 1{,}4802$ |

**Backward** ($\delta$ inizialmente 0; i valori restano invariati):

| Passo | Elaborato | Derivata locale | Aggiornamento |
|---|---|---|---|
| 1 (p. 16) | inizializzazione | | $\delta[C] = \partial C/\partial C = 1$ |
| 2 (p. 17) | $C$ (predecessore $e$) | $\partial C/\partial e = e - 1 \approx 1{,}7206$ | $\delta[e] \mathrel{+}= 1 \cdot (e-1) \approx 1{,}7206$ |
| 3 (p. 18) | $e = d + b$ | $\partial e/\partial d = \partial e/\partial b = 1$ | $\delta[d] \approx 1{,}7206$, $\delta[b] \approx 1{,}7206$ (**parziale**: manca il contributo di $c$) |
| 4 (p. 19) | $d = \sin(c)$ | $\partial d/\partial c = \cos(c) = \cos(6) \approx 0{,}9602$ | $\delta[c] \mathrel{+}= \delta[d] \cdot \cos(6) \approx 1{,}6521$ (si usa il valore di $c$ memorizzato) |
| 5 (p. 20) | $c = a \cdot b$ | $\partial c/\partial a = b = 3$, $\partial c/\partial b = a = 2$ | $\delta[a] \approx 4{,}9562$; $\delta[b] \leftarrow 1{,}7206 + 3{,}3041 \approx 5{,}0247$ |

Nota della slide: per $b$ due cammini, due contributi, una somma ($1{,}7206 + 3{,}3041 \approx 5{,}0247$).

![[14-backpropagation-p16-backward-inizializzazione.png]]
![[14-backpropagation-p20-backward-ultimo-passo.png]]

**Verifica con la regola della catena** (p. 21): $\partial C/\partial a = (\sin(ab) + b - 1) \cdot b \cos(ab) \approx 4{,}9562$ e $\partial C/\partial b = (\sin(ab) + b - 1) \cdot (a \cos(ab) + 1) \approx 5{,}0247$, quindi $\nabla C(2, 3) \approx (4{,}9562;\ 5{,}0247)$. I calcoli usano valori non arrotondati.

Tutti i valori sono verificati con [[backpropagation.py]], che calcola anche le derivate con differenze finite ($h = 10^{-6}$) ottenendo le stesse cifre.

## Correttezza · [[14 - Backpropagation.pdf#page=23|p. 23]]

Si ordinano i nodi in ordine topologico $v_1, \dots, v_m$.
- **Forward:** ogni nodo usa solo predecessori già calcolati, quindi è corretto per costruzione.
- **Backward:** usa l'ordine topologico inverso $v_m, \dots, v_1$. **Invariante:** quando si processa $v$, $\delta_v = \partial C/\partial z_v$ è già corretto.
  - *Base:* il nodo di uscita $C$, $\delta_C = \partial C/\partial C = 1$.
  - *Passo induttivo:* si suppongano corrette le $\delta_y$ di tutti i successori $y$ di $x$. Allora $\delta_x = \sum_{y \in succ(x)} \delta_y \cdot \partial z_y/\partial z_x$, che è la regola della catena. Per induzione $\delta_v$ è corretta per ogni nodo $v$.

> 🧩 Perché l'ordine topologico inverso basta: in un DAG tutti i successori di $x$ vengono dopo $x$ nell'ordine topologico, quindi nell'ordine inverso vengono **prima** di $x$. Quando si arriva a $x$, ogni successore $y$ ha già dato il suo contributo $\delta_y \cdot \partial z_y/\partial z_x$ (riga 11, eseguita quando si elaborava $y$): la somma di $\delta_x$ è completa. Per questo nell'esempio $\delta[b]$ è parziale dopo il passo 3 (ha ricevuto da $e$ ma non da $c$) e diventa definitivo solo dopo il passo 5 (quando $c$, che nell'ordine inverso precede $b$, è stato elaborato). Un ordinamento sbagliato farebbe usare $\delta_y$ incomplete.

## Complessità · [[14 - Backpropagation.pdf#page=24|p. 24]]

### Derivazione — $T = O(V + E)$ · [[14 - Backpropagation.pdf#page=24|p. 24]]
**Fonte:** la slide dà il risultato: forward $O(V + E)$, backward $O(V + E)$.
**Si parte da:** il pseudocodice; $V$ e $E$ sono il numero di nodi e di archi del grafo computazionale.

- **Forward:** ogni nodo è valutato una volta (righe 4–5 per ogni $v \in Ord$) e ogni dipendenza è letta una volta (la lista $pred[v]$ ha tante voci quanti sono gli archi entranti in $v$, e $\sum_v \lvert pred[v] \rvert = E$): $O(V) + O(E) = O(V + E)$.
- **Backward:** l'inizializzazione costa $O(V)$; il doppio ciclo (righe 8–11) elabora ogni nodo una volta e ogni arco una volta (per ogni $v$ si scorre $pred[v]$, e il corpo costa $O(1)$): $O(V + E)$.

$$
T = \underbrace{O(V + E)}_{\text{forward}} + \underbrace{O(V)}_{\text{init}} + \underbrace{O(V + E)}_{\text{backward}} = O(V + E)
$$

!! I limiti assumono **costo $O(1)$** per ciascuna operazione elementare e per il contributo di ogni arco; operazioni più complesse vanno contabilizzate separatamente (slide).

**Sanity check** ([[backpropagation.py]]): sul grafo di p. 5 $V = 6$ ed $E = 6$ (archi $a \to c$, $b \to c$, $c \to d$, $d \to e$, $b \to e$, $e \to C$): il forward legge 6 dipendenze e il backward elabora 6 archi. Nella rete di p. 25 (layer da 3, 4, 3 nodi e un nodo di costo, completamente connessa) $V = 11$ ed $E = 3 \cdot 4 + 4 \cdot 3 + 3 \cdot 1 = 27$.
**Ipotesi:** modello RAM; costo costante per operazione elementare e per derivata locale.

> 🧩 Perché è vantaggioso: un solo passaggio all'indietro produce **tutte** le derivate $\partial C/\partial z_v$ in tempo $O(V + E)$; calcolare separatamente $\partial C/\partial w_i$ per un milione di parametri, ripercorrendo ogni volta i cammini fino a $C$, ripeterebbe gran parte dei calcoli (p. 7): qui i risultati intermedi $\delta_v$ sono riutilizzati da tutti i predecessori.

## Dai grafi alle reti neurali · [[14 - Backpropagation.pdf#page=25|p. 25]]–[[14 - Backpropagation.pdf#page=30|30]]

Una **rete neurale feedforward** può essere rappresentata come un DAG di operazioni matematiche (p. 25: input, due layer nascosti di 4 e 3 nodi, un nodo di costo); non serve ancora conoscere il funzionamento dei neuroni: interessa la **struttura delle dipendenze** e l'ordine in cui si possono eseguire i calcoli (p. 25). È un caso particolare di grafo computazionale (p. 26): i **nodi** sono operazioni di somma pesata, funzioni di attivazione ecc.; gli **archi** sono connessioni che trasportano i valori (e le dipendenze). La backpropagation «classica» delle reti neurali è l'algoritmo visto, applicato a un grafo con struttura molto regolare (layer di neuroni): capita la backpropagation su grafi generici, diventa banale capirla e specializzarla alle reti neurali. Nota a mano di p. 26: «è solo una tecnica del calcolo del gradiente sui grafi computazionali».

![[14-backpropagation-p25-rete-neurale.png]]

- **Forward** (p. 27): si parte dagli input e si calcolano i valori dei nodi rispettando le dipendenze; **ordine topologico**: ogni nodo usa soltanto valori già calcolati.
- **Backward** (p. 28): si parte dal costo $C$ e si propagano le derivate verso i predecessori; **ordine topologico inverso**: ogni nodo accumula i contributi di tutti i suoi successori. Nota a mano: «verifico se la predizione è giusta ⇒ in base all'errore commesso … per propagare all'indietro l'errore e … ricavare la derivata» (lettura incerta).

![[14-backpropagation-p28-backward-rete.png]]

**Dai grafi all'apprendimento** (p. 29). Nel Machine Learning la backpropagation **calcola il gradiente del costo rispetto ai parametri**; non modifica, da sola, i parametri della rete. Tre fasi: **Forward** (calcolo del costo $C$) → **Backward** (calcolo di $\nabla C$) → **Ottimizzazione** (aggiornamento dei parametri), con l'esempio di aggiornamento

$$
w_i \leftarrow w_i - \eta \cdot \frac{\partial C}{\partial w_i}
$$

(note a mano: $\eta$ = *learning rate*, valore di scala; $w_i$ i parametri; $\partial C/\partial w_i$ l'errore commesso). Da **ASD**: grafi orientati, DFS, ordinamento topologico, riuso dei risultati intermedi. Da **ML**: scelta del modello, del costo e dell'algoritmo di ottimizzazione. L'ultima slide (p. 30) mostra il primo fotogramma di un'animazione, «1. Forward pass»: l'immagine di un gatto entra nella rete (valori di input 0,20; 0,80; 0,50), un livello nascosto di due nodi e due uscite, «Cane» e «Gatto».

![[14-backpropagation-p29-dai-grafi-all-apprendimento.png]]
![[14-backpropagation-p30-forward-pass-esempio.png]]

## Proprietà

- **Riuso dei risultati intermedi:** i valori del forward e le $\delta$ del backward sono memorizzati e riusati (come una forma di programmazione dinamica sul DAG, 🧩).
- **Dipende dall'ordine topologico:** si valuta in avanti e si propaga all'indietro in ordine topologico (inverso).

## Connessioni

- [[grafo-computazionale]] — la struttura su cui lavora
- [[ordinamento-topologico]] — l'ordine di forward e backward
- [[visita-in-profondita]] — fornisce l'ordine topologico (tempi di completamento)
- [[grafo]] — DAG, predecessori e successori

## Fonti · [[14 - Backpropagation.pdf#page=7|p. 7]]–[[14 - Backpropagation.pdf#page=30|30]]

- [[lezione-14-backpropagation]]

_Aggiornato: 2026-11-26 — ingest 14 - Backpropagation.pdf_

<!-- nav:inizio -->
---
**Lezione 14 · pagina 3 di 3** · ← [[grafo-computazionale|Grafo computazionale]] · [[lezioni|Indice]] · [[lezione-15-backtracking|Lezione 15: introduzione e riepilogo]] →
<!-- nav:fine -->
