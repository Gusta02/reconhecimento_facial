import face_recognition as fr


def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos

    return False, []

def get_rostos():

    rostos_conhecidos = []
    nomes_dos_rostos = []

    elon1 = reconhece_face("./img/elon_musk1.jpg")
    jeff1 = reconhece_face("./img/jeff_bezos1.jpg")

    if(elon1[0]):
        rostos_conhecidos.append(elon1[1][0])
        nomes_dos_rostos.append("Elon Musk")

    if(jeff1[0]):
        rostos_conhecidos.append(jeff1[1][0])
        nomes_dos_rostos.append("Jeff Bezos")

    return rostos_conhecidos, nomes_dos_rostos