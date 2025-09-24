import os

def main():
  nombre = os.getenv("USERNAME")
  print(f'Hello World {nombre}, from Github. Hola Mundo wey{nombre}. I am learding Github Actions')

if __name__ == "__main__":
  main()
