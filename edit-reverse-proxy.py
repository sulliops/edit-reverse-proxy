import os
import sys
import getpass

print "Env thinks the user is [%s]" % (os.getlogin());
print "Effective user is [%s]" % (getpass.getuser());

# Change directory to /etc/nginx/sites-enabled/
os.chdir('/etc/nginx/sites-enabled/')

# Initilize line numbers that need to be changed 
lineNum1 = 1
lineNum2 = 2
lineNum3 = 8

# Create array to hold lines from file 
edited_file = []

# Open file and read into array
with open('edit-reverse-proxy.conf', 'r') as input_file:
   edited_file = input_file.readlines()

# Get command-line arguments as variables
listenOn = sys.argv[1]
listenOn = listenOn[1:len(listenOn)-1]
toProxy = sys.argv[2]
toProxy = toProxy[1:len(toProxy)-1]

# Set lines to existing content with port numbers (argument variables) changed
listen_port = "listen " + listenOn  + ";\n"
listen_all_port = "listen [::]:" + listenOn + ";\n"
proxy_port = "proxy_pass http://127.0.0.1:" + toProxy + ";\n"

# Change lines that need to be changed using array indexing
edited_file[lineNum1] = listen_port
edited_file[lineNum2] = listen_all_port
edited_file[lineNum3] = proxy_port 

# Write array lines back into file 
with open('edit-reverse-proxy.conf','w') as input_file: 
    input_file.writelines(edited_file)

input_file.close()

# Restart nginx
try:
    run(['systemctl', 'restart', 'nginx'], capture_output=True).stdout
except CalledProcessError as e:
    print(e.output)

# Print success
print('Success!')