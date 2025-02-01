from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QHBoxLayout, QWidget, QLabel, QListView
from PyQt5.QtCore import Qt
from data.job_data import jobs_data


class JobListWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.main_layout = QHBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.setViewMode(QListView.IconMode)
        self.list_widget.setMovement(QListView.Static)
        self.list_widget.setResizeMode(QListView.Adjust)
        self.list_widget.setSpacing(0)
        self.list_widget.setFlow(QListView.LeftToRight)

        for job in jobs_data:
            item = QListWidgetItem(job.name)
            item.setData(Qt.UserRole, job)  # Stocker l'objet Job complet dans l'item
            # Personnalisez l'apparence de l'item ici si nécessaire
            self.list_widget.addItem(item)

        self.list_widget.itemClicked.connect(self.on_item_clicked)
        self.setStyleSheet("""
            QListWidget {
                background-color: rgba(50, 50, 50, 128);
                color: white;
                border: none;
            }
            QListWidget::item {
                padding: 5px;
            }
            QListWidget::item:selected {
                background-color: rgba(255, 0, 0, 100);
            }
            QListWidget::item:hover {
                background-color: rgba(100, 100, 100, 100);
            }
        """)

        # Layout
        self.main_layout.addWidget(self.list_widget)
        self.setLayout(self.main_layout)

    def on_item_clicked(self, item):
        selected_job = item.data(Qt.UserRole)
        self.parent.parent.on_job_selected(selected_job)