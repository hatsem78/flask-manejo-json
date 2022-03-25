

## Getting Started

Se debe crear un Entornos Virtuales 
[Entornos-Virtuales-Turorial](http://docs.python.org.ar/tutorial/3/venv.html)\

simples paso para crear un virtualenv Python3
```
virtualenv -p python3 virtual_pru
```

Activar el virtual creado virtual_pru
```
source virtual_pru/bin/activate
```

Desactivar el virtual 
```
deactivate 
```
## Clone el repositorio

```
git clone https://github.com/hatsem78/flask_jwt.git
```

Instalar las dependencias

```
pip install -r requirements.txt
```
##Configuración base datos

## Configuración del entorno 
realizar una copia del archivo sample.env a .env


```
cp sample.env algo.env
```



cambiar los parametros según corresponda.

## Start the server

```
FLASK_APP=run.py FLASK_DEBUG=1 flask run
```



