import os
from dotenv import load_dotenv
import requests as req
load_dotenv()

SERVIDOR = os.getenv("SERVIDOR")
ENDPOINT_PEDIDOS = os.getenv("ENDPOINT_PEDIDOS")
ENDPOINT_PRODUCTOS = os.getenv("ENDPOINT_PRODUCTOS")
ENDPOINT_CONSULTA_PEDIDOS = os.getenv("ENDPOINT_CONSULTA_PEDIDOS")
TOKEN = os.getenv ("TOKEN")
URL_TELEGRAM = os.getenv("URL_TELEGRAM")
TOKEN_TELEGRAM = os.getenv("TOKEN_TELEGRAM")
ENDPOINT_TELEGRAM = os.getenv("ENDPOINT_TELEGRAM")
ID_CHAT = os.getenv("ID_CHAT")

def consulta_productos():
	URL_CONSULTA_PRODUCTO = f"{SERVIDOR}/{ENDPOINT_PRODUCTOS}?{TOKEN}"
	
	consulta_lista_productos = req.get(URL_CONSULTA_PRODUCTO)

	if (consulta_lista_productos.status_code == 200):
		print("Conexión establecida")
		resultado = consulta_lista_productos.json()
		print(resultado)
	else:
		print("Falso")

def carga_pedidos():
	while(True):
		print("---------------------------------------------------------------------------)")
		print("ABM PEDIDOS")
		print("Presione # para concluir")

		id_producto = input("Ingrese código del producto: ")
		if (id_producto =="#"):
			break
		cant_producto = input ("Ingrese cantidad:")
		
		if (cant_producto == "#"):
			break
		
		cadena_JSON = {"id": id_producto, "cantidad":cant_producto}

		URL_PEDIDO = f"{SERVIDOR}/{ENDPOINT_PEDIDOS}?{TOKEN}"

		pedido = req.post(URL_PEDIDO, cadena_JSON)

		if (pedido.status_code == 200):
			orden_pedido = pedido.json()
			print (orden_pedido["mensaje"]," con N°: ",orden_pedido["codigo"])
	
		else:
			print("Falso")

def consultas_pedidos():
	while(True):
		print("---------------------------------------------------------------------------)")
		print("CONSULTA PEDIDOS")
		print("Presione # para concluir")
	
		id_pedido= (input("Ingrese número de pedido: "))
		if (id_pedido =="#"):
    			break
		URL_CONSULTA_PEDIDO = f"{SERVIDOR}/{ENDPOINT_CONSULTA_PEDIDOS}{id_pedido}?{TOKEN}"
		consulta_pedidos = req.get(URL_CONSULTA_PEDIDO)

		if (consulta_pedidos.status_code == 200):
			detalle_pedido = consulta_pedidos.json()
			#print(detallePedido)
			print("Pedido N°: ", id_pedido)
			print("Código Producto: ",detalle_pedido["productos"]["id"])
			print("Cantidad: ", detalle_pedido["productos"]["cantidad"])
		else:
			print("Falso")

		id_producto = int(detalle_pedido["productos"]["id"])
		cant_producto = int(detalle_pedido["productos"]["cantidad"])
		
		URL_CONSULTA_PRODUCTO = f"{SERVIDOR}/{ENDPOINT_PRODUCTOS}?{TOKEN}"
		consulta_lista_productos = req.get(URL_CONSULTA_PRODUCTO)

		resultado = consulta_lista_productos.json()

		print(resultado)
		producto = resultado["productos"][id_producto-1]["id"]
		stock = resultado["productos"][id_producto-1]["stock"]
		print("El stock del producto: ", producto, "es: ", stock)

		if (stock >= cant_producto):
			print("El pedido se puede procesar")
			TEXTO = f"El pedido N°{id_pedido} puede procesarse. Se pidieron {cant_producto} unidades del producto {producto} y en stock hay {stock} unidades"
			URL_MENSAJE_TELEGRAM = f"{URL_TELEGRAM}{TOKEN_TELEGRAM}/{ENDPOINT_TELEGRAM}?chat_id={ID_CHAT}&text={TEXTO}"
			consulta = req.get(URL_MENSAJE_TELEGRAM)
			if (consulta.status_code == 200):
        			print("Mensaje enviado a grupo Telegram")
			else:
    				print("ERROR al enviar mensaje por Telegram")
		else:
			print("La cantidad pedida supera el stock en el almacén")
			TEXTO = f"El pedido N°{id_pedido} NO puede procesarse. La cantidad pedida supera el stock en el almacén. Se pidieron {cant_producto} unidades del producto {producto} y en stock hay {stock} unidades"
			URL_MENSAJE_TELEGRAM = f"{URL_TELEGRAM}{TOKEN_TELEGRAM}/{ENDPOINT_TELEGRAM}?chat_id={ID_CHAT}&text={TEXTO}"
			consulta = req.get(URL_MENSAJE_TELEGRAM)
				
			if (consulta.status_code == 200):
        			print("Mensaje enviado a grupo Telegram")
			else:
    				print("ERROR al enviar mensaje por Telegram")

def main():
	consulta_productos()
	carga_pedidos()
	consultas_pedidos()

if (__name__=="__main__"):
    main()
