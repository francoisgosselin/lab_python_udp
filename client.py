import socket
from pathlib import Path
import hashlib

HOST = "127.0.0.1"
PORT = 12345

# Lire le message
msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")

# Calculer le hash SHA-256
hash_hex = hashlib.sha256(msg).hexdigest().encode("ascii")

# Message + séparateur + hash
payload = msg + b"\x00" + hash_hex

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(payload, (HOST, PORT))
    data, _ = s.recvfrom(1024)
    print("Réponse du serveur :", data.decode("utf-8", errors="replace"))
