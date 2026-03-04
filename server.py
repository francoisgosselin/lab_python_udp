#N3
#import socket

#HOST = "127.0.0.1"
#PORT = 12345

#with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    #s.bind((HOST, PORT))
    #print(f"Serveur UDP sur {HOST}:{PORT}")

    #while True:
        #data, addr = s.recvfrom(1024)
        #print(f"Reçu {len(data)} octets de {addr}")
        #s.sendto(b"OK", addr)

#N4
#import socket
#import hashlib

#HOST = "127.0.0.1"
#PORT = 12345

#with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    #s.bind((HOST, PORT))
    #print(f"Serveur UDP sur {HOST}:{PORT}")

    #while True:
        #data, addr = s.recvfrom(2048)

        #message, hash_hex = data.split(b"\x00", 1)
        #calc = hashlib.sha256(message).hexdigest().encode("ascii")

        #if calc == hash_hex:
            #s.sendto(b"Message et hachage valides", addr)
        #else:
            #s.sendto(b"Erreur de hachage", addr)
#N6
#import socket
#import hashlib

#HOST = "127.0.0.1"
#PORT = 12345

#with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    #s.bind((HOST, PORT))
    #print(f"Serveur UDP sur {HOST}:{PORT}")

    #while True:
        #data, addr = s.recvfrom(2048)

        #message, hash_hex = data.split(b"\x00", 1)
        #calc = hashlib.sha256(message).hexdigest().encode("ascii")

        #if calc == hash_hex:
            #s.sendto(b"Message et hachage valides", addr)
        #else:
            #s.sendto(b"Erreur de hachage", addr)



#N7
import socket
import hashlib

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serveur UDP sur {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(4096)
        """
            Pourquoi la valeur de 4096 ici? Éviter les nombres magiques dans le code.
        """

        # Séparer le contenu et le hash
        content, recv_hash = data.split(b"\x00", 1)

        # Extraire le nonce (16 octets) et le message
        nonce = content[:16] # Définir une constante, par exemple NONCE_SIZE = 16
        message = content[16:]

        # Recalculer le hash
        calc = hashlib.sha256(nonce + message).digest()
        """
        nonce + message = content. Pas besoin d'extraire et de recombiner
        """

        if calc == recv_hash:
            s.sendto(b"Message, nonce et hachage valides", addr)
        else:
            s.sendto(b"Erreur de hachage", addr)



















