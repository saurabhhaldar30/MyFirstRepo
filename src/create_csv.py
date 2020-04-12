import csv
import sys
import getopt

def print_help():
    print('Usage is :- File_Validation.py -i <inputfile> -o <outputfile>')

inputfile = None
outputfile = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "h:i:o:", ["ifile=", "ofile="])

except getopt.GetoptError:
    print_help()
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print_help()
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
        print(inputfile)
    elif opt in ("-o", "--ofile"):
        outputfile = arg
    else:
        print("opt: {} and arg: {}".format(opt, arg))

if not inputfile or not outputfile:
    print_help()
    exit(128)

# Processing files

kwargs = {'newline': ''}
mode = 'r'
try:
    print("InputFile: " + inputfile)
    with open(inputfile, mode, **kwargs) as ipcsvfile:
        reader = csv.reader(ipcsvfile)
        customer_list = list(reader)
except:
    print('Input File Not Found.. Exiting !!!!')
    sys.exit(2)

kwargs = {'newline': ''}
mode = 'w'
with open(outputfile, mode, **kwargs) as opcsvfile:
    writer = csv.writer(opcsvfile)
    for i in customer_list:
        print(i)
        writer.writerow(i)
