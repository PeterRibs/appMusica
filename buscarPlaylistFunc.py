from buscarPlaylistArtistaFunc import playlists_por_artista

def buscar_playlist(db):
    run = True
    while run:
        print("\n### Menu de busca de playlist ###")
        print("1. Por música")
        print("2. Por playlist")
        print("3. Por artista")
        print("4. Voltar")
        try:
            buscaPor = input("Ecolha a categoria da busca: ").capitalize()
            if buscaPor == "1":
                nome = input("Digite a musica que quer buscar: ").capitalize()
                result = list(filter(lambda x: nome in x["musicas"], db["playlists"]))
            elif buscaPor == "2":
                nome = input("Digite a playlist que quer buscar: ").capitalize()
                result = list(filter(lambda x: nome in x["nome"], db["playlists"]))
            elif buscaPor  == "3":
                artista = input("Digite o(a) artista que quer buscar: ").capitalize()
                result = playlists_por_artista(artista, db)
            elif buscaPor  == "4":
                print("Voltando para menu inicial!")
                run = False
            else:
                print("\nOpção inválida. Tente novamente.\n")

            print("\nResultado da busca:")

            if len(result) == 0:
                print("\nNenhuma das playlists cadastradas possui essa música.\n")
            else:
                print(result)
        except:
            print("\n***** Erro ao tentar encontrar a playlist ecolhida. *****\n")


