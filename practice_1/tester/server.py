from serialize import get_result
import socket
import sys

init_format = sys.argv[1]
# print("Im", init_format)

serializers = {'native': 2001,
               'xml': 2002,
               'json': 2003,
               'protobuf': 2004,
               'yaml': 2005,
               'msgpack': 2006,
               'avro': 2007}

HOST = "0.0.0.0"
PORT = serializers[init_format]

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        message, address = s.recvfrom(1024)
        format = message.decode().strip()
        if format != init_format:
            s.sendto('Wrong server\n'.encode(), address)
            continue
        result = get_result(format)
        s.sendto(result.encode(), address)