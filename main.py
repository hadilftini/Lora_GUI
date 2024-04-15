import sys
from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow
from setting_interface import RFTestInterface
from button_window import ButtonWindow
from lora_window import LoRaWindow
from general_window import GeneralWindow

class Controller:
    def __init__(self):
        self.login_window = LoginWindow()
        self.rf_interface = RFTestInterface(self.login_window)
        self.button_window = ButtonWindow("Your Button Text Here")
        self.lora_window = LoRaWindow(self.rf_interface)
        # Pass RFTestInterface as the previous window to GeneralWindow
        self.general_window = GeneralWindow(self.rf_interface)

        self.login_window.switch_window.connect(self.show_rf_interface)
        self.rf_interface.switch_lora_window.connect(self.show_lora_window)
        self.rf_interface.switch_general_window.connect(self.show_general_window)

    def show_login_window(self):
        self.rf_interface.hide()
        self.login_window.show()

    def show_rf_interface(self):
        self.login_window.hide()
        self.rf_interface.show()

    def show_lora_window(self):
        self.rf_interface.hide()
        self.lora_window.show()

    def show_general_window(self):  
        self.rf_interface.hide()
        self.general_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_login_window()
    sys.exit(app.exec_())