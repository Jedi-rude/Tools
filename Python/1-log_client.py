import socket

def send_log_message(message, host='localhost', port=514):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(message.encode('utf-8'))
    client_socket.close()

if __name__ == "__main__":
    send_log_message("This is a test log message.")
