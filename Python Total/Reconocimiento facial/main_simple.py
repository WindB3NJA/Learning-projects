import cv2, pathlib, os
import face_recognition as fr

ROOT = pathlib.Path(os.getcwd()) / "images"

Folder_images = os.listdir(ROOT)


# Seleccionar imagenes
"""['img (1).jpg', 'img (2).jpg', 'img (3).jpg',
'img (4).jpg', 'img (5).jpg', 'img (6).jpg',
 'img (7).jpg', 'img (8).jpg']"""

img_1 = Folder_images[0]
img_2 = Folder_images[4]

# Cargar imagenes
img_control = fr.load_image_file(ROOT / img_1)
img_test = fr.load_image_file(ROOT / img_2)

# Convertir a RGB
img_control = cv2.cvtColor(img_control, cv2.COLOR_BGR2RGB)
img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)

# localizar rostros
face_place_1 = fr.face_locations(img_control)[0]
face_dec_1 = fr.face_encodings(img_control)[0]
face_place_2 = fr.face_locations(img_test)[0]
face_dec_2 = fr.face_encodings(img_test)[0]

# Mostrar las caras en las imagenes
cv2.rectangle(img_control,
              (face_place_1[3], face_place_1[0]),
              (face_place_1[1], face_place_1[2]),
              (0, 255, 0), 2)
cv2.rectangle(img_test,
                (face_place_2[3], face_place_2[0]),
                (face_place_2[1], face_place_2[2]),
                (0, 255, 0), 2)

# Comparar las caras
result = fr.compare_faces([face_dec_1], face_dec_2, 0.4)

# Medida de distancia
dist = fr.face_distance([face_dec_1], face_dec_2)

# Mostrar el resultado
cv2.putText(img_test, f"{result} {dist.round(2)}",(50,50),
            cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 255, 0),
                                2)

# Mostar imagenes
cv2.imshow("Control", img_control)
cv2.imshow("Test", img_test)


# No dejar que se cierre la ventana
cv2.waitKey(0)




