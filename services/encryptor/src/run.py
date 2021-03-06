from tiltai.network.nanolink import gate, push, pull
from tiltai.sdn.docker import dockersdn
from tiltai.sdn.filesystem import get_topology as fromfile
from tiltai.sdn.consulregistrator import addr

from logbook import Logger
import socket

import hashlib


log = Logger("{host} - {service}".format(host=socket.gethostname(), service="Encryptor"))

def encryptor():
    plaintext = gate('in', network=dockersdn('plaintext', resolver=addr, storage=fromfile))
    encrypted = gate('out', network=dockersdn('encrypted', resolver=addr, storage=fromfile))

    while True:
        packet = pull(plaintext)
        epacket = hashlib.sha512(packet).hexdigest()
        push(epacket, encrypted)


if __name__ == '__main__':
  encryptor()
