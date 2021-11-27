#!/usr/bin/python3
import sys
from PyQt5 import QtWidgets, QtCore

def interface():
    obj = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("my first window")
    window.setGeometry(250, 100, 600, 300)

    ####################################
    #label = QtWidgets.QLabel(window)
    #label.setText("Camera Control Panel")
    #label.move(300, 150)
    ####################################

    ####################################
    #satir = QtWidgets.QLineEdit(window)
    #satir.setEchoMode(QtWidgets.QLineEdit.Password)
    #satir.setText("2.4")
    #satir.setReadOnly(True)
    ####################################

    ####################################
    #button = QtWidgets.QPushButton(window)
    #button.setText("move")
    #button.setGeometry(100,100, 100, 100)
    #button.setEnabled(False)
    ####################################

    ####################################
    #radiobutton_one   = QtWidgets.QRadioButton(window)
    #radiobutton_two   = QtWidgets.QRadioButton(window)
    #radiobutton_three = QtWidgets.QRadioButton(window)
    #radiobutton_one.setText("option 1")
    #radiobutton_two.setText("option 2")
    #radiobutton_three.setText("option 3")
    #radiobutton_one.move(100,50)
    #radiobutton_two.move(100,70)
    #radiobutton_three.move(100,90)
    #radiobutton_three.setCheckable(False)
    ####################################

    ####################################
    #control_one = QtWidgets.QCheckBox(window)
    #control_two = QtWidgets.QCheckBox(window)
    #control_three = QtWidgets.QCheckBox(window)
    #control_one.setText("option 1")
    #control_two.setText("option 2")
    #control_three.setText("option 3")
    #control_one.move(100,50)
    #control_two.move(100,70)
    #control_three.move(100,90)
    #control_three.setCheckable(False)
    ####################################

    ####################################
    #box_one = QtWidgets.QComboBox(window)
    #box_one.addItem("scan")
    #box_one.addItem("odom")
    #box_one.addItem("cmd_vel")
    #print(box_one.count())
    #box_one.setItemText(2, "camera")
    ####################################

    ####################################
    #spin = QtWidgets.QDoubleSpinBox(window)
    #spin.setRange(5,25)
    #spin.setSingleStep(1.2)
    ####################################

    ####################################
    #slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, window)
    #slider.move(300, 150)
    #slider.setMinimum(0)
    #slider.setMaximum(10)
    #slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
    #slider.setTickInterval(2)
    #slider.setValue(8)
    ####################################

    ####################################
    #satir = QtWidgets.QLineEdit(window)
    #satir.setReadOnly(True)
    #button = QtWidgets.QPushButton(window)
    #button.move(0, 30)
    #button.setText("send")
    #def update():
    #    satir.setText("1.22")
    #button.clicked.connect(update)
    ####################################

    ####################################
    #button1 = QtWidgets.QPushButton(window)
    #button2 = QtWidgets.QPushButton(window)
    #button3 = QtWidgets.QPushButton(window)
    #button4 = QtWidgets.QPushButton(window)
    #button1.setText("button 1")
    #button2.setText("button 2")
    #button3.setText("button 3")
    #button4.setText("button 4")

    #mizanpajh = QtWidgets.QHBoxLayout()
    #mizanpajv = QtWidgets.QVBoxLayout()
    #mizanpajv.addWidget(button3)
    #mizanpajv.addWidget(button4)
    #mizanpajh.addWidget(button1)
    #mizanpajh.addWidget(button2)
    #mizanpajv.addLayout(mizanpajh)
    #window.setLayout(mizanpajv)
    ####################################

    ####################################

    #button1 = QtWidgets.QPushButton(window)
    #button2 = QtWidgets.QPushButton(window)
    #button3 = QtWidgets.QPushButton(window)
    #button4 = QtWidgets.QPushButton(window)
    #button1.setText("button 1")
    #button2.setText("button 2")
    #button3.setText("button 3")
    #button4.setText("button 4")
    #mizanpaj = QtWidgets.QGridLayout()
    #mizanpaj.addWidget(button1, 1, 1)
    #mizanpaj.addWidget(button2, 1, 2)
    #mizanpaj.addWidget(button3, 2, 1)
    #mizanpaj.addWidget(button4, 2, 2)
    #window.setLayout(mizanpaj)
    ####################################

    ####################################
    #labelone = QtWidgets.QLabel(window)
    #labeltwo = QtWidgets.QLabel(window)
    #labelone.setText("position x: ")
    #labeltwo.setText("position y: ")
    #satir1 = QtWidgets.QLineEdit(window)
    #satir2 = QtWidgets.QLineEdit(window)

    #mizanpaj = QtWidgets.QFormLayout()
    #mizanpaj.addRow(labelone, satir1)
    #mizanpaj.addRow(labeltwo, satir2)
    #window.setLayout(mizanpaj)
    ####################################

    window.show()
    sys.exit(obj.exec_())

interface()
