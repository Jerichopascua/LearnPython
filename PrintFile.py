#prompt the user to enter the file name
fn = input("Enter the File Name : ")
#The function is open using the open() in the read mode
#with open(fn,'r') as y:
x=open(fn)
#A for loop is used to read each line of the file in the file
#Each line in the file is converted to upper case using upper()
#for x in y:
for y in x:
     z = y.upper()
     print(z)
x.close()


