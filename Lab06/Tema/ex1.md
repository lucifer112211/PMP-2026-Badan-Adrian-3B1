a. Prin definitie,

$$
\alpha_1(j)=P(O_1=o_1,X_1=j)
$$

Folosind regula produsului:

$$
P(O_1=o_1,X_1=j)
=
P(O_1=o_1\mid X_1=j)P(X_1=j)
$$

Dar:

$$
P(O_1=o_1\mid X_1=j)=b_j(o_1)
$$

si:

$$
P(X_1=j)=\pi_j
$$

Prin urmare:

$$
\boxed{\alpha_1(j)=\pi_jb_j(o_1)}
$$


b. Pentru $t\geq 2$, conditionam dupa starea precedenta $X_{t-1}=i$.

Folosind formula probabilitatii totale:

$$
\alpha_t(j)
=
\sum_i
P(O_1=o_1,\ldots,O_t=o_t,X_{t-1}=i,X_t=j)
$$

Probabilitatea de a ajunge din starea $i$ in starea $j$ este:

$$
P(X_t=j\mid X_{t-1}=i)=a_{ij}
$$

Din proprietatea Markov, aceasta depinde doar de starea precedenta.

De asemenea, observatia curenta $o_t$ depinde doar de starea curenta $j$:

$$
P(O_t=o_t\mid X_t=j)=b_j(o_t)
$$

Pentru fiecare stare precedenta $i$, probabilitatea corespunzatoare este:

$$
\alpha_{t-1}(i)a_{ij}b_j(o_t)
$$

Sumand dupa toate starile precedente posibile, obtinem:

$$
\boxed{
\alpha_t(j)
=
b_j(o_t)
\sum_i\alpha_{t-1}(i)a_{ij}
}
$$


c. La momentul final $T$, sistemul se poate afla in oricare dintre starile $j$.

Prin definitie:

$$
\alpha_T(j)
=
P(O_1=o_1,\ldots,O_T=o_T,X_T=j)
$$

Pentru a obtine probabilitatea intregii secvente observate, sumam dupa toate starile finale posibile:

$$
P(O_1=o_1,\ldots,O_T=o_T)
=
\sum_j
P(O_1=o_1,\ldots,O_T=o_T,X_T=j)
$$

Prin urmare:

$$
\boxed{
P(O_1=o_1,\ldots,O_T=o_T)
=
\sum_j\alpha_T(j)
}
$$