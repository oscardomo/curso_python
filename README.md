# Curso Python

Repositorio con ejercicios y programas en Python: calculadora, contador de palabras, análisis de datos con gráficas, FizzBuzz, factorial, números primos y más.

---

## Requisitos

- **Python 3.x** (se recomienda 3.9 o superior).
- Las dependencias externas están en `requirements.txt`; en este proyecto se usa **matplotlib** para las gráficas de `analisis.py`.

---

## Instalación

1. Clona o descarga este repositorio.
2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate    # Windows
   # source venv/bin/activate   # Linux/macOS
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## Instrucciones de uso

Cada script se ejecuta con:

```bash
python nombre_del_archivo.py
```

### Contenido del proyecto

| Archivo | Descripción |
|---------|-------------|
| `calculadora.py` | Calculadora interactiva (suma, resta, multiplicación, división). Escribe `salir` para terminar. |
| `contador.py` | Cuenta palabras en un archivo de texto y muestra las 10 más frecuentes. Pide la ruta del archivo al ejecutar. |
| `analisis.py` | Lee `datos.csv`, calcula estadísticas (media, mediana, desviación estándar) y dibuja un gráfico de dispersión (x vs y). |
| `fizzbuzz.py` | Imprime Fizz, Buzz o FizzBuzz para los números del 1 al 50 según las reglas clásicas. |
| `prueba.py` | Calcula el factorial de un número (ejemplo: factorial de 5). |
| `ejercicio_autocompletar.py` | Función `es_primo(n)` y pruebas con `unittest`. Ejecutar: `python ejercicio_autocompletar.py` para lanzar los tests. |

### Datos

- `datos.csv`: archivo con columnas `x` e `y` usado por `analisis.py`. Debe estar en la misma carpeta que el script.

---

## Autor

Proyecto de curso de Python. Puedes indicar aquí tu nombre o enlace a tu perfil.

---

## Licencia

Uso educativo. Ajusta la licencia según prefieras.
