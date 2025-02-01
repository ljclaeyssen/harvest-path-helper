import sys
from PyQt5.QtWidgets import QApplication
from overlay.view import CustomOverlay

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = CustomOverlay()
    overlay.show()
    sys.exit(app.exec_())