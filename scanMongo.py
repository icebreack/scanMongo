import pymongo
import sys

def mongo_db_connect(clientIP):
    # Faz a conexão no MongoDB
    try:
        conn=pymongo.MongoClient(clientIP,27017)
        conn.server_info()
        print("+>> Connected!")
    except pymongo.errors.ConnectionFailure as e:
        print("!>> Não foi possível conectar no MongoDB: %s" % e)
        return

    try:
        print("+>> Getting databases names")
        cols = conn.database_names()
        for c in cols:
            print("->> %s" % c)
    except Exception as e:
        print("!>> MongoDB: %s" % e)

def main(argv):

    fileIP = sys.argv[1]

    # Abre o arquivo
    with open(fileIP, 'r') as infile:
        data = infile.read()  

    # Pega as linhas
    my_list = data.splitlines()

    # scaneia
    for line in my_list:
        print(line)
        print('----------------------------------------')
	
        try:
            mongo_db_connect(line)
        except:
            print('Connection Error')

        print('----------------------------------------')


if __name__ == "__main__":
   main(sys.argv[1:])
