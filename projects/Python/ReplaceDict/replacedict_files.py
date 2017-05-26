import re, glob, os



def main():
    colnames = []
    colnames = eval(open('dictionary.txt', 'r').read())
    

    path=os.getcwd()
    print(path)
    for filename in glob.glob(path + '\src\*.sql'):
        sfilename = os.path.basename(filename)
        print(sfilename)

        sfile = open(filename, 'r')        
        ofile = open(path + '\out\\' + sfilename, 'w')

        pattern = re.compile(r'\b(' + '|'.join(colnames.keys()) + r')\b', re.IGNORECASE)
        result = pattern.sub(lambda x: colnames[x.group().upper()], sfile.read())
        
        sfile.close
        ofile.write(result)
        ofile.close

if __name__ == '__main__':
    main()