import numpy as np
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from math import comb
n = 10000
win1= 0
win2 = 0

for i in range(n):
    primul = np.random.randint(0,2)

    zar = np.random.randint(1,7)

    alDoilea = 1-primul
    if alDoilea==0:
        p = 0.5
    else:
        p=4/7

    m = np.random.binomial(2*zar,p)
    if zar>=m:
        castigator = primul
    else:
        castigator = alDoilea

    if castigator == 0:
        win1 +=1
    else:
        win2 +=1

print(win1/n)
print(win2/n)

#S - jucatorul care incepe, N valoarea zarului, M numarul de steme din runda 2

#s->m<-n

#p(s,n,m) = p(s)p(n)p(M|S,n)

model = DiscreteBayesianNetwork([
    ("S", "M"),
    ("N", "M")
])

cpd_S = TabularCPD(
    variable="S",
    variable_card=2,
    values=[
        [0.5],
        [0.5]
    ],
    state_names={"S": [0, 1]}
)

cpd_N = TabularCPD(
    variable="N",
    variable_card=6,
    values=[
        [1/6],[1/6],[1/6],[1/6],[1/6],[1/6]
    ],
    state_names={"N": [1, 2, 3, 4, 5, 6]}
)

valori_M = []

for m in range(13):
    linie = []

    for s in [0, 1]:
        for n in range(1, 7):

            if s == 0:
                p = 4 / 7
            else:
                p = 0.5

            if m <= 2 * n:
                probabilitate = (
                    comb(2 * n, m)
                    * p**m
                    * (1 - p)**(2 * n - m)
                )
            else:
                probabilitate = 0

            linie.append(probabilitate)

    valori_M.append(linie)

cpd_M = TabularCPD(
    variable="M",
    variable_card=13,
    values=valori_M,
    evidence=["S", "N"],
    evidence_card=[2, 6],
    state_names={
        "M": list(range(13)),
        "S": [0, 1],
        "N": [1, 2, 3, 4, 5, 6]
    }
)

model.add_cpds(cpd_S, cpd_N, cpd_M)

print(model.check_model())

infer = VariableElimination(model)

rezultat = infer.query(
    variables=["S"],
    evidence={"M": 1}
)

print(rezultat)