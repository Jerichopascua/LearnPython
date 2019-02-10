#Mail merger program in Python
#Open rnames.txt for reading the recipient names
with open("rnames.txt",'r',encoding = 'utf-8') as rnames_file:
 #Open msg.txt for reading the message
 with open("msg.txt",'r',encoding = 'utf-8') as msg_file:
 #Store the message in the mail variable
     mail = msg_file.read()
 #Iterate over recipient names in rnames.txt
 for recname in rnames_file:
   rmail = "Dear "+recname+mail
 #Store mails for each recipient as a separate file
   with open(recname.strip()+".txt",'w',encoding = 'utf-8') as rmailfile:
    rmailfile.write(rmail)
