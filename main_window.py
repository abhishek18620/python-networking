from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        #title
        self.setWindowTitle("MYQT APP")
        editor=QtWidgets.QTextEdit(self)
        self.setCentralWidget(editor)