import cv2, pathlib, os, numpy
import face_recognition as fr
from datetime import datetime

# Base de datos de imagenes
ROOT = pathlib.Path(os.getcwd()) / "employees"
my_images = []
employees_names = []
employees_list = os.listdir(ROOT)

for employee in employees_list:
    emp_img = cv2.imread(str(ROOT / employee))
    my_images.append(emp_img)
    employees_names.append(os.path.splitext(employee)[0])

# codificar las imagenes
def codex(images):
    # Lista de codex
    encoded_images = []
    # Codificar las imagenes a RGB
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Codificar las imagenes
        codexed = fr.face_encodings(image)[0]
        # Agregar a la lista
        encoded_images.append(codexed)
    # Retornar la lista
    return encoded_images

# registrar los ingresos
def register(employee_name):
    file = open("register.csv", "r+")
    list_data = file.readlines()
    regist_name = []
    for line in list_data:
        ingress = line.split(",")
        regist_name.append(ingress[0])
    if employee_name not in regist_name:
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        file.writelines(f"\n{employee_name},{time}")


# Codificar las imagenes
encoded_images = codex(my_images)

# Cargar imagen de la camara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer la imagen
great, img = cap.read()

if not great:
    print("No se pudo leer la imagen")
else:
    # Reconocer la imagen
    face_cap = fr.face_locations(img)

    # Codificar la imagen
    face_cap_codex = fr.face_encodings(img, face_cap)

    # Comparar las imagenes
    for face_codexed,face_place in zip(face_cap_codex, face_cap):
        result = fr.compare_faces(encoded_images, face_codexed, 0.4)
        dist = fr.face_distance(encoded_images, face_codexed)

        print(dist)

        index_compare = numpy.argmin(dist)
        if dist[index_compare] < 0.6:
            # Encontrar el nombre del empleado
            employee_name = employees_names[index_compare]
            y1, x2, y2, x1 = face_place
            # Dibujar el rectangulo
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, employee_name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            # Mostrar la imagen
            cv2.imshow(f"Empleado: {employee_name}", img)
            register(employee_name)
            cv2.waitKey(0)
        else:
            print(f"No se encontro coincidencias con la base de datos")
