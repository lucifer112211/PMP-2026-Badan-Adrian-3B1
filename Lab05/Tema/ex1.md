a. Relatia


$A \perp C \mid B$

inseamna ca, daca stim valoarea lui B , atunci informatia despre C nu ne mai ajuta sa aflam ceva in plus despre A.

Adica, folosind independenta conditionata:

$
P(a,c\mid b)=P(a\mid b)P(c\mid b)
$

In graful A-B-C nodul B separa A de C

b. Pornim de la:
$P(a,b,c)=P(a,c\mid b)P(b)$

Din independenta conditionata avem:
$P(a,c\mid b)=P(a\mid b)P(c\mid b)$

Deci:

$P(a,b,c)=P(a\mid b)P(c\mid b)P(b)$

Putem defini:
$\phi_{AB}(a,b)=P(a\mid b)P(b)$ si

$\phi_{BC}(b,c)=P(c\mid b)$

Astfel obtinem:
$P(a,b,c)=\frac{1}{Z}\phi_{AB}(a,b)\phi_{BC}(b,c)$

deci distributia se poate factoriza dupa cele doua clici ale grafului.

c. Presupunem:
$P(a,b,c)=\frac{1}{Z}\phi_{AB}(a,b)\phi_{BC}(b,c)$

Vrem sa aratam :
$A\perp C\mid B$


Calculam:
$P(a,c\mid b)=\frac{P(a,b,c)}{P(b)}$

Mai intai:
$P(b)=\sum_a\sum_c P(a,b,c)$

Inlocuind factorizarea:

$P(b)=
\frac{1}{Z}
\left(\sum_a\phi_{AB}(a,b)\right)
\left(\sum_c\phi_{BC}(b,c)\right)$


Atunci:

$
P(a,c\mid b)=
\frac{\phi_{AB}(a,b)}
{\sum_{a'}\phi_{AB}(a',b)}
\cdot
\frac{\phi_{BC}(b,c)}
{\sum_{c'}\phi_{BC}(b,c')}
$

Primul termen este $P(a\mid b)$, iar al doilea este $P(c\mid b)$.

Deci:


$P(a,c\mid b)=P(a\mid b)P(c\mid b)$,
De unde rezulta independenta cautata