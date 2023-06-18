
### 2 file handling functions in python
    # open -- use for reading, writing and creating files
        # accepts two arguments
        # open(<FILE_NAME> <FILE_LOCATION>, <MODE>)
            # the mode indicate what action is required such as reading, writing or creating
            # also specifies if you want the output in text or binary format.
            # MODE inclde   'r' - open and read (text format)
            #               'rb' - open and read (binary format)
            #               'r+' -open for both reading and writing
            #               'w' -open for writing (overides the existing file)
            #               'a' -open for editing or appending data
    
    # close -- use for closing the openned file connection - no arguments

    # with open('testing.txt', 'r') as file -- opens and after working with file closes
                                                # the file automatically

### OPEN AND READ FILE
file = open('txtFiles/meta_file.txt', mode='r')
data = file.readline()
print(data)

file.close()


with open('txtFiles/myfile.txt', mode='r') as meta_file:
    worla = meta_file.readline()

    print(worla)


### CREATING FILE
try:
    with open('txtFiles/name_file.txt', mode='w') as name_file:
        name_file.write('This are the names of our recent employees.')
        name_file.writelines(['\nJoe Moris', '\nMichael Saen', '\nGeorge Huges', '\nSandra Michel'])
except FileNotFoundError as e:
    print("ERROR", e)



### READING FILE
    # read() -- returns the entire content of the file as a string. can take an integer to specify
        # the number of characters to return.
    # readline() -- returns a single line as a string. Also takes an integer argument to indicate
        # the number of characters to return.
    # readlines() -- reads the entire content of the file and returns it in an ordered list. Alows
        # iteration to pick specific lines.

with open('txtFiles/name_file.txt', 'r') as file:
    print(file.read())



