import socket
from pathlib import Path
import hashlib
import secrets

HOST = "127.0.0.1"
PORT = 12345

# Lire le message
msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")

# Générer un nonce aléatoire (16 octets)
nonce = secrets.token_bytes(16)

# Calculer le hash sur nonce + message
digest = hashlib.sha256(nonce + msg).digest()

# Payload : nonce + message + séparateur + hash
payload = nonce + msg + b"\x00" + digest

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(payload, (HOST, PORT))
    data, _ = s.recvfrom(1024)
    print("Réponse du serveur :", data.decode("utf-8", errors="replace"))
