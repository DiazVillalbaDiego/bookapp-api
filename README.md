# BookApp API

API de práctica para el caso BookApp. Hecha con FastAPI; los datos viven en memoria (`app/data.py`).

## Cómo correrla (PowerShell en Windows)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

En Mac: `source .venv/bin/activate` en lugar de la línea del `Activate.ps1`.

- Swagger (la documentación, como el `api-docs` del examen): http://localhost:8000/docs
- Listado: `GET http://localhost:8000/api/books`
- Detalle: `GET http://localhost:8000/api/books/1`

## Conectar la app Android

- Emulador: `baseUrl` = `http://10.0.2.2:8000/api/` (10.0.2.2 es el "localhost" de tu PC visto desde el emulador).
- Celular real: usa la IP de tu PC en la red wifi, por ejemplo `http://192.168.1.20:8000/api/`.
- Como es `http` y no `https`, agrega en el `AndroidManifest.xml`, dentro de `<application>`:
  `android:usesCleartextTraffic="true"`.
- Retrofit: `@GET("books")` y `@GET("books/{id}")`.

## Forma del JSON

Un libro: `id`, `title`, `author`, `year`, `publisher`, `genre`, `synopsis`, `rating`, `image_url`.
`GET /api/books` devuelve un arreglo directo de libros, sin objeto envolvente.
