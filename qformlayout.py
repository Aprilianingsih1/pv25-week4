import sys
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    fbox = QFormLayout()

    l1 = QLabel("Name")

    nm = QLineEdit()
    fbox.addRow('Names', nm)

    add1 = QLineEdit()
    add2 = QLineEdit()
    vbox = QVBoxLayout()
    vbox.addWidget(add1)
    vbox.addWidget(add2)
    fbox.addRow('Address', vbox)

    r1 = QRadioButton("Male")
    r2 = QRadioButton("Female")
    hbox = QHBoxLayout()
    hbox.addWidget(r1)
    hbox.addWidget(r2)
    hbox.addStretch()
    fbox.addRow(QLabel("Gender"), hbox)

    fbox.addRow(QPushButton("Submit"), QPushButton("Cancel"))

    win.setLayout(fbox)

    win.setWindowTitle("PyQt5")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()