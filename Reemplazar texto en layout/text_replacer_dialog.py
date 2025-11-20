from qgis.PyQt.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                                   QLineEdit, QPushButton, QComboBox, QCheckBox,
                                   QGroupBox)
from qgis.PyQt.QtCore import Qt


class TextReplacerDialog(QDialog):
    def __init__(self, parent=None):
        super(TextReplacerDialog, self).__init__(parent)
        
        self.setWindowTitle("Reemplazar texto en Layouts")
        self.setMinimumWidth(450)
        
        # Layout principal
        main_layout = QVBoxLayout()
        
        # Grupo de búsqueda y reemplazo
        search_group = QGroupBox("Búsqueda y Reemplazo")
        search_layout = QVBoxLayout()
        
        # Campo de búsqueda
        search_h_layout = QHBoxLayout()
        search_label = QLabel("Buscar:")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Texto a buscar...")
        search_h_layout.addWidget(search_label)
        search_h_layout.addWidget(self.search_input)
        search_layout.addLayout(search_h_layout)
        
        # Campo de reemplazo
        replace_h_layout = QHBoxLayout()
        replace_label = QLabel("Reemplazar:")
        self.replace_input = QLineEdit()
        self.replace_input.setPlaceholderText("Texto nuevo...")
        replace_h_layout.addWidget(replace_label)
        replace_h_layout.addWidget(self.replace_input)
        search_layout.addLayout(replace_h_layout)
        
        search_group.setLayout(search_layout)
        main_layout.addWidget(search_group)
        
        # Grupo de selección de layout
        layout_group = QGroupBox("Seleccionar Layout")
        layout_group_layout = QVBoxLayout()
        
        # Combo box para layouts
        layout_select_layout = QHBoxLayout()
        layout_label = QLabel("Layout:")
        self.layout_combo = QComboBox()
        layout_select_layout.addWidget(layout_label)
        layout_select_layout.addWidget(self.layout_combo)
        layout_group_layout.addLayout(layout_select_layout)
        
        # Checkbox para todos los layouts
        self.all_layouts_check = QCheckBox("Aplicar a todos los layouts")
        self.all_layouts_check.stateChanged.connect(self.toggle_layout_combo)
        layout_group_layout.addWidget(self.all_layouts_check)
        
        layout_group.setLayout(layout_group_layout)
        main_layout.addWidget(layout_group)
        
        # Botones
        button_layout = QHBoxLayout()
        self.replace_button = QPushButton("Reemplazar")
        self.replace_button.setDefault(True)
        self.close_button = QPushButton("Cerrar")
        self.close_button.clicked.connect(self.close)
        
        button_layout.addStretch()
        button_layout.addWidget(self.replace_button)
        button_layout.addWidget(self.close_button)
        
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)
    
    def populate_layouts(self, layout_names):
        """Poblar el combo box con los nombres de los layouts"""
        self.layout_combo.clear()
        self.layout_combo.addItems(layout_names)
    
    def toggle_layout_combo(self, state):
        """Habilitar/deshabilitar el combo de layouts según el checkbox"""
        self.layout_combo.setEnabled(state != Qt.Checked)
