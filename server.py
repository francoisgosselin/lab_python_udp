import socket
import hashlib

HOST = "127.0.0.1"
PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serveur UDP sur {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(4096)

        # Séparer nonce+message et hash
        content, recv_hash = data.split(b"\x00", 1)

        nonce = content[:16]
        message = content[16:]

        # Recalculer le hash
        calc = hashlib.sha256(nonce + message).digest()

        if calc == recv_hash:
            s.sendto(b"Message, nonce et hachage valides", addr)
        else:
            s.sendto(b"Erreur de hachage", addr)
