import random, time
from typing import List
from functools import partial


random.seed(80)

State = List[int]
State_Space = List[State]

def generate_Stat(lenght: int) -> State  :
    return random.sample(list(range(1,lenght+1)),k=lenght)


def successor(state: State) -> State_Space:
    L = []
    lenght = len(state)
    for i in range(lenght-1):
        for j in range(i+1,lenght):
            s=state.copy()
            s[i],s[j]=s[j],s[i]
            L+=[s]
    return L

def fitness(state :State):  
    lenght = len(state)

    diagonal1 = [state[i] - (i+1) for i in range(lenght)]
    diagonal2 = [state[i] + (i+1) for i in range(lenght)]


    f1 = sum([diagonal1.count(i)*(diagonal1.count(i)-1)//2 for i in set(diagonal1)])
    f2 = sum([diagonal2.count(i)*(diagonal2.count(i)-1)//2 for i in set(diagonal2)])

    value = f1 + f2
    return value

def run(fitness_funct, successor_funct, generate_State_funct, MaxIteration=200):
    current = generate_State_funct()              #l'état initiale 

    for i in range(MaxIteration):           #verification du nombre des itérations

        if  fitness_funct(current) == 0: 
            break                #vérification de l'état but

        successor = successor_funct(current)                  #trouver les successeurs
        successor = sorted(successor,key=lambda state: fitness_funct(state))   #trier par valeur d'evalution

        if fitness_funct(current) < fitness_funct(successor[0]) : #vérifier si le meilleur successeur est moins bon que l'actuelle
            
            break 

        current = successor[0]                #passage état_actuel <= nouveau_état
        
        #current = random.choices(population=successor,weights=[len(current) - fitness_funct(x) + 1 for x in successor],k=1)[0]
    print(current,fitness_funct(current))
    return current,i+1,fitness_funct(current)


sizePuzzle = 50

start = time.time()
state, iteration, value = run(fitness_funct= fitness,
                        successor_funct= successor,
                        generate_State_funct= partial(generate_Stat,lenght=sizePuzzle),
                        MaxIteration=200)
end =  time.time()

print('Etat :',state)
print('Nb d\'itération :',iteration)
print('Evaluation (Nb attaque):',value)
print('Temps :',round(end - start,3),'sec')
