from saveDB import save_db

def add_artista(db):
    try:
        nome = input("Digite o nome do artista: ").capitalize()
        db["artistas"].append(nome)
        print("Artista adicionado com sucesso!")
        save_db(db)
    except:
        print("\n***** Erro ao adicionar artista. *****\n")
