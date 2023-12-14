import socket

def connect_to_server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        data = s.recv(1024)
        print(data.decode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    connect_to_server("192.168.0.247", 4545)
