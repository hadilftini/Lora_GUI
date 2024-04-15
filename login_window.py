from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QSettings
from PyQt5.QtGui import QFont, QPixmap

class LoginWindow(QWidget):
    switch_window = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 400, 300)

        # Adjusting geometry for a 2.8 inch screen
        self.setGeometry(0, 0, 220, 320)

        # Logo
        self.logo_label = QLabel(self)
        self.logo_label.setGeometry(52, 10, 120, 120)
        pixmap = QPixmap('enterprise_logo.png')
        self.logo_label.setPixmap(pixmap)

        self.title_label = QLabel("Irwise Data Logger", self)
        self.title_label.setFont(QFont('Helvetica', 16))
        self.title_label.setAlignment(Qt.AlignCenter)

        self.label_username = QLabel("Username:", self)
        self.label_password = QLabel("Password:", self)

        self.entry_username = QLineEdit(self)
        self.entry_password = QLineEdit(self)
        self.entry_password.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.logo_label)
        layout.addWidget(self.title_label)
        layout.addWidget(self.label_username)
        layout.addWidget(self.entry_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.entry_password)
        layout.addWidget(self.login_button)
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

        # Load login after creating the widgets
        self.load_login()

    def load_login(self):
        settings = QSettings('login.ini', QSettings.IniFormat)
        username = settings.value('Login/username', '')
        password = settings.value('Login/password', '')
        self.entry_username.setText('')
        self.entry_password.setText('')

    def login(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        settings = QSettings('login.ini', QSettings.IniFormat)
        correct_username = settings.value('Login/username')
        correct_password = settings.value('Login/password')

        if username == correct_username and password == correct_password:
            QMessageBox.information(self, "Login Successful", f"Welcome, {username}")
            self.switch_window.emit()  # Emit signal to switch window
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")
