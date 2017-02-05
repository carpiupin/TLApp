import socket


class Netcat:

    """ Python 'netcat like' module """

    def __init__(self, ip, port):
        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.socket.connect((ip, port))
        except socket.error, exc:
            print "Netcat - write() socket error: %s" % exc

    def read(self, length=1024):
        """ Read 1024 bytes off the socket """
        try:
            return self.socket.recv(length)
        except socket.error, exc:
            print "Netcat - read() socket error: %s" % exc

    def read_until(self, data):
        """ Read data into the buffer until we have data """

        try:
            while not data in self.buff:
                self.buff += self.socket.recv(1024)

            pos = self.buff.find(data)
            rval = self.buff[:pos + len(data)]
            self.buff = self.buff[pos + len(data):]

            return rval
        except socket.error, exc:
            print "Netcat - read_until() socket error: %s" % exc

    def write(self, data):
        try:
            self.socket.send(data)
        except socket.error, exc:
            print "Netcat - write() socket error: %s" % exc

    def close(self):
        try:
            self.socket.close()
        except socket.error, exc:
            print "Netcat - close() socket error: %s" % exc

    def getHistory(self, target):
        self.write('history ' + target + ' 1' + '\n')
        data = self.read()
        print data
        return data
