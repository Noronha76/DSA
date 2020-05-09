#imports
from pymongo import MongoClient
import datetime

# Estabelecemos a conexão ao Banco de Dados
conn = MongoClient('localhost', 27017)
print(type(conn))

# Uma única instância do MongoDB pode suportar diversos bancos de dados. 
# Vamos criar o banco de dados cadastrodb
db = conn.cadastrodb
print(type(db))

# Uma coleção é um grupo de documentos armazenados no MongoDB 
# (relativamente parecido com o conceito de tabelas em bancos relacionais)
collection = db.cadastrodb
print(type(collection))

# Dados no MongoDB são representados (e armazenados) usando documentos JSON (Java Script Object Notation). Com o PyMongo usamos dicionários para representar documentos.
post1 = {"codigo": "ID-9987725",
        "prod_name": "Geladeira",
        "marcas": ["brastemp", "consul", "elecrolux"],
        "data_cadastro": datetime.datetime.utcnow()}
print(type(post1))

collection = db.posts
post_id = collection.insert_one(post1)
post_id.inserted_id
# Quando um documento é inserido uma chave especial, "_id", é adicionada 
# automaticamente se o documento ainda não contém uma chave "_id".
print(post_id)

post2 = {"codigo": "ID-2209876",
        "prod_name": "Televisor",
        "marcas": ["samsung", "panasonic", "lg"],
        "data_cadastro": datetime.datetime.utcnow()}

print('L39')

collection = db.posts
post_id = collection.insert_one(post2).inserted_id
print(post_id)

collection.find_one({"prod_name": "Televisor"})
print('L46')

# A função find() retorna um cursor e podemos então navegar pelos dados
for post in collection.find():
    print(post)
print('L51')

# Verificando o nome do banco de dados
print(db.name)
# Listando as coleções disponíveis
print(db.collection_names())

#####################################
# Retornando Dados no MongoDB com PyMongo
#####################################
print('Retornando Dados no MongoDB com PyMongo')

import pymongo

# Criando a conexão com o MongoDB (neste caso, conexão padrão)
client_con = pymongo.MongoClient()

# Listando os bancos de dados disponíveis
print(client_con.database_names())
