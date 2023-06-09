import sys
import socket
import logging

#set basic logging
logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('172.16.16.101', 45000)
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    # Send data
    message = 'INI ADALAH DATA YANG DIKIRIM\r\n'
    logging.info(f"sending {message}")
    sock.sendall(message.encode('utf-8'))
    # Look for the response
    amount_received = 0
    amount_expected = 5
    while amount_received < amount_expected:
        data = sock.recv(64)
        if len(data) > 0:
            amount_received += len(data)
        else:
            amount_received = amount_expected
        logging.info(f"Received {data}")
        logging.info(f"Decoded message to {data.decode('utf-8')}")
        
        
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
    exit(0)
finally:
    logging.info("closing")
    sock.close()
