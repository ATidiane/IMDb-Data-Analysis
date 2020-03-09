# Analyse de données de films

Ce projet porte sur les données travailler sur des données décrivant des films.

Les données de départ sont disponibles sur: https://grouplens.org/datasets/movielens/ au format CSV.

Nous nous intéresserons en particulier au jeu de données: MovieLens 20M Dataset. Dans ce jeu de données, vous disposez entre autre de:

- Idendifiant du film dans IMdb et TMdb (ça sera important ensuite)
- Catégorie(s) du film
- Titre du film
- Notes données par les internautes aux films

Afin de rendre le projet plus intéressant, nous ajoutons des données sur les acteurs et producteurs associés aux films (récupéré sur TMdb). Ces données sont disponibles sur les liens suivants:

http://webia.lip6.fr/~guigue/film_v2.pkl

http://webia.lip6.fr/~guigue/act_v2.pkl

http://webia.lip6.fr/~guigue/crew_v2.pkl

Ces fichiers contiennent respectivement : une nouvelle description des films (dont l'identifiant TMdb et la note moyenne donnée par les internautes, la date de sortie,...), une description des acteurs de chaque film et une description des équipes (scénariste, producteur, metteur en scène) pour chaque film.

Ces données sont des listes de taille 26908, chaque élément de la liste correspondant à un dictionnaire dont vous étudierez les clés pour récupérer les informations utiles.
