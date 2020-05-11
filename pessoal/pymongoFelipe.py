from pymongo import MongoClient

# Estabelecemos a conexão ao Banco de Dados
conn = MongoClient('localhost', 27017)

# criando e/ou conectando a uma base de dados, que chamarei de dbf e atribuirei a uma variável
db = conn['dbf']

# criando e/ou conectando uma coleção (tabela)
collections = db['produtos']

#inserindo dados
#collections.insert_one({"name": "keyboard", "price": 300}) 

#p1 = {"name": "mouse"}
#p2 = {"name": "monitor"}

#collections.insert_many([p1, p2])

print(db.collection_names())
reg = collections.find()
for r in reg:
    print(r)

reg = collections.find()
for r in reg:
    print(r['name'])

reg = collections.find({"price": 300})
for r in reg:
    print(r)

#collections.delete_many({"price": 300}) #deleta todos os produrtos com preço igual 300
#collections.delete_many({}) #deleta todos os produtos da tabela
