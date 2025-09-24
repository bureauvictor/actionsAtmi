import os

def main():
  nombre = os.getenv("USERNAME")
  date = os.getenv('Date', '09-10-1990')
  print(f'Hello World {nombre}, from Github. Hola Mundo wey{nombre}. I am learding Github Actions')
  print(f'Today is: {date}')

if __name__ == "__main__":
  main()
