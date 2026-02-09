import socket
import hashlib

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serveur UDP sur {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(2048)

        message, hash_hex = data.split(b"\x00", 1)
        calc = hashlib.sha256(message).hexdigest().encode("ascii")

        if calc == hash_hex:
            s.sendto(b"Message et hachage valides", addr)
        else:
            s.sendto(b"Erreur de hachage", addr)
