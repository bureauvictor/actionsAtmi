import os

def main():
  name = os.getenv('USERNAME')
  language = os.getenv('LANGUAGE')
  print(f'Estas corriendo de forma manual este script gracias al workflow. Tu nombre de usuario en github es: {name} y tu lenguaje de programación favorito es: {language}.')

if __name__ == '__main__':
  main()
