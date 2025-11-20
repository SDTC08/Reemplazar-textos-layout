# Layout Text Replacer - Plugin para QGIS

## Descripción
Plugin de QGIS que permite buscar y reemplazar textos en elementos de etiqueta (labels) de los layouts/composiciones de impresión de forma rápida y sencilla.

## Características
- Reemplazar texto en un layout específico o en todos los layouts del proyecto
- Interfaz gráfica intuitiva
- Búsqueda y reemplazo de texto en todos los elementos de texto de los layouts
- Contador de reemplazos realizados


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


## Requisitos
- QGIS 3.0 o superior
- Python 3

## Notas importantes
- El plugin solo afecta elementos de tipo etiqueta/label en los layouts
- El reemplazo es sensible a mayúsculas/minúsculas
- Los cambios se aplican inmediatamente y no se pueden deshacer con Ctrl+Z
- Se recomienda guardar el proyecto antes de hacer reemplazos masivos


## Licencia
Este plugin es software libre y puede ser modificado y distribuido libremente.

## Autor
Tu Nombre - tu@email.com

## Contribuciones
Las contribuciones son bienvenidas. Por favor, reporta bugs o sugiere mejoras.
