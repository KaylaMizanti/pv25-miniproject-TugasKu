import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit,
    QPushButton, QComboBox, QCheckBox, QListWidget, QHBoxLayout, QDateEdit,
    QMessageBox
)
from PyQt5.QtCore import Qt, QDate

class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TugasKu (Aplikasi Manajer Tugas Kuliah Sederhana)")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        # Widget utama
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Set background
        central_widget.setStyleSheet("background-color: #f5e1ce;")  

        # Layout utama
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Label Nama dan NIM
        self.label_nama = QLabel("Nama: Kayla Mizanti\nNIM: F1D022127")
        main_layout.addWidget(self.label_nama)

        # Label Welcome
        self.label_welcome = QLabel("Welcome to TugasKu! 📚")
        self.label_welcome.setAlignment(Qt.AlignCenter)
        self.label_welcome.setStyleSheet("font-weight: bold; font-size: 16px; padding: 8px;")
        main_layout.addWidget(self.label_welcome)

        # Form input tugas
        form_layout = QHBoxLayout()

        self.input_tugas = QLineEdit()
        self.input_tugas.setPlaceholderText("Tulis tugas...")
        form_layout.addWidget(self.input_tugas)

        self.combo_matkul = QComboBox()
        self.combo_matkul.addItems([
            "Pemrograman Bergerak", "Pemrograman Visual",
            "Logika Fuzzy", "Pemsi", "IOT", "Smart City"
        ])
        form_layout.addWidget(self.combo_matkul)
        

        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True) 
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setDisplayFormat('dd/MM/yyyy')
        form_layout.addWidget(self.date_edit)

        self.checkbox_prioritas = QCheckBox("Prioritas")
        form_layout.addWidget(self.checkbox_prioritas)

        main_layout.addLayout(form_layout)

        # Tombol Tambah dan Hapus
        button_layout = QHBoxLayout()

        self.btn_tambah = QPushButton("➕ Tambah Tugas")
        self.btn_tambah.setStyleSheet("""
            background-color: #b02071;
            color: white;
            font-weight: bold;
            padding: 6px;
            border-radius: 8px;
        """)
        button_layout.addWidget(self.btn_tambah)

        self.btn_hapus = QPushButton("🗑️ Hapus Tugas")
        self.btn_hapus.setStyleSheet("""
            background-color: #e683ac;
            color: white;
            font-weight: bold;
            padding: 6px;
            border-radius: 8px;
        """)
        button_layout.addWidget(self.btn_hapus)

        main_layout.addLayout(button_layout)

        # List tugas
        self.list_tugas = QListWidget()
        self.list_tugas.setStyleSheet("""
            font-size: 14px;
            padding: 4px;
        """)  
        main_layout.addWidget(self.list_tugas)


        # Event handler
        self.btn_tambah.clicked.connect(self.tambah_tugas)
        self.btn_hapus.clicked.connect(self.hapus_tugas)

    def tambah_tugas(self):
        tugas = self.input_tugas.text()
        matkul = self.combo_matkul.currentText()
        deadline = self.date_edit.date().toString('dd/MM/yyyy')
        prioritas = self.checkbox_prioritas.isChecked()

        if tugas:
            tugas_final = f"{tugas} - {matkul} - {deadline}"
            if prioritas:
                tugas_final = "🔥 [PRIORITAS] " + tugas_final
            self.list_tugas.addItem(tugas_final)
            self.input_tugas.clear()
            self.checkbox_prioritas.setChecked(False)

            # Popup pemberitahuan
            QMessageBox.information(self, "Berhasil", "Tugas berhasil ditambahkan!")

    def hapus_tugas(self):
        list_items = self.list_tugas.selectedItems()
        if not list_items:
            QMessageBox.warning(self, "Peringatan", "Pilih tugas yang ingin dihapus terlebih dahulu!")
            return
        for item in list_items:
            self.list_tugas.takeItem(self.list_tugas.row(item))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())
