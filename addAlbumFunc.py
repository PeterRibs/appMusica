from saveDB import save_db

def add_album(db):
    try:
        nome = input("Digite o nome do álbum: ").capitalize()
        artista = input("Digite o nome do artista: ").capitalize()
        db["albuns"].append({"nome": nome, "artista": artista})
        print("Álbum adicionado com sucesso!")
        save_db(db)
    except:
        print("\n***** Erro ao adicionar álbum. *****\n")
