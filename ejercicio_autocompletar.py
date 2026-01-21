# Determina si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Solo comprobar hasta √n; si hay divisor > √n, existe uno < √n
    # Solo impares: los pares ya se descartan con n % 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import unittest

    class TestEsPrimo(unittest.TestCase):
        def test_no_primos_menores_iguales_1(self):
            self.assertFalse(es_primo(0))
            self.assertFalse(es_primo(1))
            self.assertFalse(es_primo(-5))

        def test_dos_es_primo(self):
            self.assertTrue(es_primo(2))

        def test_pares_mayores_que_2_no_son_primos(self):
            self.assertFalse(es_primo(4))
            self.assertFalse(es_primo(6))
            self.assertFalse(es_primo(100))

        def test_primos_impares(self):
            for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 97):
                self.assertTrue(es_primo(p), f"{p} debería ser primo")

        def test_compuestos_impares(self):
            for c in (9, 15, 21, 25, 27, 35, 49, 77):
                self.assertFalse(es_primo(c), f"{c} no debería ser primo")

        def test_numero_grande_primo(self):
            self.assertTrue(es_primo(97))
            self.assertTrue(es_primo(541))

    unittest.main()