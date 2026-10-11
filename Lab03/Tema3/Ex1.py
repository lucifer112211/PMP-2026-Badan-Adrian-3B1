import numpy as np

n = 100000

X = np.random.randint(1,7,n)
Y = np.random.randint(1,7,n)

suma = X+Y

def prob_cond(eveniment,conditie):
    return np.sum(eveniment&conditie)/np.sum(conditie)

# 1.
# P(X + Y >= 10 | X par)

p1 = prob_cond(suma>=10,X%2==0)

print("1. Probabilitate simulata:", p1)
print("Probabilitate teoretica:", 2/9)

# 2.
# P(X + Y >= 10 | cel putin un zar este par)

cel_putin_unul_par = (X%2==0) | (Y%2==0)

p2=prob_cond(suma>=10,cel_putin_unul_par)
print("2. Probabilitate simulata:", p2)
print("Probabilitate teoretica:", 5/27)

# 3.
# P(ambele zaruri pare | suma = 8)

ambele_pare = (X%2==0) & (Y%2==0)
p3 = prob_cond(ambele_pare,suma==8)

print("3. Probabilitate simulata:", p3)
print("Probabilitate teoretica:", 3/5)

# 4.
# A = {X + Y >= 10}
# B = {X par}

A = suma>=10
B= X%2==0

pA = np.mean(A)
pB = np.mean(B)

pAB = np.mean(A & B)

print("4.")
print("P(A):", pA)
print("P(B):", pB)
print("P(A intersectat B):", pAB)
print("P(A) * P(B):", pA * pB)
if abs(pAB - pA * pB) < 0.00001:
    print("Evenimentele sunt independente")
else:
    print("Evenimentele nu sunt independente")