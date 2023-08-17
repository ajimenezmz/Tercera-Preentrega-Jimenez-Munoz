Nombre: Edgar Alexis Jimenez Muñoz

Mi proyecto es un modelo de e-comerce para prendas de fabricación local. 

MODELOS:
-Prenda
	numSerie #Numero de serie de la prenda para facil identificacion
	tipoPrenda #Identifica el tipo de prenda, ej: "playera", "pantalon
	tela #Identifica el tipo de tela usada ej:"mezclilla"
	color #Color de la prenda
	talla #Talla, dada en Ch, M, G o EG (chico, mediano, grande, extra grande respectivamente)
	precio 
	stock #La cantidad que hay en stock

-Cliente
	nombre 
	direccion 
	correoElectronico
	numeroTelefono


#Mi intencion con este modelo (Orden) es que sea mayormente automatico. Permitir que el nombreCliente, direccion, cantidad, se llenen en el momento en el que el usuario haga una compra, pero para efectos de la entrega y por cuestion de tiempo, se tienen que llenar manualmente y es algo totalmente separado de ambos modelos. Pero para la entrega final deberia de tomar atributos de otros modelos.
-Orden 
	nombreCliente
	numSerieProd
	direccion
	cantidad

FUNCIONALIDAD:
El proyecto actualmente permite registrar objetos en tres modelos distintos.
En prenda se registran las prendas que se van a vender, con todos sus atributos.
En cliente se registran los usuarios que van a comprar alguna de las prendas disponibles.
En orden, idealmente, el usuario registrado podria poner una orden para comprar alguna de las prendas disponibles.
Por el momento toda la informacion esta publicamente disponible en tablas mostradas en cada pagina respectiva. Esto solo es con motivos de la entrega y tanto por seguridad como por utilidad no sera el caso para la entrega final.
De igual manera, existe un boton de busqueda en la pagina principal que permite filtrar todas las prendas existentes por su tipo. Es decir, si son pantalones, playeras, sudaderas, etc.

