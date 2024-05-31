from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
import numpy as np

visual = {1: "❌", -1: "⭕", 0.0: " "}


@dataclass
class Nodo:
    tablero: np.array
    vacias: int
    N: int

    def __init__(self, tablero):
        self.tablero = tablero
        self.N = self.tablero.shape[0]
        self.vacias = len(np.where(tablero == 0)[0])

    def __str__(self):
        string = f"{' ----+----+----'}\n|"
        for i in range(self.tablero.shape[0]):
            for j in range(self.tablero.shape[1]):
                if self.tablero[i, j] == 0:
                    string += "    |"
                else:
                    string += f" {visual[self.tablero[i, j]]} |"
            if i == 2 and j == 2:
                string += f"\n ----+----+----\n"
            else:
                string += f"\n ----+----+----\n|"
        return f"{string}"


@dataclass
class Jugada:
    x: int
    y: int

    def __str__(self):
        return f"\nFila: ({self.x}, Col: {self.y})"


######
# Se crean todas las posibles jugadas para el for de rango (for jugada in jugadas)
jugadas = []
for i in range(0, 3):
    for j in range(0, 3):
        jugadas.append(Jugada(i, j))
######

""" Funciones complementarias
    * crearNodo
    * nodoInicial
    * opuesto
"""


def crearNodo(tablero):
    return Nodo(tablero)


def nodoInicial():
    tablero_inicial = np.zeros((3, 3))
    return Nodo(tablero_inicial)


def opuesto(jugador):
    return jugador * -1


""" Funciones Búsqueda MiniMax
    * aplicaJugada
    * esValida
    * terminal
    * utilidad
"""


def aplicaJugada(actual: Nodo, jugada: Jugada, jugador: int) -> Nodo:
    nuevo = deepcopy(actual)
    i = jugada.x
    j = jugada.y

    nuevo.tablero[i, j] = jugador
    nuevo.vacias -= 1

    return nuevo


def esValida(actual: Nodo, jugada: Jugada) -> bool:
    valida = False
    i = jugada.x
    j = jugada.y

    if jugada.x <= actual.N-1 and jugada.x >= 0 and jugada.y <= actual.N-1 and jugada.y >= 0 and actual.tablero[i, j] == 0:
        valida = True 

    return valida


def terminal(actual: Nodo) -> bool:
    esterminal = False
    a = np.reshape(actual.tablero, 9)
    combinaciones = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for c in combinaciones:
        if (a[c[0]]== a[c[1]] and a[c[1]] == a[c[2]] and a[c[0]] != 0):
            esterminal = True


    return esterminal or actual.vacias == 0


def utilidad(nodo: Nodo) -> int:
    utilidad = 0
    a = np.reshape(nodo.tablero, 9)
    combinaciones = (
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    )

    for c in combinaciones:
        if (a[c[0]]== a[c[1]] and a[c[1]] == a[c[2]]):
            if a[c[0]] == 1:
                utilidad = 100
            if a[c[0]] == -1:
                utilidad = -100     

    return utilidad
