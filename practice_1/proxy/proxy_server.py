import socket

serializers = {'native': 2001,
               'xml': 2002,
               'json': 2003,
               'protobuf': 2004,
               'yaml': 2005,
               'msgpack': 2006,
               'avro': 2007}

HOST = "0.0.0.0"
PORT = 2000
# print("Im proxy")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        message, address = s.recvfrom(1024)
        format = message.decode().strip().split()[-1]
        if message.decode().strip().split()[0] != "get_result":
            s.sendto('No such command\n'.encode(), address)
            continue
        if format not in serializers:
            s.sendto('No such format\n'.encode(), address)
            continue
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as new_s:
            new_s.sendto(format.encode(), (format, serializers[format]))
            result, new_address = new_s.recvfrom(1024)
        s.sendto(result, address)