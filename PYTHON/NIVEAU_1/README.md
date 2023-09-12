Créer un projet CRUD (Create, Read, Update, Delete) en Python. 
Nous allons créer un gestionnaire de tâches simples en ligne de commande. 
Vous pouvez ensuite étendre ce concept en ajoutant une interface utilisateur plus avancée si vous le souhaitez.

# 1. **Structurer le projet :** Créez un dossier pour votre projet. À l'intérieur, créez un fichier principal `app.py`.

2. **Importation de bibliothèques :** Dans `app.py`, importez les bibliothèques nécessaires, telles que `pickle` pour la sérialisation des données.

3. **Créer les fonctions CRUD :**
   - **Create :** Définissez une fonction pour ajouter une nouvelle tâche à la liste.
   - **Read :** Créez une fonction pour afficher toutes les tâches ou pour afficher une tâche spécifique par son identifiant.
   - **Update :** Élaborez une fonction pour modifier une tâche existante.
   - **Delete :** Implémentez une fonction pour supprimer une tâche.

4. **Menu principal :** Créez une boucle dans `app.py` pour afficher un menu et demander à l'utilisateur quelle opération il souhaite effectuer (CRUD).

5. **Gestion des entrées/sorties :** Utilisez `input()` pour recueillir les informations nécessaires auprès de l'utilisateur et `print()` pour afficher les résultats.

6. **Sauvegarde des données :** Utilisez le module `pickle` pour sauvegarder et charger les données dans un fichier. Cela permet de conserver les tâches entre les sessions.

7. **Exécution :** Exécutez `app.py` pour démarrer votre gestionnaire de tâches en ligne de commande.