import pytube
import os

video_url = input('indroducir la url del video a descargar: ')
formato = input('seleccione el formato para la descarga: \n a) Audio \n b) Video: ')

class YouTube_Downloader:
    def descargar_Videos(self, video_url):

        youtube = pytube.YouTube(video_url)
        print('descargando... espere unos minutos')

        youtube.streams.first().download(r'Videos')
        print('video descargado exitosamente', youtube.title)

    def descargar_Audio(self,video_url):
        youtube = pytube.YouTube(video_url)
        print('descargando... espere unos minutos')

        youtube.streams.first().download(r'Audios')
        print('audio descargado exitosamente', youtube.title)

while True:
    if formato == 'a':
        video = YouTube_Downloader().descargar_Audio(video_url)

        video_url = input('indroducir la url del video a descargar: ')
        formato = input('seleccione el formato para la descarga: \n a) Audio \n b) Video: ')

    elif formato == 'b':
        audio = YouTube_Downloader().descargar_Videos(video_url)
        
        video_url = input('indroducir la url del video a descargar: ')
        formato = input('seleccione el formato para la descarga: \n a) Audio \n b) Video: ')
        
    