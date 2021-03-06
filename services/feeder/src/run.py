from tiltai.network.nanolink import gate, push, pull
from tiltai.sdn.docker import dockersdn
from tiltai.sdn.filesystem import get_topology as fromfile
from tiltai.sdn.consulregistrator import addr
from tiltai.control.network import routine


from functools import partial

import time
import socket

from logbook import Logger


log = Logger("{host} - {service}".format(host=socket.gethostname(), service="Feeder"))

def feeder():
    plaintext = gate('out', network=dockersdn('plaintext', resolver=addr, storage=fromfile), 
                            governor=partial(routine, resolver=partial(dockersdn, 'plaintext', addr, fromfile)))

    while True:
        log.debug("Sending message")
        push("Plaintext message", plaintext)
        time.sleep(3)

if __name__ == '__main__':
  feeder()
