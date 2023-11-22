import random as r
l = [0, 1, 100, 4, 9, 16, 25, 36, 49, 64, 81]   
# Cette fonction mélangera les éléments
r.shuffle(l)

# EXERCICE 001 Permutation
print("\1. Soit a = 1, b = 3 permuter les valeurs de ces deux variables à l'aide script")
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

# EXERCICE 002
print("\nCréez une fonction qui permet de calculer le prix TTC connaissant le prix HT")
def ttc(price, tva):
    return price+price*tva
print(ttc(99,0.1))

# EXERCICE 003
print("\nCréez une fonction qui affiche une table de multiplication dans une liste.")
def table_multiplication(n):
    return [x*n for x in range(1,11)]
print(table_multiplication(9))

# EXERCICE 004
print("\nRegrouper les éléments d'une liste par binomes (trinome pour le dernier groupe si la liste est impaire)")
def liste_binome(l):
    return [l[n:n+3] if(n+3==len(l)) else l[n:n+2] for n in range(0,len(l)-1,2)]

print(liste_binome(list(l)))
# EXERCICE 005
print("\nCréez une fonction qui calcul le max de 2 valeurs, puis trois valeurs. Et facultatif N valeurs.")
def max_n(*numbers):
    max = numbers[0]
    for n in numbers:
        if n>max:
            max = n
    return max

print(max_n(1,2,3))

# EXERCICE 006
print("\nSoit la chaine de caractères suivantes, calculez le nombre de i, puis le nombre de chaque lettre.")
mississippi='Mississippi'
print("nombre de i:",sum(1 if c=='i' else 0 for c in mississippi))
nombre_de_chaque_lettres = {}
for c in mississippi :
    c = c.lower()
    if c not in nombre_de_chaque_lettres.keys():
        nombre_de_chaque_lettres[c] = 1
    else : 
        nombre_de_chaque_lettres[c] += 1
print("nombre de chaque lettres",nombre_de_chaque_lettres)


