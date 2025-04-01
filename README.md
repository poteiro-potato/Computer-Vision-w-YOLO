# Computer Vision with YOLO

Este repositorio es una plantilla para el entrenamiento, prueba e implementación de redes neuronales dentro de Computer Vision utilizando YOLO de Ultralytics.

## Instalación de Librerías Necesarias
Para instalar las dependencias requeridas, ejecuta los siguientes comandos:

```bash
pip install ultralytics
pip install torch torchvision opencv-python
```

Estas son las librerías necesarias para entrenar correctamente el modelo YOLOv8. Se utiliza esta versión porque es la más reciente sin comprometer estabilidad.

---

## Estructura del Proyecto
Debes seguir esta estructura para organizar correctamente tus archivos:

```
/tu_proyecto/
│── /datasets/
│   ├── /dataset_actual/
│   │   ├── images/
│   │   │   ├── train/  # Imágenes de entrenamiento
│   │   │   ├── val/    # Imágenes de validación
│   │   │   ├── test/   # (Opcional) Imágenes de prueba
│   │   ├── labels/
│   │   │   ├── train/  # Etiquetas en formato YOLO para entrenamiento (provistas por Roboflow)
│   │   │   ├── val/    # Etiquetas en formato YOLO para validación (provistas por Roboflow)
│   │   │   ├── test/   # (Opcional) Etiquetas para prueba (provistas por Roboflow)
│   │   ├── data.yaml   # Archivo de configuración del dataset
│── buildNN.py  # Script para entrenamiento
```
Cualquier cosa, sientete libre de mandarme mnsj, éxito padrino.