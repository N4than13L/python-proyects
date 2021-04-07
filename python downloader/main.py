import pytube
import os

print("Bienvenid@ a Python Downloader.")
#\n Para salir escriba salir \n Para ayuda escriba h"
print("Author: José Nathaniel Bonilla")
print("----------------------------------------------------------")

class YouTube_Downloader:
    def descargar_Videos(self, video_url):

        youtube = pytube.YouTube(video_url)
        print('descargando... espere unos minutos')

        youtube.streams.first().download(r'Videos')
        print('video descargado exitosamente', youtube.title)
        print("------------------------------------------------------------------")
        
    def descargar_Audio(self,video_url):
        youtube = pytube.YouTube(video_url)
        print('descargando... espere unos minutos')

        youtube.streams.first().download(r'Audios')
        print('audio descargado exitosamente', youtube.title)
        print("------------------------------------------------------------------")

def Download(): 

    video_url = input('indroducir la url del video a descargar: ')
    formato = str(input('seleccione el formato para la descarga: \n a) Audio \n b) Video: '))   

    while True:
        if formato == 'a':
            video = YouTube_Downloader().descargar_Audio(video_url)
            break
        elif formato == 'b':
            video = YouTube_Downloader().descargar_Videos(video_url)
            break

while True:
    Download()
    Download()
   