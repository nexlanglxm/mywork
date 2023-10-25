'''# the with statement will automatically close the file
# when it is finished with it
with open("test-a.txt") as f:
 data = f.read()
 print (data)
# the old way of doing this is
# f = open ("test1.txt")
# data = f.read()
# print(data)'''

'''# when it is finished with it
with open("test-b.txt", "w") as f:
 data = f.write("test b\n") # returns the number of chars written
 print (data)
with open("test-b.txt", "w") as f2: # open file again
 data = f2.write("another line\n")
 print (data)'''

with open("test-d.txt", "w") as f:
 data = f.write("test eddy\n") # returns the number ofchars written
 print (data)
with open("test-d.txt", "a") as f2: # open file again
 data = f2.write("another line part two electric boogaloo\n")
 print (data)