from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap

class LoRaParameters:
    def __init__(self, frequency="", spreading_factor="", coding_rate="", bandwidth="", mode_of_transmission="", tx_power="", fec=""):
        self.frequency = frequency
        self.spreading_factor = spreading_factor
        self.coding_rate = coding_rate
        self.bandwidth = bandwidth
        self.mode_of_transmission = mode_of_transmission
        self.tx_power = tx_power
        self.fec = fec

    @classmethod
    def load_from_file(cls, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                parameters = {}
                for line in lines:
                    key, value = line.strip().split(': ')
                    parameters[key] = value
                return cls(**parameters)
        except FileNotFoundError:
            return None

class LoRaWindow(QWidget):
    return_to_previous_window = pyqtSignal()

    def __init__(self, previous_window):
        super().__init__()
        self.setWindowTitle("LoRa Window")
        self.setGeometry(100, 100, 400, 300)

        # Adjusting geometry for a 2.8 inch screen
        self.setGeometry(0, 0, 220, 320)

        self.previous_window = previous_window

        # Logo
        self.logo_label = QLabel(self)
        self.logo_label.setGeometry(52, 40, 120, 120)  # Adjust position to make room for return button
        pixmap = QPixmap('enterprise_logo.png')
        self.logo_label.setPixmap(pixmap)

        self.return_button = QPushButton("Return", self)
        self.return_button.clicked.connect(self.return_to_previous)

        self.frequency_label = QLabel("Enter Frequency (KHz)", self)
        self.frequency_input = QLineEdit(self)
        
        # SF Parameters
        self.spreading_factor_label = QLabel("Spreading Factor:", self)
        self.spreading_factor_input = QComboBox(self)
        self.spreading_factor_input.addItems(["SF7", "SF8", "SF9", "SF10", "SF11", "SF12", "SF13", "SF14", "SF15"])
        # CR Parameters
        self.coding_rate_label = QLabel("Coding Rate:", self)
        self.coding_rate_input = QComboBox(self)
        self.coding_rate_input.addItems(["4:5", "4:6", "4:7", "4:8"])
        # BW Parameters
        self.bandwidth_label = QLabel("Bandwidth:", self)
        self.bandwidth_input = QComboBox(self)
        self.bandwidth_input.addItems(["125 (KHz)", "250 (KHz)", "500 (KHz)"])
        # Mode Parameters
        self.mode_of_transmission_label = QLabel("Mode of Transmission:", self)
        self.mode_of_transmission_input = QComboBox(self)
        self.mode_of_transmission_input.addItems(["LoRa Mode","FLRC:Fast LoRa Communication"])
        # TX Parameters
        self.tx_power_label = QLabel("TX Power:", self)
        self.tx_power_input = QLineEdit(self)

        # FEC Parameters
        self.fec_label = QLabel("Forward Error Correction (FEC):", self)
        self.fec_input = QComboBox(self)
        self.fec_input.addItems(["Enabled", "Disabled"])

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_parameters)

        layout = QVBoxLayout()
        layout.addWidget(self.return_button)  # Add return button at the top
        layout.addWidget(self.logo_label)
        layout.addWidget(self.frequency_label)
        layout.addWidget(self.frequency_input)

        # Add new parameters
        layout.addWidget(self.spreading_factor_label)
        layout.addWidget(self.spreading_factor_input)
        layout.addWidget(self.coding_rate_label)
        layout.addWidget(self.coding_rate_input)
        layout.addWidget(self.bandwidth_label)
        layout.addWidget(self.bandwidth_input)
        layout.addWidget(self.mode_of_transmission_label)
        layout.addWidget(self.mode_of_transmission_input)
        layout.addWidget(self.tx_power_label)
        layout.addWidget(self.tx_power_input)
        layout.addWidget(self.fec_label)
        layout.addWidget(self.fec_input)

        layout.addWidget(self.save_button)
        self.setLayout(layout)

        # Initialize parameters from file
        self.init_parameters_from_file()  # Call the method to initialize parameters

    def save_parameters(self):
        # Récupérer les valeurs saisies par l'utilisateur
        frequency = self.frequency_input.text()
        spreading_factor = self.spreading_factor_input.currentText()
        coding_rate = self.coding_rate_input.currentText()
        bandwidth = self.bandwidth_input.currentText()
        mode_of_transmission = self.mode_of_transmission_input.currentText()
        tx_power = self.tx_power_input.text()
        fec = self.fec_input.currentText()

        # Créer une chaîne de données avec les paramètres
        data_string = f"Frequency: {frequency}\n"
        data_string += f"Spreading Factor: {spreading_factor}\n"
        data_string += f"Coding Rate: {coding_rate}\n"
        data_string += f"Bandwidth: {bandwidth}\n"
        data_string += f"Mode of Transmission: {mode_of_transmission}\n"
        data_string += f"TX Power: {tx_power}\n"
        data_string += f"FEC: {fec}\n"

        # Écrire les données dans le fichier
        with open("user_entries.txt", "a") as fichier:
            fichier.write(data_string)

        # Afficher une boîte de message pour indiquer que les paramètres ont été enregistrés
        QMessageBox.information(self, "Success", "Parameters saved successfully.")

    def return_to_previous(self):
        self.hide()
        self.previous_window.show()

    def init_parameters_from_file(self):
        # Try loading parameters from file
        try:
            lora_params = LoRaParameters.load_from_file("user_entries.txt")
            if lora_params:
                # Set parameter values in the UI
                self.frequency_input.setText(lora_params.frequency)
                self.spreading_factor_input.setCurrentText(lora_params.spreading_factor)
                self.coding_rate_input.setCurrentText(lora_params.coding_rate)
                self.bandwidth_input.setCurrentText(lora_params.bandwidth)
                self.mode_of_transmission_input.setCurrentText(lora_params.mode_of_transmission)
                self.tx_power_input.setText(lora_params.tx_power)
                self.fec_input.setCurrentText(lora_params.fec)
            else:
                QMessageBox.warning(self, "Warning", "Failed to load parameters from file. Using default values.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error occurred while loading parameters: {str(e)}. Using default values.")
            # Fallback to default values
            self.set_default_parameters()

    def set_default_parameters(self):
        # Set default parameter values in the UI
        self.frequency_input.setText("868")
        self.spreading_factor_input.setCurrentText("SF12")
        self.coding_rate_input.setCurrentText("4:5")
        self.bandwidth_input.setCurrentText("125 (KHz)")
        self.mode_of_transmission_input.setCurrentText("LoRa Mode")
        self.tx_power_input.setText("14 (dBm)")
        self.fec_input.setCurrentText("Enabled")
