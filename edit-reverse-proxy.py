import os
import sys



# directory path
os.chdir('/etc/nginx/sites-enabled/')

# initilize line numbers that need to be changed 
lineNum1 = 1
lineNum2 = 2
lineNum3 = 8

# create array to hold lines from file 
edited_file = []

# open file and read into array
with open('edit-reverse-proxy.conf', 'r') as input_file:
   edited_file = input_file.readlines()

listen_port = "listen " + sys.argv[1]  + ";\n"
listen_all_port = "listen [::]:" + sys.argv[2] + ";\n"
proxy_port = "proxy_pass http://127.0.0.1:" + sys.argv[3] + ";\n"

#change lines that need to be changed using array indexing
edited_file[lineNum1] = listen_port
edited_file[lineNum2] = listen_all_port
edited_file[lineNum3] = proxy_port 

# read array lines back into file 
with open('edit-reverse.proxy.conf','w') as input_file: 
    input_file.writelines(edited_file)

input_file.close()

