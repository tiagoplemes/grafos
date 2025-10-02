import heapq
import random

def djikstra(matriz, começo):
    vértices = len(matriz)
    valor = [float('inf')] * vértices
    valor[começo] = 0