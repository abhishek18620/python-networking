from PyQt5 import QtNetwork,QtCore
import pdb

class SocketThread(QtCore.QThread):

    # signals
    error = QtCore.pyqtSignal(QtNetwork.QTcpSocket.SocketError)
    def __init__(self, id, parent=None):
        super(SocketThread,self).__init__(parent)
        self.socket_descriptor =id
        self.socket = None

    def run(self):
        #thread star ts here
        print(' Thread Started with {0} '.format(self.socket_descriptor))
        self.socket =QtNetwork.QTcpSocket()
        if not self.socket.setSocketDescriptor(self.socket_descriptor):
            #something's wrong we just emit a signal
            self.error.emit(self.socket.error())
            return
        #slot seems to get called directly ,maybe source of error later
        self.socket.readyRead.connect(self.readRead)
        self.socket.disconnected.connect(self.disconnected)

        print('{0} Client connected'.format(self.socket_descriptor))

        # make this thread a loop
        self.exec_()
    @QtCore.pyqtSlot()
    def readRead(self):
        data=self.socket.readAll()
        print(self.socket_descriptor,"Data in : ",data)
        self.socket.write(data)

    @QtCore.pyqtSlot()
    def disconnected(self):
        print(self.socket_descriptor, "Disconnected ")
        self.socket.deleteLater()
        self.exit(0)

class NetworkServer(QtNetwork.QTcpServer):
    def __init__(self,parent=None):
        #standard practise with pyqt
        super(NetworkServer,self).__init__(parent)
        #self.newConnection.connect(self.accept_connection)
        self.listen(port=54545)
        #checking if listening or not
        # print("if listening : {0}".format( self.isListening())

    def incomingConnection(self,socket_descriptor):
        print(socket_descriptor," Connecting ...")
        #needs a bit memory management
        thread = SocketThread(socket_descriptor,self)
        thread.finished.connect(thread.deleteLater)
        thread.start()

    @QtCore.pyqtSlot()
    def start_read(self):
        pass
