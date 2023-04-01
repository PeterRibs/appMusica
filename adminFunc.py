from addArtistaFunc import add_artista
from addMusicaFunc import add_musica
from addAlbumFunc import add_album

def admin(db):
    run = True
    while run:
        print("\n### Menu do administrador ###")
        print("1. Adicionar artista")
        print("2. Adicionar música")
        print("3. Adicionar álbum")
        print("4. Voltar")
        escolha = input("Escolha uma opção: ").capitalize()
        if escolha == "1":
            add_artista(db)
        elif escolha == "2":
            add_musica(db)
        elif escolha == "3":
            add_album(db)
        elif escolha == "4":
            print("Voltando para menu inicial!")
            run = False
        else:
            print("\nOpção inválida. Tente novamente.\n")