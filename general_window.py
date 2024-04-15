from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap

class GeneralWindow(QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.setWindowTitle("General Window")
        self.setGeometry(100, 100, 400, 300)

        # Adjusting geometry for a 2.8 inch screen
        self.setGeometry(0, 0, 220, 320)

        # Logo
        self.logo_label = QLabel(self)
        self.logo_label.setGeometry(52, 10, 120, 120)
        pixmap = QPixmap('enterprise_logo.png')
        self.logo_label.setPixmap(pixmap)

        # Return button
        self.return_button = QPushButton("Return", self)
        self.return_button.clicked.connect(self.return_to_previous)

        # Save and reset buttons
        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_parameters)
        self.reset_button = QPushButton("Reset", self)
        self.reset_button.clicked.connect(self.reset_parameters)

        # Layout for buttons below logo
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.reset_button)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.return_button)  # Add return button at the top
        main_layout.addWidget(self.logo_label)  # Add logo label
        main_layout.addLayout(button_layout)  # Add buttons layout below logo
        self.setLayout(main_layout)

        self.previous_window = previous_window

    def save_parameters(self):
        # Implement saving parameters logic here
        print("Parameters saved")
        QMessageBox.information(self, "Save", "Settings saved successfully.")

    def reset_parameters(self):
        # Implement resetting parameters logic here
        print("Parameters reset")
        QMessageBox.information(self, "Reset", "Settings reset to default.")

    def return_to_previous(self):
        self.hide()
        self.previous_window.show()
