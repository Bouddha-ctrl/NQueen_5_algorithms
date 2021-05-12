import random, time
from typing import List , Tuple
from functools import partial

random.seed(80)


Genome = List[int]
Population = List[Genome]



def generate_genome(lenght: int) -> Genome  :
    return random.sample(list(range(1,lenght+1)),k=lenght)

def generate_population(size :int,lenght : int) -> Population : #size : size of the population , lenght : lenght of the genome
    return [generate_genome(lenght) for _ in range(size)]

def fitness(genome :Genome):  #l'evaluation d'un genome/etat
    lenght = len(genome)

    diagonal1 = [genome[i] - (i+1) for i in range(lenght)]
    diagonal2 = [genome[i] + (i+1) for i in range(lenght)]

    f1 = sum([diagonal1.count(i)*(diagonal1.count(i)-1)//2 for i in set(diagonal1)])
    f2 = sum([diagonal2.count(i)*(diagonal2.count(i)-1)//2 for i in set(diagonal2)])

    value = f1 + f2
    return value

def selection_pair(population :Population,fitness) -> Tuple[Genome,Genome]:  #selection de deux genomes
    length = len(population[0])
    return random.choices(population=population,weights=[length - fitness(genome) + 1  for genome in population],k=2)


def single_point_crossover(genome1 :Genome,genome2 :Genome, prob :float=.9) -> Tuple[Genome,Genome]:

    p = random.randint(1,len(genome1)-2)   #nombre aléatoire entre 2 et N-1
    
    if  random.random() < prob :
        genome1 = genome1[0:p] + [gene for gene in genome2 if gene not in genome1[0:p]]
        genome2 = [gene for gene in genome1 if gene not in genome2[p:]] + genome2[p:]
    
    return genome1, genome2



def mutation(genome : Genome,number_of_mutation : int=1, prob : float=0.2, check_mutation :bool = True) -> Genome:

    for _ in range(number_of_mutation):
        #Deux nombres aleatoire distincts entre 1 et N
        ind1,ind2 = random.sample(list(range(len(genome))),k=2) 

        if  random.random() < prob : #vérifier le seuil
            genome[ind1], genome[ind2] = genome[ind2], genome[ind1] #permutation
            if check_mutation:    #verifier si on est dans la premier mutation
                return mutation(genome,prob=prob*0.5,check_mutation=False) #tenter une deuxieme mutation

    return genome

def run_evolution(fitness_funct, Generat_pop_funct,generation_limit :int=100):
    P = Generat_pop_funct() #generer une population
    
    for i in range(generation_limit):
        P = sorted(P, key=lambda genome: fitness_funct(genome)) 

        if fitness_funct(P[0]) == 0 : #verifier l'etat but
            break

        next_generation = P[0:2]  #elitism

        for j in range(len(P)//2 -1):
            parents = selection_pair(P,fitness_funct) #selection de deux genomes

            g1, g2 = single_point_crossover(parents[0],parents[1]) #croisement
            g1 = mutation(g1) #mutation du genome croisé
            g2 = mutation(g2)
            next_generation += [g1,g2] #ajout à la nouvelle generation

        P = next_generation
        
    P = sorted(P, key=lambda genome: fitness_funct(genome))

    return P[0],i+1,fitness_funct(P[0])


sizeP = 17
sizePuzzle = 20

start = time.time()
genome,generation,h = run_evolution( fitness_funct=fitness,
                                        Generat_pop_funct=partial(generate_population,size=sizeP,lenght=sizePuzzle),
                                        generation_limit=200
                                    )
end = time.time()

print('Etat :',genome)
print('Nb d\'itération :',generation)
print('Evaluation (Nb attaque):',h)
print('Temps :',round(end - start,3),'sec')
