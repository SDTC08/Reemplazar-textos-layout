from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.core import QgsProject
from .text_replacer_dialog import TextReplacerDialog
import os


class LayoutTextReplacer:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.actions = []
        self.menu = self.tr(u'&Layout Text Replacer')
        self.toolbar = self.iface.addToolBar(u'LayoutTextReplacer')
        self.toolbar.setObjectName(u'LayoutTextReplacer')
        self.dialog = None

    def tr(self, message):
        return QCoreApplication.translate('LayoutTextReplacer', message)

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        icon_path = os.path.join(self.plugin_dir, 'icon.png')
        self.add_action(
            icon_path,
            text=self.tr(u'Reemplazar texto en layouts'),
            callback=self.run,
            parent=self.iface.mainWindow())

    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Layout Text Replacer'),
                action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar

    def run(self):
        if self.dialog is None:
            self.dialog = TextReplacerDialog()
            self.dialog.replace_button.clicked.connect(self.replace_text)
        
        # Obtener todos los layouts del proyecto
        layouts = QgsProject.instance().layoutManager().layouts()
        layout_names = [layout.name() for layout in layouts]
        
        if not layout_names:
            QMessageBox.warning(
                self.iface.mainWindow(),
                "Sin layouts",
                "No hay layouts en el proyecto actual."
            )
            return
        
        self.dialog.populate_layouts(layout_names)
        self.dialog.show()

    def replace_text(self):
        search_text = self.dialog.search_input.text()
        replace_text = self.dialog.replace_input.text()
        selected_layout = self.dialog.layout_combo.currentText()
        replace_all = self.dialog.all_layouts_check.isChecked()
        
        if not search_text:
            QMessageBox.warning(
                self.dialog,
                "Texto vacío",
                "Por favor ingresa el texto a buscar."
            )
            return
        
        replacements = 0
        layout_manager = QgsProject.instance().layoutManager()
        
        if replace_all:
            layouts = layout_manager.layouts()
        else:
            layout = layout_manager.layoutByName(selected_layout)
            layouts = [layout] if layout else []
        
        for layout in layouts:
            for item in layout.items():
                # Verificar si es un item de etiqueta (QgsLayoutItemLabel)
                if hasattr(item, 'text') and callable(item.text):
                    current_text = item.text()
                    if search_text in current_text:
                        new_text = current_text.replace(search_text, replace_text)
                        item.setText(new_text)
                        replacements += 1
        
        if replacements > 0:
            QMessageBox.information(
                self.dialog,
                "Reemplazo completado",
                f"Se realizaron {replacements} reemplazos en los layouts."
            )
        else:
            QMessageBox.information(
                self.dialog,
                "Sin coincidencias",
                "No se encontró el texto buscado en ningún layout."
            )
        
        # Actualizar la vista
        self.iface.mapCanvas().refresh()
