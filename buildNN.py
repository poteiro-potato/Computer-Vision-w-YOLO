from ultralytics import YOLO

import os
os.chdir('Ruta/a/la/carpeta/general/donde/estés/trabajando') 
"""
Ojo, es la carpeta donde se encuentren tus códigos, 
dataset y todos los arcchivos con los que estés trabajando
"""
#Cargar el modelo preentrenado 
model = YOLO('yolov8s.pt') # Puedes trabajar con el 8s o el 8n
"""
yolov8s = small
yolov8n = nano

Evidentemente mientras más grande sea el modelo, más pesado será entrenar, 
recomiendo empezar con el 8n para pruebas, ya después avanzas con el 8s
"""

model.train(
    data='/Ruta/a/tu/data.yaml',
    epochs=100, # Empieza con 20 y de ahí vele calando            
    batch=32, # Dependiendo de cuantas imagenes,aumenta mientras más, pero empieza con 16             
    imgsz=320, # Esto es para la resolución de la imagen           
    device='mps', # Aquí cambia por '0' o 'cuda'        
    half=True,  # ni le muevas           
    workers=8,  # Los hilos del procesador          
    optimizer='AdamW',# Ni le muevas    
    verbose=False, # Tampoco le muevas        
    plots=False  # Esto es para que no te genera gráficas del rendimiento de tu modelo, alenta el entrenamiento          
)