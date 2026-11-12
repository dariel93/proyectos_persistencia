import pymongo as pm

url="mongodb://localhost:27017"
serv=pm.MongoClient(url)

col_libros=serv.libreria.libros
#col_libros.insert_one({'isbn': 'yu12', 'titulo': 'C++', 'paginas': 520, 'categoria': 'programación', 'precio': 40.7})
col_libros.update_one({"isbn":"1111A"},{"$inc":{"precio":20}})
libros=col_libros.find({"categoria":"programación"})
for lb in libros:
    print(lb)
serv.close()