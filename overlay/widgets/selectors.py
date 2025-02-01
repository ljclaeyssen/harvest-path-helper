from PyQt5.QtWidgets import QPushButton, QListWidget, QListWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from data.job_data import jobs_data
from .buttons import TransparentButton

class DropdownListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        self.setStyleSheet("""
            QListWidget {
                background-color: rgba(50, 50, 50, 128);
                color: white;
                border: 1px solid gray;
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

class JobSelector(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.selected_job = jobs_data[0]  # Sélection initiale

        self.toggle_button = TransparentButton(self.selected_job.name, self)
        self.toggle_button.clicked.connect(self.toggle_list)

        self.job_list_widget = DropdownListWidget()
        for job in jobs_data:
            item = QListWidgetItem(job.name)
            item.setData(Qt.UserRole, job)
            self.job_list_widget.addItem(item)
        self.job_list_widget.itemClicked.connect(self.on_item_clicked)
        self.job_list_widget.hide()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.toggle_button)
        self.setLayout(layout)

    def toggle_list(self):
        if self.job_list_widget.isHidden():
            # Positionner la liste en dessous du bouton
            button_geometry = self.toggle_button.geometry()
            global_pos = self.mapToGlobal(button_geometry.bottomLeft())
            self.job_list_widget.setGeometry(global_pos.x(), global_pos.y(), button_geometry.width(), 200)
            self.job_list_widget.show()
        else:
            self.job_list_widget.hide()

    def on_item_clicked(self, item):
        self.selected_job = item.data(Qt.UserRole)
        self.toggle_button.setText(self.selected_job.name)
        self.parent.on_job_selected(self.selected_job)
        self.job_list_widget.hide()

class ResourceSelector(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.selected_resource = None
        self.toggle_button = TransparentButton("Select Resource", self)
        self.toggle_button.clicked.connect(self.toggle_list)

        self.resource_list_widget = DropdownListWidget()
        self.resource_list_widget.itemClicked.connect(self.on_item_clicked)
        self.resource_list_widget.hide()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.toggle_button)
        self.setLayout(layout)

        self.current_job = None  # Attribut pour stocker le métier actuellement sélectionné

    def update_resources(self, job):
        self.current_job = job
        self.resource_list_widget.clear()
        if job:
            for resource in job.harvestables:
                item = QListWidgetItem(resource.name)
                item.setData(Qt.UserRole, resource)
                self.resource_list_widget.addItem(item)
        self.toggle_button.setText("Select Resource")

    def toggle_list(self):
        if self.resource_list_widget.isHidden():
            # Positionner la liste en dessous du bouton
            button_geometry = self.toggle_button.geometry()
            global_pos = self.mapToGlobal(button_geometry.bottomLeft())
            self.resource_list_widget.setGeometry(global_pos.x(), global_pos.y(), button_geometry.width(), 200)
            self.resource_list_widget.show()
        else:
            self.resource_list_widget.hide()

    def on_item_clicked(self, item):
        self.selected_resource = item.data(Qt.UserRole)
        self.toggle_button.setText(self.selected_resource.name)
        self.parent.on_resource_selected(self.selected_resource)
        self.resource_list_widget.hide()