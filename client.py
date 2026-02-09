import socket
from pathlib import Path
import hashlib

def flip_first_bit(data: bytes) -> bytes:
    if len(data) == 0:
        return data
    ba = bytearray(data)
    ba[0] ^= 0b00000001  # inverse le bit de poids faible du 1er octet
    return bytes(ba)

HOST = "127.0.0.1"
PORT = 12345

# Lire le message original
msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")

# 1) Calculer le hash du message ORIGINAL
hash_hex = hashlib.sha256(msg).hexdigest().encode("ascii")

# 2) Corrompre le message
corrupted_msg = flip_first_bit(msg)

# 3) Envoyer message corrompu + hash original
payload = corrupted_msg + b"\x00" + hash_hex

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(payload, (HOST, PORT))
    data, _ = s.recvfrom(1024)
    print("Réponse du serveur :", data.decode("utf-8", errors="replace"))
