# file_importer.py
from PyQt5.QtWidgets import QFileDialog

def import_file():
    file_path, _ = QFileDialog.getOpenFileName(
        None, "Select CAD File", "", "CAD Files (*.dxf *.step)"
    )
    return file_path
