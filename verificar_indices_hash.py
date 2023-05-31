from pymongo import MongoClient

# Conexão com o servidor MongoDB
client = MongoClient('127.0.0.1', 27017)
db = client['sbu']  # Substitua 'nome_do_banco' pelo nome real do seu banco de dados

hashed_indexes = []

# Percorre todas as coleções e índices em busca de índices hash
for coll_name in db.list_collection_names():
    collection = db[coll_name]
    indexes = collection.index_information()

    for index_name, index_info in indexes.items():
        if 'hashed' in index_info.get('key', {}):
            hashed_indexes.append({
                'collection': coll_name,
                'index': index_name
            })

# Exibe os índices hash encontrados
if hashed_indexes:
    print("Índices hash encontrados:")
    for index in hashed_indexes:
        print("Coleção:", index['collection'])
        print("Índice:", index['index'])
        print("-----------------------")
else:
    print("Nenhum índice hash encontrado.")
