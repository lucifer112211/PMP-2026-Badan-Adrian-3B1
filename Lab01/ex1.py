import numpy as np
#      r,a,n
bile = [3,4,2]

def simuleaza_experiment(bile):
    bile=bile.copy()
    zar = np.random.randint(1,7);

    if zar == 6:
        bile[0] = bile[0]+1
    elif zar == 1 or zar ==4:
        bile[1] = bile[1]+1
    else:
        bile[2] = bile[2]+1


    total = sum(bile)

    x = np.random.randint(1,total+1)

    if x<=bile[0]:
        return 0
    elif x<=bile[0]+bile[1]:
        return 1
    else:
        return 2


tries = 600
extrageri = [0,0,0]
for i in range(tries):
    index = simuleaza_experiment(bile)
    extrageri[index] = extrageri[index] +1 

print("Extras bila rosie: " + str(extrageri[0])+"/"+str(tries))
print("Extras bila albastra: " + str(extrageri[1])+"/"+str(tries))
print("Extras bila neagra: " + str(extrageri[2])+"/"+str(tries))




