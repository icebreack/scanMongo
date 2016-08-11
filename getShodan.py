import shodan
import sys
import getopt

# Configuration
API_KEY = ""


def main(argv):
    
    with open('API.txt') as f:
        API_KEY = f.read()
    
    if API_KEY=='':
        print('No API_KEY was found in API.txt file')
        sys.exit(2)
    
    search = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hs:o:",["search=","ofile="])
    except getopt.GetoptError:
        print('getShodan.py -s <search string in between ""> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('getShodan.py -s <search string in between ""> -o <outputfile>')
            sys.exit()
        elif opt in ("-s", "--search"):
            search = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        
    try:
        # Setup the api
        api = shodan.Shodan(API_KEY)
        
        # Perform the search
        result = api.search(search)

        # Loop through the matches and do anything
        for service in result['matches']:
            if outputfile == '':
                print (service['ip_str'])
            else:
                print ('Escrevendo %s' % service['ip_str'])
                target = open(outputfile, 'a')
                target.write(service['ip_str'])
                target.write('\n')
                target.close()        
    except Exception as e:
        print ('Error: %s' % e)
        sys.exit(1)

if __name__ == "__main__":
   main(sys.argv[1:])