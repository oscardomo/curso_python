from __future__ import annotations

import json
from pathlib import Path

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Datos (en memoria + persistidos en JSON)
tareas: list[dict] = []
siguiente_id = 1
ARCHIVO_DATOS = Path("tareas.json")


def guardar_datos() -> None:
    data = {"siguiente_id": siguiente_id, "tareas": tareas}
    # Escritura atómica simple (evita archivos corruptos si se corta a mitad)
    tmp = ARCHIVO_DATOS.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(ARCHIVO_DATOS)


def cargar_datos() -> None:
    global siguiente_id, tareas
    try:
        data = json.loads(ARCHIVO_DATOS.read_text(encoding="utf-8"))
        tareas = data.get("tareas", [])
        siguiente_id = int(data.get("siguiente_id", 1))
    except FileNotFoundError:
        pass
    except (json.JSONDecodeError, ValueError, TypeError):
        # Si el JSON está corrupto o tiene formato inesperado, arrancamos vacío
        tareas = []
        siguiente_id = 1


def agregar_tarea(texto: str) -> None:
    global siguiente_id
    tareas.append({"id": siguiente_id, "texto": texto, "hecho": False})
    siguiente_id += 1
    guardar_datos()


def completar_tarea(id: int) -> None:
    for tarea in tareas:
        if tarea["id"] == id:
            tarea["hecho"] = True
            break
    guardar_datos()


# Cargar datos antes de definir rutas / manejar requests
cargar_datos()

@app.route("/")
def index():
    # Ordenar tareas: incompletas primero, luego completadas
    tareas_ordenadas = sorted(tareas, key=lambda t: t["hecho"])
    return render_template("index.html", tareas=tareas_ordenadas)


@app.route("/agregar", methods=["POST"])
def agregar():
    texto_tarea = (request.form.get("texto_tarea") or "").strip()
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect("/")


@app.route("/completar/<int:id>")
def completar(id: int):
    completar_tarea(id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)