from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QTimer, QEvent
from PyQt5.QtGui import QPainter, QColor, QPen
from overlay.widgets import TitleBar, ArrowLabel

class CustomOverlay(QWidget):
    def __init__(self):
        super().__init__()

        # Couleurs et transparence
        self.background_color = QColor(50, 50, 50, 128)
        self.border_color = QColor(50, 50, 50)
        self.border_width = 3

        # Taille de la fenêtre
        self.setGeometry(100, 100, 500, 800)

        # Flags pour la fenêtre
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) # On enlève le flag Qt.WindowTransparentForInput
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Barre de titre personnalisée
        self.title_bar = TitleBar(self)

        # Flèche
        self.arrow_label = ArrowLabel(self)

        # Variables pour la bordure
        self.isMouseOver = False
        self.borderTimer = QTimer(self)
        self.borderTimer.timeout.connect(self.updateBorder)
        self.borderTimer.start(50)

        # Met à jour la position des éléments quand CustomOverlay est redimensionné
        self.arrow_label.update_position()
        self.title_bar.setGeometry(0, 0, self.width(), self.title_bar.height)

        self.installEventFilter(self) # Ajout d'un filtre d'événements

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress or event.type() == QEvent.MouseButtonRelease:
            if self.rect().contains(event.pos()):
                # Gérer l'événement nous-même
                if event.type() == QEvent.MouseButtonPress:
                    self.mousePressEvent(event)
                elif event.type() == QEvent.MouseButtonRelease:
                    self.mouseReleaseEvent(event)
                return True # Bloquer l'événement pour les widgets en dessous
        return super().eventFilter(obj, event)

    def mouseMoveEvent(self, event):
        # Détection de la souris au-dessus de la fenêtre
        if self.rect().contains(event.pos()):
            self.isMouseOver = True
        else:
            self.isMouseOver = False
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), self.background_color)

        # Dessiner la bordure custom si la souris est au-dessus de la fenêtre
        if self.isMouseOver:
            painter.setPen(QPen(self.border_color, self.border_width))
            painter.drawRect(self.border_width // 2, self.border_width // 2,
                             self.width() - self.border_width, self.height() - self.border_width)

    def resizeEvent(self, event):
        # Redimensionner la barre de titre
        self.title_bar.setGeometry(0, 0, self.width(), self.title_bar.height)
        self.arrow_label.update_position()

    def updateBorder(self):
        if self.underMouse() != self.isMouseOver:
            self.isMouseOver = self.underMouse()
            self.update()