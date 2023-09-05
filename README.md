# TFG_Reconocimiento_de_habla_en_dispositivos_portables
Se trata de un sistema de aprendizaje automático para la detección de emociones en el habla.

Los audios con los que se quieran realizar las pruebas deben estar en una carpeta llamada: 'AudioWAV'
Esta carpeta se tiene que comprimir en: 'archive.zip'
Y esta última carpeta zip resultante tendrá que estar en una carpeta denominada: 'data'
Es decir, la disposición de carpetas referentes a los audios quedaría de la siguiente forma:
data//archive.zip//AudioWAV  

La carpeta 'src', el archivo jupyter, y el csv correspondiente con los datos de los audios estarán al mismo nivel que la carpeta 'data'.

El archivo que se tiene que ejecutar para obtener el dataset es 'PrepareDataset.ypynb' y si no surge ningún inconveniente, se generará una carpeta resultante llamada 'datasets', que es la que se utilizará en el archivo principal 'Prueba1_HuggingSound.ipynb'.
