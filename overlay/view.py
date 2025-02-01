from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from overlay.widgets import TitleBar, JobSelector, ResourceSelector

class CustomOverlay(QWidget):
    def __init__(self):
        super().__init__()

        # Couleurs et transparence
        self.background_color = QColor(50, 50, 50, 128)
        self.border_color = QColor(255, 0, 0)
        self.border_width = 3

        # Taille de la fenêtre
        self.setGeometry(100, 100, 500, 800)

        # Flags pour la fenêtre
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Barre de titre personnalisée
        self.title_bar = TitleBar(self)

        # Sélecteur de métier
        self.job_selector = JobSelector(self)

        # Sélecteur de ressource (initiallement caché)
        self.resource_selector = ResourceSelector(self)
        self.resource_selector.hide()

        # Flèche (exemple simple, à améliorer)
        self.arrow_label = QLabel("➡️", self)
        self.arrow_label.setAlignment(Qt.AlignCenter)
        self.arrow_label.setStyleSheet("font-size: 50px; color: white;")
        self.updateArrowPosition()

        # Layout principal
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.title_bar)
        layout.addWidget(self.job_selector)
        layout.addWidget(self.resource_selector)
        layout.addWidget(self.arrow_label)
        layout.addStretch() # Pour pousser le contenu vers le haut
        self.setLayout(layout)

        # Variables pour la bordure
        self.isMouseOver = False
        self.borderTimer = QTimer(self)
        self.borderTimer.timeout.connect(self.updateBorder)
        self.borderTimer.start(50)

    def on_job_selected(self, selected_job):
        """Méthode appelée lorsqu'un métier est sélectionné."""
        print(f"Métier sélectionné : {selected_job.name}")
        self.resource_selector.update_resources(selected_job)
        self.resource_selector.show()

    def on_resource_selected(self, selected_resource):
        """Méthode appelée lorsqu'une ressource est sélectionnée."""
        print(f"Ressource sélectionnée : {selected_resource.name}")
        # Mettez ici le code pour mettre à jour l'affichage en fonction de la ressource sélectionnée

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
        self.updateArrowPosition()

    def updateArrowPosition(self):
        # Centrer la flèche dans la zone en dessous de la barre de titre et des selecteurs
        self.arrow_label.setGeometry(0, self.title_bar.height, self.width(), 50)

    def updateBorder(self):
        if self.underMouse() != self.isMouseOver:
            self.isMouseOver = self.underMouse()
            self.update()