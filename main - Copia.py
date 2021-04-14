import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

arquivo = open('C:\\Users\\Pichau\\Downloads\\dados.csv', 'r', encoding='UTF-8')
lines = arquivo.readlines()
mycol.delete_many({})

for l in lines:
    coluna = l.split(';')
    mydict = {"Nome": coluna[0].strip(), "Telefone": coluna[1].strip()}
    mycol.insert_one(mydict)



