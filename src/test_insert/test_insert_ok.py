import requests
import pytest
import json
from src.helpers.db import DB
from src.helpers.envs import Envs
from src.helpers.helpers import Helpers

url_ = Envs.negocios #la idea es que este en un archivo con las envs encriptadas
fecha = Helpers.date_now
num = Helpers.num_random(1, 9999)

class Test_insert_ok:

    def test_pedido_post(self):
        url = (f"{url_}/api/negocio/v10/insert-pedidos-list")
        headers = {"Content-Type": "application/json"}
        user_data = {
            "codProducto ": 439,
            "codTipoSolicitud ": "RE",
            "fechaPedido ": f"{fecha}",
            "importe":  f"{num}",
            "esTotal": False,
            "idFormaPago": "CB",
            "idPedido ": "H7",
            "requiereAutorizacion": False,
            "origen": "OT"
        }
        response = requests.post(url, json=user_data, headers=headers)
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        assert 'Access-Control-Allow-Origin' in response.headers
        assert response.headers['Access-Control-Allow-Origin'] == "*"
        user_data = response.json()
        assert "idProceso" in user_data
        assert isinstance(user_data["codPrducto"], int)
        assert "cantidadErrores" in user_data
        assert isinstance(user_data["codPrducto"], int)
        assert "cantidadOperacionesProcesadas" in user_data
        assert isinstance(user_data["codPrducto"], int)

   
    def test_pedido_post_sin_cammpo_esTotal(self):  #La idea de este tipo de test es con cada campo requerido
        url = (f"{url_}/api/negocio/v10/insert-pedidos-list")
        headers = {"Content-Type": "application/json"}
        user_data = {
            "codProducto ": 439,
            "codTipoSolicitud ": "RE",
            "fechaPedido ": f"{fecha}",
            "importe":  f"{num}",
            "idFormaPago": "CB",
            "idPedido ": "H7",
            "requiereAutorizacion": False,
            "origen": "OT"
        }
        response = requests.post(url, json=user_data, headers=headers)
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        assert 'Access-Control-Allow-Origin' in response.headers
        assert response.headers['Access-Control-Allow-Origin'] == "*"
        user_data = response.json()
        assert user_data["msj"] == "Falta campo esTotal, por favor completar"

