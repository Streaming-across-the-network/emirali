import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    received_msg, server_addr = client_socket.recvfrom(2048)  # buffer size
    print("Message: ", received_msg.decode(), " received from: ", server_addr)
    time.sleep(3)
    