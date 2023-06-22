from pymongo import MongoClient
from tkinter import Tk, simpledialog

# Obtém as informações do banco de dados e coleção do usuário usando uma caixa de diálogo
def obter_informacoes_bd():
    root = Tk()
    root.withdraw()
    banco = simpledialog.askstring("Informações do Banco de Dados", "Digite o nome do banco de dados:")
    colecao = simpledialog.askstring("Informações da Coleção", "Digite o nome da coleção:")
    return banco, colecao

# Conecta-se ao banco de dados e executa a operação de busca (find)
def executar_busca(banco, colecao):
    # Estabelece conexão com o servidor MongoDB
    client = MongoClient()

    # Acessa o banco de dados e a coleção especificados
    db = client[banco]
    collection = db[colecao]

    # Executa a operação de busca (find) na coleção
    resultados = collection.find()

    # Exibe os documentos encontrados
    for documento in resultados:
        print(documento)

# Função principal do script
def main():
    # Obtém as informações do banco de dados e coleção
    banco, colecao = obter_informacoes_bd()

    # Executa a busca
    executar_busca(banco, colecao)

# Executa a função principal
if __name__ == "__main__":
    main()