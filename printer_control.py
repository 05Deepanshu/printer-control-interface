import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtWidgets import QSpinBox
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import Qt

def get_printers():
    return ["Printer 1", "Printer 2", "Printer 3"]
def get_printer_status(printer_id):
    return f"Status: Online, Paper: OK, Ink: 75%"
def send_print_job(printer_id, document, options):
    return "Job sent successfully"
def cancel_print_job(printer_id, job_id):
    return f"Job {job_id} cancelled"
def get_print_queue(printer_id):
    return ["Job 1: Document A", "Job 2: Document B"]
def perform_maintenance(printer_id, task):
    return f"Maintenance task '{task}' completed"

class PrinterControlGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Printer Control Interface")
        self.setGeometry(100, 100, 600, 400)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        printer_layout = QHBoxLayout()
        self.printer_combo = QComboBox()
        self.printer_combo.addItems(get_printers())
        printer_layout.addWidget(QLabel("Select Printer:"))
        printer_layout.addWidget(self.printer_combo)
        main_layout.addLayout(printer_layout)

        self.status_label = QLabel("Printer Status: ")
        main_layout.addWidget(self.status_label)

        
        job_layout = QHBoxLayout()
        self.copies_spin = QSpinBox()
        self.copies_spin.setMinimum(1)
        self.page_range_edit = QLineEdit()
        self.quality_combo = QComboBox()
        self.quality_combo.addItems(["Draft", "Normal", "High"])
        job_layout.addWidget(QLabel("Copies:"))
        job_layout.addWidget(self.copies_spin)
        job_layout.addWidget(QLabel("Page Range:"))
        job_layout.addWidget(self.page_range_edit)
        job_layout.addWidget(QLabel("Quality:"))
        job_layout.addWidget(self.quality_combo)
        main_layout.addLayout(job_layout)

        self.send_job_button = QPushButton("Send Print Job")
        main_layout.addWidget(self.send_job_button)

        self.queue_text = QTextEdit()
        self.queue_text.setReadOnly(True)
        main_layout.addWidget(QLabel("Print Queue:"))
        main_layout.addWidget(self.queue_text)

        cancel_layout = QHBoxLayout()
        self.cancel_job_edit = QLineEdit()
        self.cancel_job_button = QPushButton("Cancel Job")
        cancel_layout.addWidget(QLabel("Job ID:"))
        cancel_layout.addWidget(self.cancel_job_edit)
        cancel_layout.addWidget(self.cancel_job_button)
        main_layout.addLayout(cancel_layout)

        maintenance_layout = QHBoxLayout()
        self.maintenance_combo = QComboBox()
        self.maintenance_combo.addItems(["Clean Print Heads", "Align Printer"])
        self.maintenance_button = QPushButton("Perform Maintenance")
        maintenance_layout.addWidget(self.maintenance_combo)
        maintenance_layout.addWidget(self.maintenance_button)
        main_layout.addLayout(maintenance_layout)

        self.printer_combo.currentIndexChanged.connect(self.update_printer_status)
        self.send_job_button.clicked.connect(self.send_print_job)
        self.cancel_job_button.clicked.connect(self.cancel_print_job)
        self.maintenance_button.clicked.connect(self.perform_maintenance)

        self.update_printer_status()
        self.update_print_queue()

    def update_printer_status(self):
        printer_id = self.printer_combo.currentText()
        status = get_printer_status(printer_id)
        self.status_label.setText(f"Printer Status: {status}")

    def send_print_job(self):
        printer_id = self.printer_combo.currentText()
        options = {
            "copies": self.copies_spin.value(),
            "page_range": self.page_range_edit.text(),
            "quality": self.quality_combo.currentText()
        }
        result = send_print_job(printer_id, "Document", options)
        self.show_message(result)
        self.update_print_queue()

    def cancel_print_job(self):
        printer_id = self.printer_combo.currentText()
        job_id = self.cancel_job_edit.text()
        result = cancel_print_job(printer_id, job_id)
        self.show_message(result)
        self.update_print_queue()

    def perform_maintenance(self):
        printer_id = self.printer_combo.currentText()
        task = self.maintenance_combo.currentText()
        result = perform_maintenance(printer_id, task)
        self.show_message(result)

    def update_print_queue(self):
        printer_id = self.printer_combo.currentText()
        queue = get_print_queue(printer_id)
        self.queue_text.setText("\n".join(queue))

    def show_message(self, message):
        print(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrinterControlGUI()
    window.show()
    sys.exit(app.exec())