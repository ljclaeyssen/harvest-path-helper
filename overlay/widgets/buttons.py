from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QSize

class TitleBarButton(QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                color: white;
                border: none;
                font-size: 16px;
            }}
            QPushButton:hover {{
                background-color: rgba(255, 0, 0, 100);
            }}
        """)

class TransparentButton(QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                color: white;
                border: none;
                font-size: 16px;
                padding: 5px;
                text-align: left;
            }}
            QPushButton:hover {{
                background-color: rgba(100, 100, 100, 100);
            }}
        """)

    def sizeHint(self):
        # Spécifier une taille préférée pour le bouton
        return QSize(100, 30)