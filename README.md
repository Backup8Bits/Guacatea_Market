<h1 align="center">Bienvenidos a Guacatea Market 🛒</h1>

## 🥑 ¿Qué es Guacatea_Market?
> ![localhost_market(Nest Hub Max)](https://user-images.githubusercontent.com/90936639/180116263-f5d650ac-8853-405b-99e6-572d1f1f0863.png)

 > Es un E-Comerce robusto construído con Flask, Postgresql y SQLAlchemy.<br>
 > Donde podra comprar y vender arte digital de artistas independientes.

## 📂 Link para Clonar Repositorio
```
git clone https://github.com/Fer-Bar/Guacatea_Market.git
```

## Instrucciones de uso
#### Correrlo localmente:
1. Crea un entorno virtual:
- Windows:
```
py -m venv nombre-del-entorno
cd nombre-del-entorno/Scripts
activate
```
- Unix o Linux:
```
pip install virtualenv
virtualenv nombre-del-entorno
source venv/bin/activate
```
2. Ve al directorio llamado [web](web).
```
cd web
```
3. Instala las dependencias con:
```
pip install -r requirements.txt
```
4. Para correr la app localmente corre el archivo [run.py](web/run.py).
```
py run.py
```
- Asegurese de que la última linea del archivo run.py se vea así:
```
app.run(host='0.0.0.0', port=5000, debug=True)
```
5. En la consola usted puede crear las tablas con el comando:
```
flask create_db
```

#### Correrlo en docker:
Se require de tener instalado `docker` y `docker-compose`, para poder hacer uso de los servicios y probarlos solo se necesita ejecutar `docker-compose up` en la carpeta principal del proyecto, dentro del compose ya se encuenta configurada una base de datos, a la cual se puede acceder usando la cadena: `postgresql://guacatea:guacatea@db:5432/guacatea`, en dado caso de que se requieran conectar se puede acceder a la página `localhost:8888` ahí estara una interfaz web que permite acceder a la base de datos los accesos son: `user=guacatea`, `password=guacatea`, `host=db` y `db=market` si se requiere entrar desde la linea de comando solo es de usar como `host=localhost`.

## Correr los tests
```

python -m pytest -v

```

## 🏆 Integrantes
- Lino Fernando Barrientos Cárdenas
- Neimv Zephon Zatara Lyra
- Magno Martinez
