# LAB_1_Ambiente-de-trabajo_IA
# Integrantes: Eduardo Díaz del Castillo, Abdiel Alveo, Astrid Hurley

Instalación de ROS (Representación del Conocimiento) LAB 1. Ambiente de trabajo

Lineamientos del proyecto:

1. Seguir el instructivo de la instalación de ROS. (ros-melodic-desktop-full)
2. Crear un entorno de trabajo para ejecutar un experimento de ROS.
3. Configurar el entorno del usuario para que pueda llamar los comandos de ROS como parte de los comandos del sistema operativo
4. Leer la documentación de ROS
5. Escribir un programa en C++, Python o Java que:
Cada 5 segundos genere un número aleatorio, y lo envie a a traves de un topico de ROS hacia otro NODO, que lo reciba y lo grafique en cada interacción.

¿Qué se debe entregar?
1. Codigo del programa que genera los número aleatorios y el que lo recibe.
Los archivos estan en la carpeta script dentro de my_first_package nombrados como talker.py y listener.py

Primero debemos tener una terminal corriendo roscore.
En otra terminal compilamos rosrun my_first_package talker.py (Saliendo como resultado el programa de numeros aleatorios cada 5 segundos)

![alt text](https://github.com/ryu-ed/LAB_1_Ambiente-de-trabajo_IA/raw/master/talker.png " ")

En otra terminal compilamos rosrun my_first_package listener.y (Despues de haber ejecutado el talker.py) Donde recibe los datos del talker.py

![alt text](https://github.com/ryu-ed/LAB_1_Ambiente-de-trabajo_IA/raw/master/listener.png " ")

2. Imagen generado por el programa rqt_graph donde se muestra el comportamiento de los nodos.
En otra terminal ejecutamos rqt_graph donde nos muestra el comportamiento de los nodos. 
![alt text](https://github.com/ryu-ed/LAB_1_Ambiente-de-trabajo_IA/raw/master/rqt.png " ")

Donde vemos graficamente como se comportan los nodos. 

3. Estructura de datos que usaron para trasmitir la información (rostopic info <nombre del topico>)
![alt text](https://github.com/ryu-ed/LAB_1_Ambiente-de-trabajo_IA/raw/master/rostopic.png " ")
  
Vemos la estructura que se uso para transmitir la informacion (Nombre del topico: /chatter)
