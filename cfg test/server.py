import socket

def start_server(cfg):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", cfg["port"]))
    server.listen(1)
    print(f"Server listening on {cfg['address']}:{cfg['port']}")

    while True:
        client, address = server.accept()
        print(f"Accepted connection from {address}")
        client.sendall(b"Hello, you've connected to the server!")
        client.close()

if __name__ == "__main__":
    cfg = {
        "address": "192.168.0.62",
        "port": 4545,
        "scope": "site",
        "ttl": 1,
        "interface": "en0",
        "enable_ipv6": False,
    }
    start_server(cfg)
