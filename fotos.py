import cv2
import os
import time

"""
Este código es para tomar las fotos con la webcam o cámara
que vas a estar usando, no olvides que es muy importante 
tomar fotos con la misma cámara que usarás para la visión.
"""

# Crear carpeta para almacenar las fotos si no existe
folder_name = "Nombre_de_tu_folder" 
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Iniciar la cámara
camera = cv2.VideoCapture(0)  # 0 es el índice de la webcam predeterminada
if not camera.isOpened():
    print("No se puede acceder a la cámara")
    exit()

"""
Variables que controlan, cuantas fotos tomarás y el
timestamp que usarás entre c/u de ellas.
"""
total_photos = 90
interval_seconds = 4

# Bucle para tomar las fotos
for i in range(1, total_photos + 1):
    # Leer la imagen desde la cámara
    ret, frame = camera.read()
    
    if not ret:
        print("Error al capturar la imagen")
        break
    
    # Mostrar la imagen en una ventana llamada "Cámara"
    cv2.imshow('Cámara', frame)
    
    # Guardar la imagen en la carpeta con un nombre secuencial
    photo_path = os.path.join(folder_name, f"foto_{i}.png")
    cv2.imwrite(photo_path, frame)
    
    print(f"Foto {i} guardada en {photo_path}")
    
    # Esperar 3 segundos entre cada foto
    time.sleep(interval_seconds)
    
    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
camera.release()
cv2.destroyAllWindows()
