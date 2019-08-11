import unittest
import cnyt_Calculadora as cal

class test_calculadora(unittest.TestCase):
    def test_modulo(self):
        self.assertEqual(cal.sumaC((1,1),(2,2)),(3,3))
        self.assertEqual(cal.restaC((1,1),(2,2)),(-1,-1))
        self.assertEqual(cal.multiplicacionC((1,1),(2,2)),(3,4))
        self.assertEqual(cal.divisionC((1,1),(2,2)),(0.5,0.0))
        self.assertEqual(cal.conjugadoC((2,2)),(2,-2))
        self.assertEqual(cal.polarC((1,0)),(1.0,0.0))
        self.assertEqual(cal.cartesianoC((1,0)),(1.0,0.0))
        self.assertEqual(cal.faseC((1,0)),0.0)


if __name__ == "__main__":
    unittest.main()
