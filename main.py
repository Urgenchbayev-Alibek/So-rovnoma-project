import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QComboBox, QRadioButton, QPushButton, QMessageBox, QHBoxLayout
from database import Connection_DB

class MainWindow(QWidget):
    def __init__(self, db_conn):
        super().__init__()
        self.db_conn = db_conn
        self.setWindowTitle("So'rovnoma")
        self.setGeometry(200, 200, 400, 400)
        self.initUI()

    def initUI(self):
        self.main_v_layout = QVBoxLayout()

        self.ism_h_layout = QHBoxLayout()
        self.ism_label = QLabel("Ism")
        self.ism_input = QLineEdit()
        self.ism_input.setFixedWidth(200)
        self.ism_h_layout.addWidget(self.ism_label)
        self.ism_h_layout.addWidget(self.ism_input)

        self.Sharif_h_layout = QHBoxLayout()
        self.Sharif_label = QLabel("Sharif")
        self.Sharif_input = QLineEdit()
        self.Sharif_input.setFixedWidth(200)
        self.Sharif_h_layout.addWidget(self.Sharif_label)
        self.Sharif_h_layout.addWidget(self.Sharif_input)

        self.Yosh_h_layout = QHBoxLayout()
        self.Yosh_label = QLabel("Yosh")
        self.Yosh_input = QLineEdit()
        self.Yosh_input.setFixedWidth(200)
        self.Yosh_h_layout.addWidget(self.Yosh_label)
        self.Yosh_h_layout.addWidget(self.Yosh_input)

        self.Jins_h_layout = QHBoxLayout()
        self.Jins_label = QLabel("Jins")
        self.Jins_radio_v_buttons=QVBoxLayout()
        self.erkak_radio = QRadioButton("Erkak", self)
        self.ayol_radio = QRadioButton("Ayol", self)
        self.Jins_h_layout.addWidget(self.Jins_label)
        self.Jins_radio_v_buttons.addWidget(self.erkak_radio)
        self.Jins_radio_v_buttons.addWidget(self.ayol_radio)
        self.Jins_h_layout.addLayout(self.Jins_radio_v_buttons)


        self.Viloyat_h_layout = QHBoxLayout()
        self.Viloyat_label = QLabel("Viloyat")
        self.Viloyat_input = QComboBox(self)
        self.Viloyat_input.addItems([
            "Toshkent viloyati", "Andijon viloyati", "Farg'ona viloyati", "Namangan viloyati",
            "Samarqand viloyati", "Buxoro viloyati", "Navoiy viloyati", "Qashqadaryo viloyati",
            "Surxondaryo viloyati", "Jizzax viloyati", "Sirdaryo viloyati", "Xorazm viloyati"
        ])
        self.Viloyat_h_layout.addWidget(self.Viloyat_label)
        self.Viloyat_h_layout.addWidget(self.Viloyat_input)

        self.Telefon_h_layout = QHBoxLayout()
        self.Telefon_label = QLabel("Telefon")
        self.Telefon_input = QLineEdit('+')
        self.Telefon_h_layout.addWidget(self.Telefon_label)
        self.Telefon_h_layout.addWidget(self.Telefon_input)

        self.Fakultet_h_layout = QHBoxLayout()
        self.Fakultet_label = QLabel("Fakultet")
        self.Fakultet_input = QLineEdit()
        self.Fakultet_input.setFixedWidth(200)
        self.Fakultet_h_layout.addWidget(self.Fakultet_label)
        self.Fakultet_h_layout.addWidget(self.Fakultet_input)

        self.Kurs_h_layout = QHBoxLayout()
        self.Kurs_label = QLabel("Kurs")
        self.Kurs_input = QComboBox()
        self.Kurs_input.addItems(["1-kurs", "2-kurs", "3-kurs", "4-kurs"])
        self.Kurs_h_layout.addWidget(self.Kurs_label)
        self.Kurs_h_layout.addWidget(self.Kurs_input)

        self.save_button = QPushButton("Saqlash")
        self.save_button.clicked.connect(self.save_student)

        self.main_v_layout.addLayout(self.ism_h_layout)
        self.main_v_layout.addLayout(self.Sharif_h_layout)
        self.main_v_layout.addLayout(self.Yosh_h_layout)
        self.main_v_layout.addLayout(self.Jins_h_layout)
        self.main_v_layout.addLayout(self.Viloyat_h_layout)
        self.main_v_layout.addLayout(self.Telefon_h_layout)
        self.main_v_layout.addLayout(self.Fakultet_h_layout)
        self.main_v_layout.addLayout(self.Kurs_h_layout)
        self.main_v_layout.addWidget(self.save_button)

        self.setLayout(self.main_v_layout)

    def save_student(self):
        if not self.erkak_radio.isChecked() and not self.ayol_radio.isChecked():
            QMessageBox.warning(self, "Xatolik", "Erkak yoki Ayol tanlanishi kerak")
            return
        first_name = self.ism_input.text()
        last_name = self.Sharif_input.text()
        yosh = self.Yosh_input.text()
        jins = "Erkak" if self.erkak_radio.isChecked() else "Ayol"
        viloyat = self.Viloyat_input.currentText()
        telefon = self.Telefon_input.text()
        fakultet = self.Fakultet_input.text()
        kurs = self.Kurs_input.currentText()

        if first_name and last_name and yosh.isdigit() and telefon and fakultet:
            try:
                cursor = self.db_conn.cursor()
                cursor.execute(
                    "INSERT INTO students (first_name, last_name, age, gender, region, phone, faculty, course) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (first_name, last_name, int(yosh), jins, viloyat, telefon, fakultet, kurs)
                )
                self.db_conn.commit()
                QMessageBox.information(self, "Saqlandi", "Ma'lumotlar muvaffaqiyatli saqlandi!")
                self.clear_fields()
            except Exception as e:
                QMessageBox.critical(self, "Xatolik", f"Ma'lumotlarni saqlashda xatolik: {e}")
        else:
            QMessageBox.warning(self, "Xato", "Iltimos, barcha maydonlarni to'ldiring va yoshni raqam bilan kiriting")

    def clear_fields(self):
        self.ism_input.clear()
        self.Sharif_input.clear()
        self.Yosh_input.clear()
        self.erkak_radio.setChecked(False)
        self.Viloyat_input.setCurrentIndex(0)
        self.Telefon_input.clear()
        self.Fakultet_input.clear()
        self.Kurs_input.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    connection = Connection_DB().get_connection()
    main_window = MainWindow(connection)
    main_window.show()
    sys.exit(app.exec())
