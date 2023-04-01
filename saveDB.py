import json

# Função de salvar banco de dados
def save_db(db):
    try:
        with open("db.txt", "w") as f:
            f.write(json.dumps(db))
        print("Banco de dados salvo com sucesso!")
    except:
        print("\n***** Erro ao salvar banco de dados. *****\n")