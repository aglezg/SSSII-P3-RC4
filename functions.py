from operator import mod
import os

# Limpia la pantalla de la terminal
def cleanTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

# Inicialización (Key Scheduling Algorithm, KSA)
def KSA(key):
  S: int = []
  for i in range(256):
    S[i] = i
  
  j: int = 0
  for i in range(255):
    j: int = mod(j + S[i] + key[i], 256) 
    # realizar swap
  return S

KSA('a')