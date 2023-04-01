from saveDB import save_db

def add_playlist(db):
    try:
        nome = input("Digite o nome da playlist: ").capitalize()
        playlist = {"nome": nome, "musicas": []}
        while True:
            listaMusicas = [i["nome"] for i in db["musicas"]]
            print(f"\nMúsicas cadastradas:\n{listaMusicas}\n")
            musica = input("Digite o nome da música a ser adicionada (ou 'sair' para finalizar): ")
            if musica.lower() == "sair":
                break
            else:
                for m in db["musicas"]:
                    if m["nome"] == musica:
                        playlist["musicas"].append(m["nome"])
                        print("\n***** Música adicionada com sucesso! *****\n")
                        break
                else:
                    print(f"\n***** Música '{musica}' não encontrada. *****\n")
        db["playlists"].append(playlist)
        print("Playlist adicionada com sucesso!")
        save_db(db)
    except:
        print("\n***** Erro ao adicionar playlist. *****\n")
