from face_recognition.api import face_distance, face_encodings
import numpy as np
import face_recognition as fr
import cv2
from engine import get_rostos

rostos_conhecidos, nomes_dos_rostos = get_rostos()



video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, :: -1]

    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_locations)


    for (top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
        resultados = fr.compare_faces(rostos_conhecidos, face_encodings)
        print(resultados)

        face_distance = fr.face_distance(rostos_conhecidos, face_encodings)

        best_match_index = np.argmin(face_distance)
        if resultados[best_match_index]:
            name = nomes_dos_rostos[best_match_index]

        else:
            name = "desconhecido"

        # Ao Redor do Rosto
        cv2.rectangle(frame,(left, top), (right, bottom), (0, 0, 255), 2)

        # Embaixo
        cv2.rectangle(frame,(left, bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Texto
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Webcam_facerecognition', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()