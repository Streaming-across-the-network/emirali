import socket
import config
import time 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((config.server_ip, config.port_nr))
message = "This is a friendly hello message."
while True:
    print("message sent.")
    server_socket.sendto(message.encode(), (config.client_ip, config.port_nr))
    time.sleep(3)
