import json
import os

from adminFunc import admin
from userFunc import usuario

db_file = "db.txt"

# Verificando se o arquivo do banco de dados já existe
if os.path.exists(db_file):
    try:
        with open(db_file, "r") as f:
            db = json.loads(f.read())
    except:
        print("\n***** Erro ao carregar o banco de dados. Usando base de dados inicial. *****\n")
        
else:
    # Criar, caso não exista
    db = {"musicas": [], "artistas": [], "albuns": [], "playlists": []}

def main(dados):
    run = True
    while run:
        print("\nBem-vindo ao aplicativo de streaming!")
        print("1. Administrador")
        print("2. Usuário")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            admin(dados)
        elif escolha == "2":
            usuario(dados)
        elif escolha == "3":
            print("Obrigado por usar o aplicativo de streaming!")
            run = False
        else:
            print("\nOpção inválida. Tente novamente.\n")

main(db)