import random as r
l = [0, 1, 100, 4, 9, 16, 25, 36, 49, 64, 81]   
# Cette fonction mélangera les éléments
r.shuffle(l)

# EXERCICE 001 Permutation
print("\n1. Soit a = 1, b = 3 permuter les valeurs de ces deux variables à l'aide script")
a=1
b=3
a,b = b,a
print(f"a={a} b={b}")

print("\n2. Refaire la même chose avec les trois variables suivantes a = 1, b = 2, c = 3")
a=1
b=2
c=3
a, b, c = c, a, b
print(f"a={a} b={b} c={c}")

# EXERCICE 002 TVA
print("\nCréez une fonction qui permet de calculer le prix TTC connaissant le prix HT")
def ttc(price, tva):# prend en argument un prix et une valeur de TVA (entre 0 et 1)
    # retourne le prix arrondi à 2 chiffres après la virgule
    return round(number= price + price*tva, ndigits=2)

print(ttc(99.99,0.2))

# EXERCICE 003 Tables de multiplication
print("\nCréez une fonction qui affiche une table de multiplication dans une liste.")
def table_multiplication(n):# prend en argument un nombre n
    table = []              # on crée une table de multiplication vide (list)
    for i in range(1,10+1): # i prendra les valeurs suivantes : [1,2,3,4,5,6,7,8,9,10]
        table.append(n*i)   # on ajoute le multiple à la table
    return table            # on renvoie la table de multiplication complétée

def table_courte(n): #version utilisant une compréhension de liste
    return [x*n for x in range(1,11)]

print(table_multiplication(9))
print(table_courte(9))

# EXERCICE 004 Slicing
print("\nRegrouper les éléments d'une liste par binomes (trinome pour le dernier groupe si la liste est impaire)")
def grouper_par_binome(l):          # prend en argument une liste l
    resultat = []
    for i in range(0,len(l),2):   # i prendra les valeurs suivantes : [0,2,4,...,len(l)-1]
        binome = l[i:i+2]           # binome = [l[i],l[i+1]]
        resultat.append(binome)     # on ajoute le binome a la liste du résultat
    
    if len(l)%2 :   #si la liste a une longueur impaire on aura un résultat du type : [[0,1],[2,3],[4]]
        last = resultat[-1]     # on récupère le dernier élement (qui est solitaire)
        resultat.remove(last)   # on le retire de la liste
        resultat[-1] = resultat[-1]+last #on rajoute le solitaire au dernier groupe pour former un trinome
    
    return resultat

print(grouper_par_binome(list(range(7))))
print(grouper_par_binome(list(range(6))))

# fonction généralisée pour faire des groupes de toutes taille et sur une ligne :
# group_by_d = lambda l,d: [l[i:len(l)] if len(l) -i-d < d else l[i:i+d] for i in range(0,len(l)-d+1,d)]
# print(group_by_d(l,2))

# EXERCICE 005 Max
print("\nCréez une fonction qui calcul le max de 2 valeurs, puis trois valeurs. Et facultatif N valeurs.")
def max2(a,b):  # prend en argument deux nombres a et b
    if a>b:     # si a est plus grand que b
        return a #on renvoie a
    else:       # sinon
        return b #on renvoie b
    
def max3(a,b,c):# prend en argument trois nombres a, b et c
    if a>b and a>c: # si a est le plus grand des trois
        return a # on renvoie a
    elif b>a and b>c: # sinon, si b est le plus grand des trois
        return b # on renvoie b
    else : #sinon (ça veut dire que c est le plus grand)
        return c # on renvoie c

def maxn(*args): # prends un nombre indéfini d'arguments (on les récupère sous forme de liste)
    le_plus_grand = args[0] #on choisis arbitrairement un premier chiffre
    for number in args: #pour chaque nombre dans args
        if number > le_plus_grand: #si le nombre est le plus grand qu'on a déjà vu
            le_plus_grand = number #il prend la place du plus grand nombre
    return le_plus_grand #on renvoie le plus grand nombre

a,b,c,d = 5,7,-89,0
print(max2(a,b))
print(max3(a,b,c))
print(maxn(a,b,c,d))

# EXERCICE 006 Comptez les lettres
print("\nSoit la chaine de caractères suivantes, calculez le nombre de i, puis le nombre de chaque lettre.")
def nombre_de_i(mot): #prend en argument un mot
    return mot.count('i') #renvoie le nombre de i

def nombre_de_chaque_lettres(mot): #prend en argument un mot
    compteur = {}   #on initialise un dictionaire vide
    for letter in mot: #pour chaque lettre du mot
        compteur[letter] = mot.count(letter) #on enregistre le nombre d'occurence de la lettre
    return compteur #on renvoie le nombre

def remplacer_par_e(mot): #prend en argument un mot
    a_remplacer = max(nombre_de_chaque_lettres(mot)) #on récupère la lettre qui reviens le plus souvent
    resultat = '' #on initialise un résultat
    for lettre in mot: #pour chaque lettre du mot
        if lettre == a_remplacer : #si on doit remplacer la lettre
            resultat += 'e' #on la replace
        else: # sinon
            resultat += lettre #on laisse la lettre d'origine
    return resultat #on retourne le resultat

mot='Mississippi'
print("nombre de i:",nombre_de_i(mot))
print("nombre de chaque lettres",nombre_de_chaque_lettres(mot))
print("je remplace une des lettre qui revient le plus par 'e'",remplacer_par_e(mot))