#N2
#from pathlib import Path

#p = Path("data/message.txt")

# Lecture en texte (str)
#s = p.read_text(encoding="utf-8")
#print(type(s), len(s))
#print(s)

# Lecture en binaire (bytes)
##b = p.read_bytes()
#print(type(b), len(b))
#print(b[:20])

# Conversions explicites
#b2 = s.encode("utf-8")
#s2 = b.decode("utf-8")

#print(type(b2), len(b2))
#print(type(s2))

#N3
#import socket
#from pathlib import Path

#HOST = "127.0.0.1"
#PORT = 12345

#msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")

#with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    #s.sendto(msg, (HOST, PORT))
    #data, _ = s.recvfrom(1024)
    #print("Réponse du serveur :", data.decode("utf-8", errors="replace"))


#N4
#import socket
#from pathlib import Path
#import hashlib

#HOST = "127.0.0.1"
#PORT = 12345

# Lire le message
#msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")

#  Calcul du hash SHA-256 
#hash_hex = hashlib.sha256(msg).hexdigest().encode("ascii")

# Message + séparateur + hash
#payload = msg + b"\x00" + hash_hex

#with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    #s.sendto(payload, (HOST, PORT))
    #data, _ = s.recvfrom(1024)
    #print("Réponse du serveur :", data.decode("utf-8", errors="replace"))

#N5
 #bytes : immuable
#data = b"ABC"
#print(data)
#print(data[0])        # 65
#print(chr(data[0]))   # 'A'

 #bytearray : modifiable
#ba = bytearray(b"ABC")
#ba[0] = 66            # 'B'
#print(bytes(ba))      # b'BBC'

 #slicing
#data2 = b"ABCDEFG"
#print(data2[0:3])     # b'ABC'
#print(data2[3:])      # b'DEFG'

#n6
#import socket
#from pathlib import Path
#import hashlib

#def flip_first_bit(data: bytes) -> bytes:
    #ba = bytearray(data)
    #ba[0] ^= 0b00000001
    #return bytes(ba)

#HOST = "127.0.0.1"
#PORT = 12345

#Message original
#msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")

 #Hash du message ORIGINAL
#hash_hex = hashlib.sha256(msg).hexdigest().encode("ascii")

# Corruption du message
#corrupted_msg = flip_first_bit(msg)
# Envoi: messaged corrrompu + hash original
#payload = corrupted_msg + b"\x00" + hash_hex

#with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    #s.sendto(payload, (HOST, PORT))
    #data, _ = s.recvfrom(1024)
    #print("Réponse du serveur :", data.decode("utf-8", errors="replace"))

#n7
import socket
from pathlib import Path
import hashlib
import secrets

HOST = "127.0.0.1"
PORT = 12345
NONCE_SIZE = 16
BLOCK_SIZE = 1024

# Lire le message en UTF-8
msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")

# Générer un nonce aléatoire (16 octets)
nonce = secrets.token_bytes(NONCE_SIZE)

# Calculer le hash sur nonce + message
digest = hashlib.sha256(nonce + msg).digest()

# Construire le payload : nonce + message + séparateur + hash
payload = nonce + msg + b"\x00" + digest

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(payload, (HOST, PORT))
    data, _ = s.recvfrom(BLOCK_SIZE)
    print("Réponse du serveur :", data.decode("utf-8", errors="replace"))





