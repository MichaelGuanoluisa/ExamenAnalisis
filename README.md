# Examen Analisis de Datos Primer bimestre

1. Recolectar datos de twiter con el tema Juegos Olimpicos usando localizacion, guardar en base de datos couchdb y por ultimo pasar a mongodb en la nube.

  1.1. entramos a bounding box y seleccionamos una localizacion en mi caso seleccione
  primer ciudad Ecuador, Quito
  ![image](https://user-images.githubusercontent.com/66236038/127720420-839a27b4-d063-4bef-90f9-a52fc39435af.png)

  segunda ciudad Ecuador, Ibarra
  ![image](https://user-images.githubusercontent.com/66236038/127720495-a37f9b48-c352-48d4-8a53-c84e940b102d.png)

  tercera ciudad Ecuador, Guayaquil
  ![image](https://user-images.githubusercontent.com/66236038/127721288-3a7bd95f-3eea-47da-a3e2-a22f0127b438.png)

  anexo extracion de datos en esa localizacion
  ![image](https://user-images.githubusercontent.com/66236038/127720866-67977202-4ece-449a-acb3-eeaef64862f8.png)


2. Recopilamos datos sobre "Juegos olimpicos" de tweets con track y se guarda en una base de datos "olimpicos-couchdb" en una base de datos couchdb

  ![image](https://user-images.githubusercontent.com/66236038/127723910-0a1ad00d-1809-456c-8194-48bc85dd54f0.png)

3. Recopilamos datos con Web Scraping en la pagina web del comercio, estos datos se guardan en la base mongodb llamada "comercio" y coleccion "web", se extrajo el contenido de los articulos de noticias.

  ![image](https://user-images.githubusercontent.com/66236038/127723968-6cfa6eaf-77ac-4367-835f-33434db27123.png)

  se guarda como valor article 
  ![image](https://user-images.githubusercontent.com/66236038/127723990-4659d69c-0394-46c4-8a88-44a0ce31905c.png)


4. Recopilamos datos de facebook con la palabra "olimpicos" para ver los posts juegos olimpicos y se guardo en una base de datos llamada "facebook" y coleccion "fb_posts", intente porner "juegos olimpicos" pero me daba un error de sintaxis solo busca por una palabra.

![image](https://user-images.githubusercontent.com/66236038/127724707-52d700ec-7778-4469-ae20-44ac2def7a3f.png)

5. 
6. 
7. Pasamos los datos de couchdb a mongodb, enviamos y almacenamos en colecciones dentro de la base de datos llamada "examen"
![image](https://user-images.githubusercontent.com/66236038/127725245-b3499a4a-ec3a-4501-a007-90c4fa20e3dc.png)

8. Pasamos la base de datos examenes de mongo db a mongo db atlas, pero antes de eso las demas bases de datos que estaban en mongo db de los puntos 3 y 4 lo pase como coleccion dentro de examen 
![image](https://user-images.githubusercontent.com/66236038/127726084-752bf92f-db5e-40c5-825b-b9d2781a0e0a.png)
 y luego se envio a mongo db atlas 
 ![image](https://user-images.githubusercontent.com/66236038/127726097-954cc2e7-e448-40ed-95d6-0bd2975aa432.png)

9. Pasar los datos de mongodb atlas a csv 

10. Pasar los datos de mongodb atlas a json




