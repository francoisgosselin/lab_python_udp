print("\n--- Partie 5 : bytes / bytearray ---")

# bytes : immuable
data = b"ABC"
print(data)          # b'ABC'
print(data[0])       # 65
print(chr(data[0]))  # 'A'

# bytearray : modifiable
ba = bytearray(b"ABC")
ba[0] = 66           # 'B'
print(bytes(ba))     # b'BBC'

# slicing
data2 = b"ABCDEFG"
print(data2[0:3])    # b'ABC'
print(data2[3:])     # b'DEFG'
