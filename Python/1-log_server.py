import socket

def start_log_server(host='0.0.0.0', port=514):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Log server started on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        with client_socket:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                log_message = data.decode('utf-8')
                print(f"Received log: {log_message}")
                # Optionally, save the log message to a file or database
                with open('logs.txt', 'a') as f:
                    f.write(log_message + '\n')

if __name__ == "__main__":
    start_log_server()
