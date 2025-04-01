import cv2
from ultralytics import YOLO

"""
Este código te permite testear tu modelo recién entrenado,
usa la cámara para devolver los resultados de identificación
que arroja el modelo.

Recuerda de preferencia usar siempre la misma cámara.

*Nota: Puedes modificarlo para que use fotos en tu computadora
en vez de usar la cámara si te es más cómodo.
"""

# Ruta al archivo del modelo entrenado
model_path = 'Ruta/a/tu/modelo/best.pt'  # Ajusta esta ruta pal nuevo modelo, que no se te olvide rey

# Cargar el modelo entrenado
model = YOLO(model_path)

# Inicializar la webcam (0 es la webcam por defecto, si tienes varias puedes cambiarlo)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error al abrir la webcam.")
    exit()

while True:
    # Capturar frame de la webcam
    ret, frame = cap.read()
    if not ret:
        print("Error al recibir frame.")
        break

    # Usar el modelo para hacer predicciones en el frame
    results = model(frame)

    # Dibujar rectángulos y etiquetas en el frame para cada detección
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas del rectángulo
            confidence = box.conf[0]  # Confianza de la predicción
            class_id = int(box.cls[0])  # Clase predicha por el modelo
            """
            Este era el algoritmo que usamos para los cortadores,
            no lo quise modificar para que te puedas guiar, pero, 
            no olvides que debes modificarlo a tus necesidades.

            El 'class_id' es el índice que tiene tu categoría
            con respecto a la lista de clases (categorías) que 
            declaraste en tu 'data.yaml'

            Ejemplo:
            names: ['Centros', 'Cortador_Bola', 'Cortador_Plano']
            
            La broca de centros ocupa el índice '0' en la lista, por
            eso tiene el 'class_id == 0'
            """
            # Comprobamos si es la clase que identifica "cortador plano"
            # Supongamos que el modelo fue entrenado con 'cortador plano' como clase 0
            if class_id == 0:  # Cambia esto según tu modelo
                # Dibujar el rectángulo alrededor del objeto detectado
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Verde para el rectángulo
                
                # Colocar la etiqueta con el texto "cortador plano"
                label = "Centros"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            elif class_id == 1:
                # Dibujar el rectángulo alrededor del objeto detectado
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Verde para el rectángulo
                
                # Colocar la etiqueta con el texto "cortador plano"
                label = "Cortador bola"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            elif class_id == 2:
                # Dibujar el rectángulo alrededor del objeto detectado
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Verde para el rectángulo
                
                # Colocar la etiqueta con el texto "cortador plano"
                label = "Cortador Plano"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    # Mostrar el frame con las anotaciones
    cv2.imshow('Deteccion de Herramental', frame)

    # Presionar 'q' para salir del loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la webcam y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
