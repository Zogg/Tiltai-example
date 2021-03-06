from tiltai.network.nanolink import gate, push, pull
from tiltai.sdn.docker import dockersdn
from tiltai.sdn.filesystem import get_topology as fromfile
from tiltai.sdn.consulregistrator import addr

from logbook import Logger
import socket

log = Logger("{host} - {service}".format(host=socket.gethostname(), service="Email-Sink"))

def emailsink():
    crypted_mails = gate('in', network=dockersdn('crypted_mails', resolver=addr, storage=fromfile))

    while True:
        email = pull(crypted_mails)
        log.info(email)


if __name__ == '__main__':
  emailsink()
