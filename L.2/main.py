from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint

def winner_generator():
    number = randint(0,99)
    
    winner.setText(str(number))
    text.setText("Winner")

app = QApplication([])
main = QWidget()
main.setWindowTitle("Winner generator")
main.move(900,90)
main.resize(400,200)

winner = QLabel("?")
text = QLabel("Push the button to generate winner number")
button = QPushButton("Generate")

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
main.setLayout(line)

button.clicked.connect(winner_generator)

main.show()
app.exec_()