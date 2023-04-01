from saveDB import save_db

def add_musica(db):
    try:
        nome = input("Digite o nome da música: ").capitalize()
        artista = input("Digite o nome do artista: ").capitalize()
        album = input("Digite o nome do álbum: ").capitalize()
        db["musicas"].append({"nome": nome, "artista": artista, "album": album})
        print("Música adicionada com sucesso!")
        save_db(db)
    except:
        print("\n***** Erro ao adicionar música. *****\n")
