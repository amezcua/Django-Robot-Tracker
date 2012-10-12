# Robot-tracket app.
# App que mira para cada solicitud si es de un robot. Inicialmente se parte de una lista vacia y se van almacenando los
# useragents de todas las solicitudes que intentan acceder a robots.txt en el directorio raiz en una lista
# para cada solicitud se mira la lista en un middleware que establece si la solicitud es de un robot o no.
