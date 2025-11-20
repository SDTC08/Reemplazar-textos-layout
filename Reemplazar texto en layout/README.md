# Layout Text Replacer - Plugin para QGIS

## Descripción
Plugin de QGIS que permite buscar y reemplazar textos en elementos de etiqueta (labels) de los layouts/composiciones de impresión de forma rápida y sencilla.

## Características
- Reemplazar texto en un layout específico o en todos los layouts del proyecto
- Interfaz gráfica intuitiva
- Búsqueda y reemplazo de texto en todos los elementos de texto de los layouts
- Contador de reemplazos realizados

## Instalación

### Método 1: Instalación manual
1. Copia la carpeta `text_replacer_plugin` en el directorio de plugins de QGIS:
   - **Windows**: `C:\Users\[usuario]\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`
   - **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`

2. Renombra la carpeta a `text_replacer_plugin` si tiene otro nombre

3. Abre QGIS y ve a: **Complementos → Administrar e instalar complementos → Instalados**

4. Busca "Layout Text Replacer" y activa el checkbox

### Método 2: Crear ZIP para instalación
1. Comprime la carpeta `text_replacer_plugin` en un archivo ZIP
2. En QGIS: **Complementos → Administrar e instalar complementos → Instalar desde ZIP**
3. Selecciona el archivo ZIP creado

## Uso

1. Abre un proyecto de QGIS que contenga layouts/composiciones de impresión

2. Ve al menú: **Complementos → Layout Text Replacer → Reemplazar texto en layouts**
   O haz clic en el ícono de la barra de herramientas

3. En el diálogo que aparece:
   - **Buscar**: Ingresa el texto que deseas buscar
   - **Reemplazar**: Ingresa el texto nuevo
   - **Layout**: Selecciona el layout específico donde hacer el reemplazo
   - **Aplicar a todos los layouts**: Marca esta opción para reemplazar en todos los layouts del proyecto

4. Haz clic en "Reemplazar"

5. Se mostrará un mensaje con la cantidad de reemplazos realizados

## Ejemplos de uso

### Ejemplo 1: Actualizar año en todos los layouts
- Buscar: "2023"
- Reemplazar: "2024"
- Marcar: "Aplicar a todos los layouts"

### Ejemplo 2: Cambiar nombre de autor en un layout específico
- Buscar: "Juan Pérez"
- Reemplazar: "María González"
- Seleccionar layout específico

### Ejemplo 3: Actualizar nombre de proyecto
- Buscar: "Proyecto Piloto"
- Reemplazar: "Proyecto Final"
- Marcar: "Aplicar a todos los layouts"

## Requisitos
- QGIS 3.0 o superior
- Python 3

## Notas importantes
- El plugin solo afecta elementos de tipo etiqueta/label en los layouts
- El reemplazo es sensible a mayúsculas/minúsculas
- Los cambios se aplican inmediatamente y no se pueden deshacer con Ctrl+Z
- Se recomienda guardar el proyecto antes de hacer reemplazos masivos

## Estructura de archivos
```
text_replacer_plugin/
│
├── __init__.py                 # Inicialización del plugin
├── metadata.txt                # Metadatos del plugin
├── layout_text_replacer.py     # Lógica principal
├── text_replacer_dialog.py     # Interfaz gráfica
├── icon.png                    # Ícono del plugin (24x24 px)
└── README.md                   # Este archivo
```

## Desarrollo

### Archivos principales

**layout_text_replacer.py**: Contiene la clase principal del plugin que:
- Inicializa la interfaz y menús
- Gestiona las acciones del plugin
- Ejecuta la lógica de búsqueda y reemplazo en los layouts

**text_replacer_dialog.py**: Define el diálogo de interfaz gráfica con:
- Campos de búsqueda y reemplazo
- Selector de layouts
- Opciones para aplicar a todos los layouts

### Personalización
Puedes modificar el código para:
- Añadir opciones de búsqueda (case-sensitive, regex, etc.)
- Incluir preview de los cambios antes de aplicarlos
- Exportar un log de los cambios realizados
- Trabajar con otros tipos de elementos (no solo etiquetas)

## Solución de problemas

**El plugin no aparece en el menú**
- Verifica que la carpeta esté en el directorio correcto de plugins
- Revisa que el nombre de la carpeta sea `text_replacer_plugin`
- Reinicia QGIS

**Error al ejecutar el plugin**
- Verifica que todos los archivos estén presentes
- Revisa la consola de Python en QGIS para ver mensajes de error
- Asegúrate de tener un proyecto con layouts abierto

**No se encuentran los textos**
- La búsqueda es exacta (case-sensitive)
- Solo busca en elementos de tipo etiqueta/label
- Verifica que el texto exista en los layouts

## Licencia
Este plugin es software libre y puede ser modificado y distribuido libremente.

## Autor
Tu Nombre - tu@email.com

## Contribuciones
Las contribuciones son bienvenidas. Por favor, reporta bugs o sugiere mejoras.
