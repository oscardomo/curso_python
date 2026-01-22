# Gestor de Tareas (Flask)

Esqueleto mínimo de una aplicación Flask.

## Persistencia (JSON)

Las tareas se guardan automáticamente en `tareas.json` tras cada cambio (agregar/completar).  
Al reiniciar la app, se vuelven a cargar desde ese archivo.

## Requisitos

- Python 3.x

## Ejecutar (Windows + PowerShell)

Activar el entorno virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

O instalar dependencias si no las tuvieras:

```powershell
pip install -r requirements.txt
```

### Opción A: `flask run` (recomendado en desarrollo)

```powershell
$env:FLASK_APP = "app:create_app"
$env:FLASK_ENV = "development"
flask run
```

Abre `http://127.0.0.1:5000/`.

### Opción B: ejecutar directo

```powershell
python .\app.py
```

## Qué hace

- `GET /`: lista tareas (incompletas primero) + formulario para añadir.
- `POST /agregar`: agrega tarea y redirige a `/`.
- `GET /completar/<id>`: marca como hecha y redirige a `/`.
