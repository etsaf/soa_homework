import pickle
from xml_marshaller import xml_marshaller
import json
import msgpack
import yaml
from google.protobuf import json_format
from message_dict_pb2 import Dict
import io
import avro.schema
import avro.io
import sys
import timeit



test_dict = {"int": 1001,
             "float": 7.77,
             "string": "String!",
             "array_int": [115, 20897, -33],
             "array_float": [-1.9, 1500.567, 3.5],
             "array_string": ["red", "orange", "yellow"],
             "dict_int": {"one": 115, "two": 20897, "three": -33},
             "dict_float": {"good": -1.9, "okay": 1500.567, "bad": 3.5},
             "dict_string": {"strawberry": "red", "tangerin": "orange", "lemon": "yellow"},
             }

#Pickle

def native_serialize(message_dict):
    packed = pickle.dumps(message_dict)
    return packed

def native_deserialize(message_dict):
    reconstructed = pickle.loads(message_dict)
    return reconstructed

#XML

def xml_serialize(message_dict):
    packed = xml_marshaller.dumps(message_dict)
    return packed

def xml_deserialize(message_dict):
    reconstructed = xml_marshaller.loads(message_dict)
    return reconstructed

#JSON

def json_serialize(message_dict):
    packed = json.dumps(message_dict)
    return packed

def json_deserialize(message_dict):
    reconstructed = json.loads(message_dict)
    return reconstructed

#YAML

def yaml_serialize(message_dict):
    packed = yaml.dump(message_dict)
    return packed

def yaml_deserialize(message_dict):
    reconstructed = yaml.safe_load(message_dict)
    return reconstructed

#MessagePack

def msgpack_serialize(message_dict):
    packed = msgpack.packb(message_dict)
    return packed

def msgpack_deserialize(message_dict):
    reconstructed = msgpack.unpackb(message_dict)
    return reconstructed

#Google Protocol Buffers

def protobuf_serialize(message_dict):
    parsed_message = Dict()
    json_format.ParseDict(message_dict, parsed_message)
    return parsed_message.SerializeToString()

def protobuf_deserialize(message_dict):
    parsed_message = Dict()
    parsed_message.ParseFromString(message_dict)
    reconstructed = json_format.MessageToDict(parsed_message, preserving_proto_field_name=True)
    return reconstructed

#Apache Avro

test_schema = '''
{
"namespace": "example.avro",
 "type": "record",
 "name": "Dict",
 "fields": [
     {"name": "int", "type": "int"},
     {"name": "float", "type": "double"},
     {"name": "string", "type": "string"},
     {"name": "array_int",
     "type": {"type": "array", "items": "int"}},
     {"name": "array_float",
     "type": {"type": "array", "items": "double"}},
     {"name": "array_string",
     "type": {"type": "array", "items": "string"}},
     {"name": "dict_int",
     "type": {"type": "map", "values": "int"}},
     {"name": "dict_float",
     "type": {"type": "map", "values": "double"}},
     {"name": "dict_string",
     "type": {"type": "map", "values": "string"}}
 ]
}
'''
schema = avro.schema.parse(test_schema)

def avro_serialize(message_dict):
    writer = avro.io.DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write(message_dict, encoder)
    raw_bytes = bytes_writer.getvalue()
    return raw_bytes

def avro_deserialize(message_dict):
    bytes_reader = io.BytesIO(message_dict)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(schema)
    reconstructed = reader.read(decoder)
    return reconstructed


serializers = {'native': (native_serialize, native_deserialize),
               'xml': (xml_serialize, xml_deserialize),
               'json': (json_serialize, json_deserialize),
               'protobuf': (protobuf_serialize, protobuf_deserialize),
               'yaml': (yaml_serialize, yaml_deserialize),
               'msgpack': (msgpack_serialize, msgpack_deserialize),
               'avro': (avro_serialize, avro_deserialize)}

def check_correctness(message_dict, serialize, deserialize):
    new_dict = deserialize(serialize(message_dict))
    return new_dict == message_dict

def get_size(message_dict, serialize):
    res = serialize(message_dict)
    return sys.getsizeof(res)

def get_time(message_dict, serialize, deserialize):
    ser_time = timeit.timeit(lambda: serialize(message_dict), number=1000)
    message = serialize(message_dict)
    deser_time = timeit.timeit(lambda: deserialize(message), number=1000)
    return (round(ser_time * 1000, 2), round(deser_time * 1000, 2))

def get_result(format):
#format = sys.argv[1]
    if format not in serializers:
        result = "No such format " + format + '\n'
        return result
    serialize, deserialize = serializers[format]
    if not check_correctness(test_dict, serialize, deserialize):
        result = "Bug in format " + format + '\n'
        return result
    size = get_size(test_dict, serialize)
    time = get_time(test_dict, serialize, deserialize)
    #print(format + " - " + str(size) + " - " + str(time[0]) + "μs - " + str(time[1]) + "μs")
    result = format + " - " + str(size) + " - " + str(time[0]) + "μs - " + str(time[1]) + "μs\n"
    return result
