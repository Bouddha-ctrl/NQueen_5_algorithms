
from itertools import permutations 
import time

def fitness(state ):  
    lenght = len(state)

    diagonal1 = [state[i] - (i+1) for i in range(lenght)]
    diagonal2 = [state[i] + (i+1) for i in range(lenght)]


    f1 = sum([diagonal1.count(i)*(diagonal1.count(i)-1)//2 for i in set(diagonal1)])
    f2 = sum([diagonal2.count(i)*(diagonal2.count(i)-1)//2 for i in set(diagonal2)])

    value = f1 + f2
    return value

def run(taille: int):
    state = list(range(1,taille+1))

    space = list(permutations(state))

    for state in space:
        if fitness(state) == 0: break
    return state




puzzleSize = 11
start = time.time()

state = run(taille=puzzleSize)

end = time.time()

print(state)
print(round(end-start,3))