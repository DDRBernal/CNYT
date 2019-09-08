import unittest
import cnyt_Calculadora as cal

class test_calculadora(unittest.TestCase):
    def test_modulo(self):
        self.assertEqual(cal.sumaC((1,1),(2,2)),(3,3))
        self.assertEqual(cal.restaC((1,1),(2,2)),(-1,-1))
        self.assertEqual(cal.multiplicacionC((1,1),(2,2)),(0,4))
        self.assertEqual(cal.divisionC((1,1),(2,2)),(0.5,0.0))
        self.assertEqual(cal.conjugadoC((2,2)),(2,-2))
        self.assertEqual(cal.polarC((1,0)),(1.0,0.0))
        self.assertEqual(cal.cartesianoC((1,0)),(1.0,0.0))
        self.assertEqual(cal.faseC((1,0)),0.0)
        #------Matrices------#
        self.assertEqual(cal.multiplicacionEV([2,3],1),[2,3])
        self.assertEqual(cal.sumaV([1,2],[2,3]),[(3,0),(3,0)])
        self.assertEqual(cal.inversaV([5,5]),[-5,-5])
        self.assertEqual(cal.sumaM([[1,2,3],[2,3,4]],[[1,2,3],[2,3,4]]),[[(2, 0), (4, 0), (6, 0)], [(4, 0), (6, 0), (8, 0)]])
        self.assertEqual(cal.restaM([[1,2,3],[2,3,4]],[[1,2,3],[2,3,4]]),[[(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)]])
        self.assertEqual(cal.multiplicacionM([[1,2],[2,3]],[[2,3],[2,4]]),[[(6, 0), (11, 0)], [(10, 0), (18, 0)]])
        self.assertEqual(cal.multiplicacionMV([[1,1],[2,3]],[1,1]),[(2, 0), (5, 0)])
        self.assertEqual(cal.inversaM([[2,3,4]]),[[-2,-3,-4]])
        self.assertEqual(cal.transpuestaM([[1,2],[2,3]]),[[1, 2], [2, 3]])
        self.assertEqual(cal.multiplicacionME([[1,1,1]],3),[[3,3,3]])
        self.assertEqual(cal.conjugadaM([[1,1,1]]),[[1,1,1]])
        self.assertEqual(cal.adjuntaM([[1,2,3]]),[[1],[2],[3]])
        self.assertEqual(cal.normaM([[1,2],[1,2],[1,2]]),3.872983346207417)
        self.assertEqual(cal.checkHermitian([[1,(0,1)],[(0,-1),1]]),True)
        self.assertEqual(cal.checkUnitaria([[1,0],[0,1]]),True)
        self.assertEqual(cal.productoTensor([[1,2],[4,5],[9,9]],[[5,5,5],[4,3,2]]),[[(5, 0), (5, 0), (5, 0), (10, 0), (10, 0), (10, 0)], [(4, 0), (3, 0), (2, 0), (8, 0), (6, 0), (4, 0)], [(20, 0), (20, 0), (20, 0), (25, 0), (25, 0), (25, 0)], [(16, 0), (12, 0), (8, 0), (20, 0), (15, 0), (10, 0)], [(45, 0), (45, 0), (45, 0), (45, 0), (45, 0), (45, 0)], [(36, 0), (27, 0), (18, 0), (36, 0), (27, 0), (18, 0)]])

if __name__ == "__main__":
    unittest.main()
