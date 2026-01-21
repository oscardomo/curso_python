# analisis.py: lee y trabaja con datos.csv

import csv
import statistics

import matplotlib.pyplot as plt

with open("datos.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    datos = list(reader)

# Convertir a números (las claves son los nombres de las columnas: x, y)
for fila in datos:
    fila["x"] = float(fila["x"])
    fila["y"] = float(fila["y"])

print(f"Filas leídas: {len(datos)}")
print(f"Columnas: {list(datos[0].keys())}")
print("\nPrimeras 5 filas:")
for fila in datos[:5]:
    print(f"  x={fila['x']}, y={fila['y']}")

# Estadísticas por columna
columnas = ["x", "y"]
print("\n--- Estadísticas por columna ---")
for col in columnas:
    valores = [fila[col] for fila in datos]
    media = statistics.mean(valores)
    mediana = statistics.median(valores)
    desv = statistics.stdev(valores)
    print(f"\n{col}:")
    print(f"  Media:              {media:.4f}")
    print(f"  Mediana:            {mediana:.4f}")
    print(f"  Desv. estándar:     {desv:.4f}")

# Gráfica de dispersión: x vs y
x_vals = [fila["x"] for fila in datos]
y_vals = [fila["y"] for fila in datos]

plt.figure(figsize=(7, 5))
plt.scatter(x_vals, y_vals, c="steelblue", edgecolors="navy", alpha=0.8, s=50)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Dispersión: y vs x")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
