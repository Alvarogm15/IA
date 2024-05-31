from tictactoeAlum import *


def PSEUDOminimax(nodo):
    mejorJugada = -1
    puntos = -2
    for jugada in jugadas:
        if esValida(nodo, jugada):
            intento = aplicaJugada(nodo, jugada, 1)
            util = utilidad(intento)
            if util > puntos:
                puntos = util
                mejorJugada = jugada
    nodo = aplicaJugada(nodo, mejorJugada, 1)
    return nodo


def jugadaAdversario(nodo):
    valida = False
    jugada = None
    while not valida:
        fila = int(input("Fila: "))
        col = int(input("Col: "))
        jugada = Jugada(fila, col)
        valida = esValida(nodo, jugada)
        if not valida:
            print("\n Intenta otra posicion del tablero \n")
    nodo = aplicaJugada(nodo, jugada, -1)
    return nodo


def minimax(nodo):
    max = -1000
    for jugada in jugadas:
        if esValida(nodo, jugada):
            intento = aplicaJugada(nodo, jugada, 1)
            max_actual = valorMin(intento, opuesto(1))
            if max_actual > max:
                max = max_actual
                mejorJugada = jugada
    nodo = aplicaJugada(nodo, mejorJugada, 1)
    return nodo

import math
def valorMin(nodo, jugador):
    if terminal(nodo):
        valor_min = utilidad(nodo)
    else:
        valor_min = math.inf
        for jugada in jugadas:
            if esValida(nodo, jugada):
                intento = aplicaJugada(nodo, jugada, jugador)
                aux = valorMax(intento, opuesto(jugador))
                valor_min = min(valor_min, aux)
    return valor_min


def valorMax(nodo, jugador):
    if terminal(nodo):
        valor_max = utilidad(nodo)
    else:
        valor_max = -math.inf
        for jugada in jugadas:
            if esValida(nodo, jugada):
                intento = aplicaJugada(nodo, jugada, jugador)
                aux = valorMin(intento, opuesto(jugador))
                valor_max = max(valor_max, aux)
    return valor_max