import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QComboBox, QRadioButton, QPushButton, QMessageBox, QHBoxLayout
from database import Connection_DB

class MainWindow(QWidget):
    def __init__(self, db_conn):
        super().__init__()
        self.db_conn = db_conn
        self.setWindowTitle("So'rovnoma")
        self.setGeometry(300, 200, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.ism_label = QLabel("Ism")
        self.Sharif_label = QLabel("Sharif")
        self.Yosh_label = QLabel("Yosh")
        self.Jins_label = QLabel("Jins")
        self.Viloyat_label = QLabel("Viloyat")
        self.Telefon_label = QLabel("Telefon")
        self.Fakultet_label = QLabel("Fakultet")
        self.Kurs_label = QLabel("Kurs")
        self.save_button = QPushButton("Saqlash")
        self.save_button.clicked.connect(self.save_student)

        layout.addWidget(self.ism_label)
        layout.addWidget(self.Sharif_label)
        layout.addWidget(self.Yosh_label)
        layout.addWidget(self.Jins_label)
        layout.addWidget(self.Viloyat_label)
        layout.addWidget(self.Telefon_label)
        layout.addWidget(self.Fakultet_label)
        layout.addWidget(self.Kurs_label)
        layout.addWidget(self.save_button)

        layout2 = QVBoxLayout()
        self.ism_input = QLineEdit()
        self.Sharif_input = QLineEdit()
        self.Yosh_input = QLineEdit()
        self.erkak_radio = QRadioButton("Erkak", self)
        self.ayol_radio = QRadioButton("Ayol", self)
        self.erkak_radio.setChecked(True)
        self.Viloyat_input = QComboBox(self)
        self.Viloyat_input.addItems([
            "Toshkent viloyati", "Andijon viloyati", "Farg'ona viloyati", "Namangan viloyati",
            "Samarqand viloyati", "Buxoro viloyati", "Navoiy viloyati", "Qashqadaryo viloyati",
            "Surxondaryo viloyati", "Jizzax viloyati", "Sirdaryo viloyati", "Xorazm viloyati"
        ])
        self.Telefon_input = QLineEdit('+')
        self.Fakultet_input = QLineEdit()
        self.Kurs_input = QComboBox()
        self.Kurs_input.addItems(["1-kurs", "2-kurs", "3-kurs", "4-kurs"])

        layout2.addWidget(self.ism_input)
        layout2.addWidget(self.Sharif_input)
        layout2.addWidget(self.Yosh_input)
        layout2.addWidget(self.erkak_radio)
        layout2.addWidget(self.ayol_radio)
        layout2.addWidget(self.Viloyat_input)
        layout2.addWidget(self.Telefon_input)
        layout2.addWidget(self.Fakultet_input)
        layout2.addWidget(self.Kurs_input)

        main_layout = QHBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(layout2)
        self.setLayout(main_layout)

    def save_student(self):
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
                QMessageBox.information(self, "Muvaffaqiyatli", "Talaba ma'lumotlari saqlandi!")
                self.clear_fields()
            except Exception as e:
                QMessageBox.critical(self, "Xatolik", f"Ma'lumotlarni saqlashda xatolik: {e}")
        else:
            QMessageBox.warning(self, "Xato", "Iltimos, barcha maydonlarni to'ldiring va yoshni raqam bilan kiriting")

    def clear_fields(self):
        self.ism_input.clear()
        self.Sharif_input.clear()
        self.Yosh_input.clear()
        self.erkak_radio.setChecked(True)
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
