# Python : Concepts de base

Ci-dessous sont présentés quelques concepts de base en Python, structurés pour une meilleure compréhension.

## Variables et types de données

- `x = 10` : Affectation de la valeur 10 à la variable x.
- `y = 'Hello World!'` : Affectation de la chaîne de caractères 'Hello World!' à la variable y.
- `type(x)` : Affichage du type de la variable x.
- `type(y)` : Affichage du type de la variable y.
- `int()` : Création d'un objet de type entier.
- `float()` : Création d'un objet de type flottant.
- `str()` : Création d'un objet de type chaîne de caractères.

## Structures de contrôle de flux

- `if` : Permettant de tester une condition.
- `else` : Permettant d'exécuter un bloc de code si la condition testée est fausse.
- `elif` : Permettant de tester une condition supplémentaire.
- `for` : Permettant de parcourir une liste ou une séquence.
- `while` : Permettant d'exécuter une boucle tant qu'une condition est vraie.
- `break` : Permettant de sortir d'une boucle.
- `continue` : Permettant de passer à l'itération suivante d'une boucle.

## Listes et dictionnaires

- `my_list = [1, 2, 3, 4]` : Création d'une liste avec les éléments 1, 2, 3 et 4.
- `my_dict = {'key1': 'value1', 'key2': 'value2'}` : Création d'un dictionnaire avec les clés et les valeurs correspondantes.
- `len(my_list)` : Renvoi de la longueur de la liste my_list.
- `my_list.append(5)` : Ajout de l'élément 5 à la fin de la liste my_list.
- `my_dict.keys()` : Renvoi d'une liste des clés du dictionnaire my_dict.
- `my_dict.values()` : Renvoi d'une liste des valeurs du dictionnaire my_dict.

## Fonctions

- `def my_function(param1, param2):` : Création d'une nouvelle fonction nommée my_function qui prend deux paramètres.
- `return` : Renvoi d'une valeur depuis une fonction.
- `my_function(x, y)` : Appel de la fonction my_function avec les arguments x et y.

## Gestion des erreurs

- `try` : Permettant d'essayer une instruction susceptible de générer une erreur.
- `except` : Permettant de gérer les erreurs éventuellement levées.
- `finally` : Permettant d'exécuter du code après la gestion d'erreur, qu'il y ait eu une erreur ou non.

## Importation de modules

- `import module_name` : Importation d'un module nommé module_name.
- `from module_name import function_name` : Importation d'une fonction spécifique d'un module.
- `import module_name as alias` : Importation d'un module avec un alias.