# -*- coding: utf-8 -*-

"""
Package: iads
Fichier: Classifiers.py
Année: semestre 2 - 2018-2019, Sorbonne Université
"""

# Import de packages externes


import numpy as np
import pandas as pd

# ---------------------------


class Classifier:
    """ Classe pour représenter un classifieur
        Attention: cette classe est une classe abstraite, elle ne peut pas être
        instanciée.
    """

    def __init__(self, input_dimension):
        """ Constructeur de Classifier
            Argument:
                - intput_dimension (int) : dimension d'entrée des exemples
            Hypothèse : input_dimension > 0
        """
        raise NotImplementedError("Please Implement this method")

    def predict(self, x):
        """ rend la prediction sur x (-1 ou +1)
        """
        raise NotImplementedError("Please Implement this method")

    def train(self, labeledSet):
        """ Permet d'entrainer le modele sur l'ensemble donné
        """

        raise NotImplementedError("Please Implement this method")

    def accuracy(self, dataset):
        """ Permet de calculer la qualité du système
        """

        cp = 0
        #res = list(map(lambda x, y: 1 if self.predict(x) == y else 0, dataset.x, dataset.y))
        for x, y in zip(
                dataset.x, dataset.y):  # je recupere des paires [point(i,j),label]
            ypred = self.predict(x)  # je recupere y predit(ŷ) pour ce popint x
            cp += 1 if ypred == y else 0  # je compare la valeur predit a la valeur terrain

        res = cp / len(dataset.x)
        # pour le pourcentage de bonnes predictions
        return res


# ---------------------------
class ClassifierLineaireRandom(Classifier):
    """ Classe pour représenter un classifieur linéaire aléatoire
        Cette classe hérite de la classe Classifier
    """

    def __init__(self, input_dimension):
        """ Constructeur de Classifier
            Argument:
                - intput_dimension (int) : dimension d'entrée des exemples
            Hypothèse : input_dimension > 0
        """
        self.input_dimension = input_dimension
        self.w = 2 * np.random.random(self.input_dimension) - 1
        # on retrourn un vesteur de deux valeurs  random.random(2)) & de
        # valeure entre -1 et 1

    def predict(self, x):
        """ rend la prediction sur x (-1 ou +1)
        """
        transpose = self.w.T  # .T signifie la transposee pour le produit matriciel
        # on retour -1 si le produit de la valeur du point         par le poids
        # <0 sinon 1
        return -1 if np.dot(x, transpose) < 0 else 1

    def train(self, labeledSet):
        """ Permet d'entrainer le modele sur l'ensemble donné
        """
        self.dataset = labeledSet


# ---------------------------
class ClassifierKNN(Classifier):
    """ Classe pour représenter un classifieur par K plus proches voisins.
        Cette classe hérite de la classe Classifier
    """

    def __init__(self, input_dimension, k):
        """ Constructeur de Classifier
            Argument:
                - intput_dimension (int) : dimension d'entrée des exemples
                - k (int) : nombre de voisins à considérer
            Hypothèse : input_dimension > 0
        """
        self.k = k
        self.input_dimension = input_dimension

    def predict(self, x):
        """ rend la prediction sur x (-1 ou +1)
        """
        ind, listDistances = [], []
        ypred = 0
        for i in self.dataset.x:
            # la distance int le point x et tous les autres()
            listDistances.append(np.linalg.norm(i - x))

        # liste trie des distances et renvoie les index
        listDistances = np.argsort(listDistances)
        return -1 if sum(self.dataset.y[listDistances[1:self.k]]) < 0 else 1

    def train(self, labeledSet):
        """ Permet d'entrainer le modele sur l'ensemble donné
        """
        self.dataset = labeledSet


# ---------------------------
class Regressor(Classifier):
    """ Classe réprésentant une régression.

    """

    def __init__(self, dimension_kernel, learning_rate, kernel, max_iter=10):
        """

        :param dimension_kernel:
        :param learning_rate:
        :param kernel:

        """

        self.dimension_kernel = dimension_kernel
        self.learning_rate = learning_rate
        self.kernel = kernel
        self.max_iter = max_iter
        self.w = np.random.random(self.dimension_kernel)
        print(self.w)

    def predict(self, x):
        """ FIXME! briefly describe function

        :param x:
        :returns:
        :rtype:

        """

        return self.kernel.transform(x).dot(self.w.T)

    def train(self, labeledSet):
        """ FIXME! briefly describe function

        :param labeledSet:
        :returns:
        :rtype:

        """
        for _ in range(self.max_iter):
            self.w -= (self.learning_rate *
                       np.mean(2 *
                               (np.dot(self.kernel.transform_set(labeledSet.x), self.w.T) -
                                labeledSet.y)))

# ---------------------------


class NoKernel:
    def transform(self, x):
        """
        """

        return x


class KernelBias:
    def transform(self, x):
        """
        """

        if x.ndim == 1:
            return np.hstack((x, 1))
        elif x.ndim == 2:
            return np.hstack((x, np.ones(x.shape[0])[:, np.newaxis]))
        else:
            raise("Wrong number of dimensions of X")


class KernelPoly:
    def transform(self, x):
        """
        """

        return np.array([1, x[0], x[1], x[0]**2, x[1]**2, x[0] * x[1]])


class KernelPolytwo:
    def transform(self, x):
        """
        """

        return np.hstack((np.ones(x.shape[0])[:, np.newaxis], x, x**2))
