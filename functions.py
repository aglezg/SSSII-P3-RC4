from ctypes import sizeof
from operator import mod
import os

# Limpia la pantalla de la terminal
def cleanTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

# Intercambiar 2 elementos de un vector
def swap(vec: list, pos1: int, pos2: int): 
  if (pos1 < 0 or pos1 >= len(vec)):
     return None
  if (pos2 < 0 or pos2 >= len(vec)):
     return None
  value1 = vec[pos1]
  vec[pos1] = vec[pos2]
  vec[pos2] = value1
  return vec

# Inicialización (Key Scheduling Algorithm, KSA)
def KSA(key: list):
  S: list(int) = []
  for i in range(256):
    S.append(i)
  
  j: int = 0
  for i in range(256):
    j = mod(j + S[i] + key[i % len(key)], 256) 
    S = swap(S, i, j)

  return S

S = KSA([2, 5])
print(S)