## README.md — Labo Python UDP

Nom : Léa Esso-Solam BIKASSA
Cours : INF26207 – Téléinformatique

Ce laboratoire présente une introduction à la programmation réseau en Python à l’aide des sockets UDP, ainsi qu’aux notions d’encodage, d’intégrité des données et de sécurité.

## Question – Partie 2 
len(s) mesure le nombre de caractères d’une chaîne Unicode (str), tandis que len(b) mesure le nombre d’octets (bytes). En UTF-8, certains caractères comme les accents ou
les emojis sont encodés sur plusieurs octets, ce qui explique que la longueur en bytes soit souvent supérieure à la longueur en caractères.

**ok**

## Question – Partie 3 
Les sockets transmettent des données binaires car les protocoles réseau sont indépendants de l’encodage des caractères. L’utilisation de bytes permet de contrôler explicitement l’encodage (UTF-8, ASCII, etc.) et d’assurer une communication fiable entre systèmes
différents

## Modification de recvfrom(64)
En utilisant la fonction recvfrom(64), le message envoyé contient des caractères UTF-8 (accents, emoji), qui occupent plusieurs octets. Cette taille de buffer est  trop petite et tronque le message ce qui provoque des erreurs sous Windows.
D'ou la modification de la taille du buffer en recvfrom(1024) ou recvfrom(2048), afin de garantir la réception complète du message.

## Question – Partie 4 
hexdigest() est plus pratique pour l’affichage et les échanges textuels, alors que digest() est plus compact pour les traitements binaires.
**digest: encodage représenté par des octets, hexdigest: encodage représenté comme une chaine de caractères hexadécimaux**

## Question – Partie 7 
Un nonce sert à garantir l’unicité d’un message lors d’un échange réseau. Il permet d’empêcher les attaques par rejeu en s’assurant qu’un ancien message capturé ne puisse
pas être réutilisé avec succès, même si le contenu du message est identique.

les parties en commentaire sont fait pour pourvoir tester les autres parties sans problèmess. Penser a les enlever chacune pour lancer chaque question.

```bash
python main.py
```
