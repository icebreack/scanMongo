import pymongo
import sys

def mongo_db_connect(clientIP):
    # Faz a conexão no MongoDB
    try:
        conn=pymongo.MongoClient(clientIP,27017)
	print conn
        conn.server_info()
        print "Conectado!!!!"
        conn.database_names()	
    except pymongo.errors.ConnectionFailure, e:
        print "Não foi possível conectar no MongoDB: %s" % e 

def main(argv):

    fileIP = sys.argv[1]

    # Abre o arquivo
    with open(fileIP, 'r') as infile:
        data = infile.read()  

    # Pega as linhas
    my_list = data.splitlines()

    # scaneia
    for line in my_list:
        print line
        print '----------------------------------------'
	
        try:
            mongo_db_connect(line)
        except:
            print 'Conexao Terminada'

        print '----------------------------------------'


if __name__ == "__main__":
   main(sys.argv[1:])
