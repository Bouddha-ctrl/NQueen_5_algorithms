import time
from pysat.solvers import Minisat22

# Pour le probleme de N dames, les variables représentent un double (i,j) avec i, j dans [0,N].
# Ce double on la signification suivante : la variable (i,j) est vraie ssi
# dans la solution du probléme, la case de coordonnée (i,j) contient une dame.



def run(taille):

    # On définit l comme étant les chiffres dans [0,N]

    l = list(range(0, taille))

    def encode(i,j):
        """La fonction encode prend le double (i,j) de pos en argument et renvoie un nombre qui indique la variable correspondant à ce double.
        """
        return 1 + i + j* taille

    def decode(n):
        """Decode prend en argument prend un nombre entre 1 et N*N*2 qui représente une variable représentant un double (i,j) et renvoie le double correspondant.
        """
        m = n-1
        i = m % taille
        m= m//taille
        j = m % taille

        return (i,j)




    debut = time.time()

    # Instancier la variable phi1 par la contrainte SAT qui indique que
    # chaque ligne contient au moins une valeur

    phi1 = []

    for i in l :
        h=[encode(i,j) for j in l]
        phi1+=[h]

    #print(phi1)

    # Instancier la variable phi2 par la contrainte SAT qui indique
    # qu'une ligne contient au plus une valeur

    phi2 = []

    for i in l :
        for j in l:
            for jj in range(j+1,taille):
                phi2.append([-encode(i,j),-encode(i,jj)])

    #print(phi2)


    # Instancier la variable phi3 par la contrainte SAT qui indique qu'une
    # colonne contient au moins une valeur

    phi3 = []

    for j in l :
        h=[encode(i,j) for i in l]
        phi3+=[h]

    #print(phi3)

    # Instancier la variable phi4 par la contrainte SAT qui indique
    # qu'une colonne contient au plus une valeur

    phi4 = []

    for j in l :
        for i in l:
            for ii in range(i+1,taille):
                phi4.append([-encode(i,j),-encode(ii,j)])

    # print(phi4)

    # Instancier la variable phi5 par la contrainte SAT qui indique que
    # sur une diagonal on a au plus une  valeur

    phi5 = []

    for j in range(taille-2,-1,-1):
        h1 = (0,j)
        h2 = (j,0)
        L1 = [(i,j) for i,j in zip(list(range(h1[0],taille)),list(range(h1[1],taille))) ]
        L1 = [[-encode(L1[I][0],L1[I][1]),-encode(L1[J][0],L1[J][1])] for I in range(len(L1)) for J in range(I+1,len(L1))]
        phi5+=L1

        if h1!=h2:
            L2 = [(i,j) for i,j in zip(list(range(h2[0],taille)),list(range(h2[1],taille))) ]
            L2 = [[-encode(L2[I][0],L2[I][1]),-encode(L2[J][0],L2[J][1])] for I in range(len(L2)) for J in range(I+1,len(L2))]
            phi5+=L2

    #print(phi5)

    # Instancier la variable phi6 par la contrainte SAT qui indique que
    # sur une antidiagonal on a au plus une  valeur

    phi6 = []

    pas = taille-1

    for j in range(1,taille):
        h1 = (0,j)
        h2 = (pas-j,pas)
        
        L1= [ (h1[0]+k,h1[1]-k) for k in range(h1[1]+1)]
        L1 = [[-encode(L1[I][0],L1[I][1]),-encode(L1[J][0],L1[J][1])] for I in range(len(L1)) for J in range(I+1,len(L1))]
        phi6+=L1
        if h1!=h2:
            L2= [ (h2[0]+k,h2[1]-k) for k in range(taille - h2[0])]
            L2 = [[-encode(L2[I][0],L2[I][1]),-encode(L2[J][0],L2[J][1])] for I in range(len(L2)) for J in range(I+1,len(L2))]
            phi6+=L2

    #print(phi6)


    # Cette partie du programme lance le solveur SAT avec la conjonction des contraintes,
    # c'est-à-dire la concaténation des listes les représentant.

    solution =[0]*taille

    with Minisat22(bootstrap_with=phi1+phi2+phi3+phi4+phi5+phi6) as m:
        # si on trouve une solution
        
        if m.solve():
            model = [decode(v) for v in m.get_model() if v >0] 
            
            for item in model:
                solution[item[0]] = item[1]+1
            return solution
            #print("temps d'execution :",time.time()-debut)
        #    print(solution)
        #else :
        #    print("pas de solution")   # dans le cas où N=2 ou N=3
    return 

taille = 100

start = time.time()
state = run(taille)
end = time.time()


def fitness(genome):  #l'evaluation d'un genome/etat
    lenght = len(genome)

    diagonal1 = [genome[i] - (i+1) for i in range(lenght)]
    diagonal2 = [genome[i] + (i+1) for i in range(lenght)]

    f1 = sum([diagonal1.count(i)*(diagonal1.count(i)-1)//2 for i in set(diagonal1)])
    f2 = sum([diagonal2.count(i)*(diagonal2.count(i)-1)//2 for i in set(diagonal2)])

    value = f1 + f2
    return value
print(fitness(state))
print(state)
print(round(end-start,3))