### AD Examen 1
##### Ejercicio 1 - Tweets por localización
En este ejercicio se usó el script para recoger tweets del stream que vengan de un área específica, en este caso se eligio las ciudades de Tokyo, Nagoya y Kanazawa junto con sus alrededores como indica el siguiente cuadro de cordenadas

![image](https://user-images.githubusercontent.com/66144847/127722276-982fe59e-fcb4-4ef9-95ea-20997f5c49e7.png)

Con estas coordernadas se pudo recoger tweets que probablemente hablen de los juegos olímpicos, pero no se puede saber a ciencia cierta porque se tendría que hacer filtrado avanzado, otro efecto secundario de recoger tweets solo por región es que posiblemente los tweets estarán en japonés.

Una vez recogidos los tweets, se guardaron en una base de couchdb como se muestra a continuación

![image](https://user-images.githubusercontent.com/66144847/127722390-f99f4d12-287a-4418-9c9c-3a87f7e36003.png)

##### Ejercicio 2 - Tweets por palabra clave
En este ejercicio se usó el script para recoger tweets del stream que contengan palabras clave específicas, en este caso se eligio las palabras "tokyo2021" y "olympics" para obtener tweets sobre los juegos olímpicos

Una vez recogidos los tweets, se guardaron en una base de couchdb como se muestra a continuación

![image](https://user-images.githubusercontent.com/66144847/127722548-a6ab0b62-2a7f-4a47-97fb-6b8069fcebae.png)

##### Ejercicio 3 - Webscraping
En este ejercicio se utilizó el script para recoger datos de una página web sobre las olimpiadas, en este caso se usó la página https://edition.cnn.com/world/live-news/tokyo-2020-olympics-07-30-21-spt/index.html
Inspeccionando la estructura de la página se ve que existen varios párrafos por título y no todos tienen la misma forma, por lo que sería muy complicado emparejar todos estos elementos con un título

![image](https://user-images.githubusercontent.com/66144847/127724198-2ac21abf-640b-4c0c-bd5b-092d957ede00.png)

Para no quedar sin información, se guarda el título de los artículos, el cual si está uniforme

![image](https://user-images.githubusercontent.com/66144847/127724254-c5a34e5e-2dfe-49ca-84bb-cae86d6eee93.png)

Ahora, se crea una base en mongoDB y una colección 

![image](https://user-images.githubusercontent.com/66144847/127722852-cad73390-556d-45e6-bd52-910e1c230b6d.png)

Luego de ejecutar el script, se puede ver como todos los datos se guardaron

![image](https://user-images.githubusercontent.com/66144847/127724291-8186f53d-e5b7-4cd2-9c84-34d15e6fe9d9.png)



