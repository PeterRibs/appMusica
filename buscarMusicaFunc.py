def buscar_musica(db):
    try:
        musica = input("Escolha uma música: ").capitalize()
        result = list(filter(lambda x: musica in list(x.values())[0], db["musicas"]))

        if len(result) == 0:
                print("\nMúsica não possui informação cadastrada.\n")
        else:
                print(result)
    except:
        print("\n***** Erro ao tentar encontrar a música ecolhida. *****\n")