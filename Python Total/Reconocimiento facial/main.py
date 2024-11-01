import cv2, pathlib, os
import face_recognition as fr

ROOT = pathlib.Path(os.getcwd()) / "images"
Folder_images = os.listdir(ROOT)
Img_names = []
Data_Images = []

counter = 0
# Cargar imagenes
for image in Folder_images:
    Img_names.append(image)
    data = fr.load_image_file(ROOT / image)
    rgb_data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
    Data_Images.append(rgb_data)
    counter += 1

counter = 0
for data in Data_Images:
    face_place = fr.face_locations(data)[0]
    face_dec = fr.face_encodings(data)[0]
    cv2.rectangle(data, (face_place[3], face_place[0]),
                  (face_place[1], face_place[2]),
                  (0, 255, 0), 2)
    cv2.imshow(f"Imagen {Img_names[counter]}", data)
    cv2.waitKey(0)
    counter += 1

