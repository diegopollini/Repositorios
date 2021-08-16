import os
from dotenv import load_dotenv
import requests as req
load_dotenv()

SERVIDOR = os.getenv("SERVIDOR")
ENDPOINT_PEDIDOS = os.getenv("ENDPOINT_PEDIDOS")
ENDPOINT_PRODUCTOS = os.getenv("ENDPOINT_PRODUCTOS")
ENDPOINT_CONSULTA_PEDIDOS = os.getenv("ENDPOINT_CONSULTA_PEDIDOS")
TOKEN = os.getenv ("TOKEN")

def consultaProductos():
	URL_CONSULTA_PRODUCTO = f"{SERVIDOR}/{ENDPOINT_PRODUCTOS}?{TOKEN}"
	
	consultaListaProductos = req.get(URL_CONSULTA_PRODUCTO)

	if (consultaListaProductos.status_code == 200):
		print("Conexión establecida")
		resultado = consultaListaProductos.json()
		print(resultado)
	else:
		print("Falso")

def cargaPedidos():
	while(True):
		print("---------------------------------------------------------------------------)")
		print("ABM PEDIDOS")
		print("Presione # para concluir")

		idProducto = input("Ingrese código del producto: ")
		if (idProducto =="#"):
			break
		cantProducto = input ("Ingrese cantidad:")
		
		if (cantProducto == "#"):
			break
		
		cadenaJSON = {"id": idProducto, "cantidad":cantProducto}

		URL_PEDIDO = f"{SERVIDOR}/{ENDPOINT_PEDIDOS}?{TOKEN}"

		pedido = req.post(URL_PEDIDO, cadenaJSON)

		if (pedido.status_code == 200):
			ordenPedido = pedido.json()
			print (ordenPedido["mensaje"]," con N°: ",ordenPedido["codigo"])
	
		else:
			print("Falso")

def consultasPedidos():
	while(True):
		print("---------------------------------------------------------------------------)")
		print("CONSULTA PEDIDOS")
		print("Presione # para concluir")
	
		idPedido= (input("Ingrese número de pedido: "))
		if (idPedido =="#"):
    			break
		URL_CONSULTA_PEDIDO = f"{SERVIDOR}/{ENDPOINT_CONSULTA_PEDIDOS}{idPedido}?{TOKEN}"
		consultaPedidos = req.get(URL_CONSULTA_PEDIDO)

		if (consultaPedidos.status_code == 200):
			detallePedido = consultaPedidos.json()
			#print(detallePedido)
			print("Pedido N°: ", idPedido)
			print("Código Producto: ",detallePedido["productos"]["id"])
			print("Cantidad: ", detallePedido["productos"]["cantidad"])
		else:
			print("Falso")

		idProducto = int(detallePedido["productos"]["id"])
		cantProducto = int(detallePedido["productos"]["cantidad"])
		
		URL_CONSULTA_PRODUCTO = f"{SERVIDOR}/{ENDPOINT_PRODUCTOS}?{TOKEN}"
		consultaListaProductos = req.get(URL_CONSULTA_PRODUCTO)

		resultado = consultaListaProductos.json()

		print(resultado)
		producto = resultado["productos"][idProducto-1]["id"]
		stock = resultado["productos"][idProducto-1]["stock"]
		print("El stock del producto: ", producto, "es: ", stock)

		if (stock >= cantProducto):
    			print("El pedido se puede procesar")
		else:
    			print("La cantidad pedida supera el stock en el almacén")

    	

def main():
	consultaProductos()
	cargaPedidos()
	consultasPedidos()

if (__name__=="__main__"):
    main()
