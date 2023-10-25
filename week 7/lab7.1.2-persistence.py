writeNumber = (0)

import os.path
filename = "count.txt"
if not os.path.isfile(filename):
  print("File does not exist")
  writeNumber(0)

def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
 # this file will be created when we write back.
 # no file assumes first time running
 # ie 0 previous runs
        return 0
'''
def readNumber():
 with open(filename) as f:
    number = int(f.read())
    return number
def writeNumber(number):
 with open(filename, "wt") as f:
 # write takes a string so we need to convert
    f.write(str(number))
# main
num = readNumber()
num += 1
print (f"we have run this program {num} times")
writeNumber(num)
'''