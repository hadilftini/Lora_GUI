from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QPixmap

class RFTestInterface(QWidget):
    switch_ping_pong_window = pyqtSignal()
    switch_lora_window = pyqtSignal()
    switch_general_window = pyqtSignal()

    def __init__(self, previous_window):
        super().__init__()
        self.setWindowTitle("Setting Test Interface")
        self.setGeometry(100, 100, 400, 300)

        # Adjusting geometry for a 2.8 inch screen
        self.setGeometry(0, 0, 220, 320)

        self.previous_window = previous_window

        # Logo
        self.logo_label = QLabel(self)
        self.logo_label.setGeometry(52, 10, 120, 120)
        pixmap = QPixmap('enterprise_logo.png')
        self.logo_label.setPixmap(pixmap)

        self.title_label = QLabel(" Setting Interface", self)
        self.title_label.setFont(QFont('Helvetica', 16))
        self.title_label.setAlignment(Qt.AlignCenter)

        self.button1 = QPushButton("PING PONG", self)
        self.button1.clicked.connect(self.open_ping_pong_window)

        self.button2 = QPushButton("LoRa", self)
        self.button2.clicked.connect(self.open_lora_window)

        self.button3 = QPushButton("Generale", self)
        self.button3.clicked.connect(self.open_general_window)

        self.return_button = QPushButton("Return", self)
        self.return_button.clicked.connect(self.return_to_previous_window)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.return_button)
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

    def open_ping_pong_window(self):
        self.switch_ping_pong_window.emit()

    def open_lora_window(self):
        self.switch_lora_window.emit()

    def open_general_window(self):
        self.switch_general_window.emit()

    def return_to_previous_window(self):
        self.hide()
        self.previous_window.show()
