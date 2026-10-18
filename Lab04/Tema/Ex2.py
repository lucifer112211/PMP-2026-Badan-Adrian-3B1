#structura este : B->T, B->X, B->D, T->D

#P(B,T,D,X)=P(B)P(T|B)P(X|B)P(D|B,T)

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ("B","T"),
    ("B","X"),
    ("B","D"),
    ("T","D")
    
])
cpd_b = TabularCPD("B",2,[[0.9],[0.1]])
cpd_t = TabularCPD("T",2,[
    [0.7,0.2],
    [0.3,0.8]],
    ["B"],
    [2]    
)
cpd_x = TabularCPD("X",2,[
    [0.9,0.1],
    [0.1,0.9]],
    ["B"],
    [2]    
)
cpd_d = TabularCPD("D",2,[
    [0.9,0.5,0.6,0.1],
    [0.1,0.5,0.4,0.9]],
    ["B","T"],
    [2,2]    
)

model.add_cpds(cpd_b,cpd_t,cpd_x,cpd_d)
print(model.check_model())

#b. Trebuie sa calculam P(B=1|T=1,D=1)

infer = VariableElimination(model)

rezultat_b = infer.query(["B"],{"T":1,"D":1})
print(rezultat_b)

#c. nu avea boala, deci B= 0 , calculam P(X=1|B=0)
rezultat_c = infer.query(["X"],{"B":0})
print(rezultat_c)