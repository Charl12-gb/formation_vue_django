# **Boucles :**
# **Loops :**

# Boucle for pour afficher les nombres de 1 à 5
# For loop to display numbers from 1 to 5
for i in range(1, 6):
    print(i)

# ---------------------------------------------------------------------------------

# Boucle while pour calculer la somme des nombres de 1 à 10
# While loop to calculate the sum of numbers from 1 to 10
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(total)

# ---------------------------------------------------------------------------------

# **Instructions conditionnelles :**
# **Conditional instructions :**

# Vérification si un nombre est pair ou impair => Checking whether a number is odd or even
num = 7
if num % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")

# ---------------------------------------------------------------------------------

# **Fonctions :** => Functions

# Définition d'une fonction pour calculer le carré d'un nombre
def carre(nombre):
    return nombre ** 2

resultat = carre(5)
print(resultat)

# ---------------------------------------------------------------------------------

# **Listes :**

# Création d'une liste d'éléments
fruits = ["pomme", "banane", "orange"]

# Accès aux éléments de la liste
print(fruits[0])  # Affiche "pomme"

# Ajout d'un élément à la liste
fruits.append("fraise")
print(fruits)

# ---------------------------------------------------------------------------------

# Création d'un tuple
coordonnees = (3, 5)

# Accès aux éléments du tuple
x = coordonnees[0]
y = coordonnees[1]
print("Coordonnées x :", x)
print("Coordonnées y :", y)

# ---------------------------------------------------------------------------------

# Création d'un dictionnaire
etudiant = {
    "nom": "Alice",
    "age": 21,
    "matiere_preferee": "Mathématiques"
}

# Accès aux valeurs à l'aide des clés
nom_etudiant = etudiant["nom"]
age_etudiant = etudiant["age"]
print("Nom de l'étudiant :", nom_etudiant)
print("Âge de l'étudiant :", age_etudiant)

# Modification de la valeur associée à une clé
etudiant["age"] = 22

# Ajout d'une nouvelle paire clé-valeur
etudiant["ville"] = "Paris"

# Parcours des clés et des valeurs du dictionnaire
for cle, valeur in etudiant.items():
    print(f"{cle}: {valeur}")

# ---------------------------------------------------------------------------------

# **Tableaux (à l'aide de la bibliothèque NumPy) :**

import numpy as np

# Création d'un tableau NumPy
tableau = np.array([1, 2, 3, 4, 5])

# Opérations sur le tableau
double_tableau = tableau * 2
print(double_tableau)

# Ces exemples vous montrent comment utiliser les boucles, les instructions conditionnelles, les fonctions, les listes et les tableaux en Python.