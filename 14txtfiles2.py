import os
cwd = os.getcwd()
print(cwd)


camels = 42
print('%d' %camels)

#more than one format sequence.
stringo = 'In %d years, i have spooted %g %s.'
print(stringo %(3, 0.1, 'camels'))

see = open('try.txt', 'w') # create a txt file
line = 'no one is there, this is try text\n'
see.write(line) #write content to the file

see.close() #close the file

print(os.path.exists('try.txt')) #checks whether a file or directory exists

print(os.path.isdir('try.txt'))

print(os.listdir(cwd)) #returns a list of the files in the given directory

# a function that will take a directory and a filename and joins
    # them into a complete path
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

    if os.path.isfile(path):
        print(path)
    else:
        walk(path)


## 14.5 CATCHING EXCEPTIONS
try:
    fin = open('bad_file')
except:
    print('Something went wrong')


## DATABASES
import dbm
db = dbm.open('captions', 'c')
db['cls.png'] = 'Photo of John Legend.'

# keys and items don't work with databases but a for loop can be used
for key in db:
    print(key, db[key])

db.close()


## 14.7 PICKLING

## 14.8

## 14.9 WRITING MODULES
# import files

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print(linecount('dict.py'))

#print(files.linecount('files.py'))