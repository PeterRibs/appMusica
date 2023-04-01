from addPlaylistFunc import add_playlist
from buscarMusicaFunc import buscar_musica
from buscarPlaylistFunc import buscar_playlist

def usuario(db):
    run = True
    while run:
        print("\n### Menu do usuário ###")
        print("1. Criar playlist")
        print("2. Informações de uma música")
        print("3. Mostrar todas as músicas cadastradas")
        print("4. Mostrar todas as playlists cadastradas")
        print("5. Mostrar todos os artistas cadastrados")
        print("6. Buscar uma playlist")
        print("7. Voltar")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            add_playlist(db)
        elif escolha == "2":
            buscar_musica(db)  
        elif escolha == "3":
            print([i["nome"] for i in db["musicas"]])
        elif escolha == "4":
            print([i["nome"] for i in db["playlists"]])
        elif escolha == "5":
            print(db["artistas"])
        elif escolha == "6":
            buscar_playlist(db)    
        elif escolha == "7":
            print("Voltando para menu inicial!")
            run = False
        else:
            print("\nOpção inválida. Tente novamente.\n")