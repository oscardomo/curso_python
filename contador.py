"""
Programa para contar palabras en un archivo de texto.
"""

from collections import Counter


def leer_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo de texto.
    
    Args:
        ruta_archivo: Ruta del archivo a leer.
        
    Returns:
        El texto contenido en el archivo.
        
    Raises:
        FileNotFoundError: Si el archivo no existe.
    """
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return archivo.read()


def separar_en_palabras(contenido: str) -> list[str]:
    """
    Separa un texto en una lista de palabras.
    
    Args:
        contenido: Texto a dividir.
        
    Returns:
        Lista de palabras (segmentos separados por espacios).
    """
    return contenido.split()


def contar_palabras(palabras: list[str]) -> int:
    """
    Cuenta el número total de palabras en una lista.
    
    Args:
        palabras: Lista de palabras.
        
    Returns:
        Número total de palabras.
    """
    return len(palabras)


def palabras_mas_frecuentes(palabras: list[str], n: int = 10) -> list[tuple[str, int]]:
    """
    Obtiene las n palabras más frecuentes y su conteo.

    Args:
        palabras: Lista de palabras.
        n: Cantidad de palabras a devolver (por defecto 10).

    Returns:
        Lista de tuplas (palabra, conteo) ordenadas de mayor a menor frecuencia.
    """
    return Counter(palabras).most_common(n)


def pedir_ruta_archivo() -> str:
    """
    Pide al usuario la ruta de un archivo de texto y la devuelve.

    Repite el prompt hasta que se proporcione una ruta no vacía.

    Returns:
        Ruta del archivo introducida por el usuario.
    """
    while True:
        ruta = input("Ingresa la ruta del archivo de texto: ").strip()
        if ruta:
            return ruta
        print("No ingresaste ninguna ruta. Intenta de nuevo.\n")


def main():
    """
    Pide una ruta de archivo, cuenta las palabras y muestra el total
    y las 10 más frecuentes. Gestiona FileNotFoundError y otros errores.
    """
    ruta = pedir_ruta_archivo()
    
    try:
        contenido = leer_archivo(ruta)
        palabras = separar_en_palabras(contenido)
        total = contar_palabras(palabras)
        print(f"\nNúmero total de palabras: {total}")

        top_10 = palabras_mas_frecuentes(palabras, 10)
        print("\nLas 10 palabras más frecuentes:")
        for i, (palabra, conteo) in enumerate(top_10, 1):
            print(f"  {i:2}. {palabra}: {conteo}")
    except FileNotFoundError:
        print(f"\nError: No se encontró el archivo '{ruta}'.")
    except Exception as e:
        print(f"\nError al leer el archivo: {e}")


if __name__ == "__main__":
    main()
