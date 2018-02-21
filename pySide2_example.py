#! /usr/bin/python


import sys
from PySide2 import QtWidgets

def main():
    QtWidgets.QApplication.setLibraryPaths(["/Applications/Houdini/Houdini16.5.392/Frameworks/Houdini.framework/Versions/Current/Libraries/Qt_plugins", ])
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    button = QtWidgets.QPushButton("Hello, PyQt!")
    window.setCentralWidget(button)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
