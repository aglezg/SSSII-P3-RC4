import os

# Limpia la pantalla de la terminal
def cleanTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')
