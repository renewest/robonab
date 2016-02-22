import socket
import json

def to_sock01(data):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.1.36', 13372))
	s.send(json.dumps(data))
	result = json.loads(s.recv(1024))
	s.close()
	return result

def to_sock02(data):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.36', 13372))
        s.send(json.dumps(data))
        result = json.loads(s.recv(1024))
        s.close()
	return result

