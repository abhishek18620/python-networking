import sys
from PyQt5 import QtWidgets,QtNetwork,QtCore
from main_window import MainWindow
from network_server import NetworkServer
app=QtWidgets.QApplication(sys.argv)

# qwindow
main_window = MainWindow()
main_window.show()

network_server=NetworkServer()
test_socket =QtNetwork.QTcpSocket()
test_socket.connectToHost('127.0.0.1',54545)
print("its working till here ")
str="testign testing"
b = bytes(str, 'UTF-8')
temp=test_socket.write(QtCore.QByteArray(b))
print(temp)
sys.exit(app.exec_())
