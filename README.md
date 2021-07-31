### AD Examen 1
##### Ejercicio 1 - Tweets por localización
En este ejercicio se usó el script para recoger tweets del stream que vengan de un área específica, en este caso se eligio las ciudades de Tokyo, Nagoya y Kanazawa junto con sus alrededores como indica el siguiente cuadro de cordenadas

![image](https://user-images.githubusercontent.com/66144847/127722276-982fe59e-fcb4-4ef9-95ea-20997f5c49e7.png)

Con estas coordernadas se pudo recoger tweets que probablemente hablen de los juegos olímpicos, pero no se puede saber a ciencia cierta porque se tendría que hacer filtrado avanzado, otro efecto secundario de recoger tweets solo por región es que posiblemente los tweets estarán en japonés.

Una vez recogidos los tweets, se guardaron en una base de couchdb como se muestra a continuación

![image](https://user-images.githubusercontent.com/66144847/127722390-f99f4d12-287a-4418-9c9c-3a87f7e36003.png)

##### Ejercicio 1 - Tweets por palabra clave
En este ejercicio se usó el script para recoger tweets del stream que contengan palabras clave específicas, en este caso se eligio las palabras "tokyo2021" y "olympics" para obtener tweets sobre los juegos olímpicos

Una vez recogidos los tweets, se guardaron en una base de couchdb como se muestra a continuación

![image](https://user-images.githubusercontent.com/66144847/127722548-a6ab0b62-2a7f-4a47-97fb-6b8069fcebae.png)
