import sys
import socket

target = sys.argv[1]

try:
     
    if (socket.gethostbyname(target)):
        print("The host is live.")

    # will scan ports between 1 to 65,535
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
         
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open\n".format(port))
        else:
            print("Port {} is close\n".format(port))
        s.close()
         
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not live !!!!")
        sys.exit()