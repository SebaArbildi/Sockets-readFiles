# Echo server program
import socket
import sys
import json
from TemperatureEntities import Temperature

HOST = '127.0.0.1'               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        aux = json.loads(data)
        auxTemperature = Temperature.Temperature(aux["City"], int(aux["Temperature"]))
        cityInCelsius = Temperature.Temperature.convertFahrenheitToCelsius(auxTemperature)
        conn.send(json.dumps(cityInCelsius.convertToDictionary()).encode('utf-8'))
