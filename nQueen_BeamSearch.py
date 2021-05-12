import random, time
from typing import List
from functools import partial


random.seed(80)

State = List[int]
State_Space = List[State]

def generate_State(lenght: int) -> State  :
    return random.sample(list(range(1,lenght+1)),k=lenght)



def generate_State_Space(size: int):
    return [generate_State(size) for _ in range(size)]


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

    #f1 = lenght - len(set(diagonal1))  direct selement
    #f2 = lenght - len(set(diagonal2))  direct selement

    f1 = sum([diagonal1.count(i)*(diagonal1.count(i)-1)//2 for i in set(diagonal1)])
    f2 = sum([diagonal2.count(i)*(diagonal2.count(i)-1)//2 for i in set(diagonal2)])


    value = f1 + f2
    return value

def run(fitness_funct, successor_funct, generate_State_Space_funct, SizeSpace, MaxIteration=200):

    Space = generate_State_Space_funct(SizeSpace)   #generation d'un population

    for i  in range(MaxIteration):                  #vérifier le nombre de l'itération
        Space = sorted(Space,key=lambda state: fitness_funct(state)) 

        
        if fitness_funct(Space[0])==0: break        #Vérifier l'etat but 
        
        Space = Space[:SizeSpace]                   #choisir les meilleur K états
        
        successor = []
        for state in Space:
            successor+=successor_funct(state)       #les successeurs des K états
        Space = successor

    Space = sorted(Space,key=lambda state: fitness_funct(state)) #si on n'a pas trouvé une solution

    return Space[0],i,fitness_funct(Space[0])


SizePuzzle = 50

start = time.time()
state,iteration,value = run(fitness_funct=fitness,
                        successor_funct=successor,
                        generate_State_Space_funct=generate_State_Space,
                        SizeSpace=SizePuzzle,
                        MaxIteration=200)
end = time.time()

print('Etat :',state)
print('Nb d\'itération :',iteration)
print('Evaluation (Nb attaque):',value)
print('Temps :',round(end - start,3),'sec')

