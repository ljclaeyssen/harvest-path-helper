from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QColor, QPen

class TitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent  # Gardez une référence à la fenêtre parente (CustomOverlay)
        self.background_color = QColor(50, 50, 50, 200)
        self.height = 30
        self.dragging = False
        self.drag_offset = QPoint()

        # Bouton pour fermer
        self.close_button = QPushButton("X", self)
        self.close_button.setFixedSize(self.height, self.height)
        self.close_button.setStyleSheet(f"""
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
        self.close_button.clicked.connect(self.parent.close) # Correction ici : appelle self.parent.close()

        # Layout
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(self.close_button)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.parent.move(event.globalPos() - self.drag_offset)

    def mouseReleaseEvent(self, event):
        self.dragging = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), self.background_color)

    def resizeEvent(self, event):
        self.close_button.setGeometry(self.width() - self.height, 0, self.height, self.height)

class ArrowLabel(QLabel):
    def __init__(self, parent):
        super().__init__("➡️", parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("font-size: 50px; color: white;")

    def update_position(self):
        # Centrer la flèche dans la zone en dessous de la barre de titre
        parent = self.parent()
        if parent:
            self.setGeometry(0, parent.title_bar.height, parent.width(), parent.height() - parent.title_bar.height)