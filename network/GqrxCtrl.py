import socket
import sys


class GqrxCtrl():
    # Class to control qgrx via TCP

    def __init__(self, gqrxHostIp):
        self.ip = gqrxHostIp
        self.port = 7356
        self.bufSize = 1024

        # Establish TCP connection to GQRX
        self.qgrxClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.qgrxClient.connect((self.ip, self.port))

    def gqrxTuneFreq(self, freq):
        message = "F " + str(freq)
        self.qgrxClient.send(message)

    def gqrxDemodMode(self, DemodMode):
        message = "M" + DemodMode
        self.qgrxClient.send(message)

    def gqrxClose(self):
        self.gqrxClient.close()
