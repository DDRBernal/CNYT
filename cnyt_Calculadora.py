from sys import stdin
import math
from math import atan

def restaC(tuplaA,tuplaB):
    if (type(tuplaA)==int):num=tuplaA;tuplaA=(num,0)
    if (type(tuplaB)==int):num=tuplaB;tuplaB=(num,0)    
    tuplaFinal=(tuplaA[0]-tuplaB[0],tuplaA[1]-tuplaB[1])
    return(tuplaFinal)
    
def sumaC(tuplaA,tuplaB):
    if (type(tuplaA)==int):num=tuplaA;tuplaA=(num,0)
    if (type(tuplaB)==int):num=tuplaB;tuplaB=(num,0)
    tuplaFinal=(tuplaA[0]+tuplaB[0],tuplaA[1]+tuplaB[1])
    return(tuplaFinal)

def multiplicacionC(tuplaA,tuplaB):
    if (type(tuplaA)==int):num=tuplaA;tuplaA=(num,0)
    if (type(tuplaB)==int):num=tuplaB;tuplaB=(num,0)
    tuplaFinal1=((tuplaA[0]*tuplaB[0]),-(tuplaA[1]*tuplaB[1]))
    tuplaFinal2=(tuplaA[0]*tuplaB[1]),(tuplaA[1]*tuplaB[0])
    return (tuplaFinal1[0]+tuplaFinal1[1],tuplaFinal2[0]+tuplaFinal2[1])
    

def divisionC(tuplaA,tuplaB):
    if (type(tuplaA)==int):num=tuplaA;tuplaA=(num,0)
    if (type(tuplaB)==int):num=tuplaB;tuplaB=(num,0)    
    valor1=(tuplaA[0]*tuplaB[0]) ##sin i
    valor2=((tuplaA[0]*-tuplaB[1])+(tuplaA[1]*tuplaB[0])) ## con i
    valor22=(tuplaA[1]*tuplaB[1]) ## con i**2
    tuplaF=(valor1,valor2,valor22)
    ##denomidador
    valor3=tuplaB[0]**2 ## sin i
    valor4=(tuplaB[1]**2) ##con i
    tuplaFinal=((tuplaF[0]+tuplaF[2])/(valor3+valor4),tuplaF[1]/(valor3+valor4))
    return(tuplaFinal)

def moduloC(tuplaA):
    if (type(tuplaA)==int):num=tuplaA;tuplaA=(num,0)    
    tuplaFinal=((tuplaA[0]**2)+(tuplaA[1]**2))**0.5
    return tuplaFinal

def conjugadoC(tuplaA):
    if (type(tuplaA)==int):num=tuplaA;tuplaA=(num,0)    
    tuplaFinal=(tuplaA[0],-tuplaA[1])
    return(tuplaFinal)

def polarC(tuplaA):
    if (type(tuplaA)==int):num=tuplaA;tuplaA=(num,0)    
    tupla1=((tuplaA[0]**2)+(tuplaA[1]**2))**0.5
    tuplaFinal=(tupla1,atan(tuplaA[1]/tuplaA[0]))
    return(tuplaFinal)

def cartesianoC(tuplaA):
    if (type(tuplaA)==int):num=tuplaA;tuplaA=(num,0)    
    tuplaFinal=(tuplaA[0]*math.cos(tuplaA[1]),tuplaA[0]*math.sin(tuplaA[1]))
    return(tuplaFinal)

def faseC(tuplaA):
    if (type(tuplaA)==int):num=tuplaA;tuplaA=(num,0)    
    tuplaFinal=(math.atan(tuplaA[1]/tuplaA[0]))
    return(tuplaFinal)

#---------------------------------- calculadora matriz ----------------------------------------#


def multiplicaEscalar(tupla,c):
    tuplaF = (tupla[0]*c,tupla[1]*c)
    return tuplaF

def sumaV(vectorA,vectorB):
    vectorR=[]
    for i in range(len(vectorA)):
        vectorR.append(sumaC(vectorA[0],vectorB[0]))

    return vectorR

def inversaV(vector):
    vectorF=[]
    for i in range(len(vector)): vectorF.append(vector[i][0],vector[i][1])
    

def sumaM(matrizA,matrizB):
    matrizR=[]
    for q in range(len(matrizA)):
        matrizR.append([])
        for k in range(len(matrizA[0])):matrizR[q].append(0)
    for i in range(0,len(matrizA)):
        for j in range(len(matrizA[0])):matrizR[i][j]=sumaC(matrizA[i][j],matrizB[i][j])
            
    return matrizR


def restaM(matrizA,matrizB):
    matrizR=[]
    for q in range(len(matrizA)):
        matrizR.append([])
        for k in range(len(matrizA[0])):matrizR[q].append(0)
    for i in range(0,len(matrizA)):
        for j in range(len(matrizA[0])):matrizR[i][j]=restaC(matrizA[i][j],matrizB[i][j])
    return matrizR


def multiplicacionM(matrizA,matrizB):
    if (len(matrizB)==1 and (len(matrizB[0])==len(matrizA[0]))):
        return multiplicacionMV(matrizA,matrizB[0])
    matrizR=[]
    if (len(matrizA[0])==len(matrizB)):
        for i in range(0,len(matrizA)):
            matrizR.append([]);
            suma=0
            for j in range(0,len(matrizA[i])):
                for k in range(0,len(matrizB)):
                    suma=sumaC(suma,multiplicacionC(matrizA[i][k],matrizB[k][j]))
                matrizR[i].append(suma)
                suma=0
    if (matrizR==[]):print("El numero de columnas de A debe ser igual al numero de filas de B")
    return matrizR

def multiplicacionMV(matriz,vector):
    matrizR=[]
    for i in range(0,len(matriz)):
        suma=0
        for j in range(0,len(matriz[i])):
            suma= sumaC(suma,multiplicacionC(matriz[i][j],vector[j]))
        matrizR.append(suma)
        suma=0
    return matrizR

def inversaM(matriz):
    matrizR=[]
    for i in range(0,len(matriz)):
        matrizR.append([int(i) for i in range(0,len(matriz[0]))]);
        for j in range(0,len(matriz[0])):
            matrizR[i][j]=matriz[i][j]*-1
                       
    return matrizR

def escalarM(matriz,c):
    matrizR=[]
    for i in range(0,len(matriz)):
        matrizR.append([int(i) for i in range(0,len(matriz[0]))]);
        for j in range(0,len(matriz[0])):
            matrizR[i][j]= c*matriz[i][j]
    return matriz

def transpuestaM(matriz):
    matrizR=[]
    for i in range(0,len(matriz)):
            matrizR.append([])
            for j in range(0,len(matriz[0])):
                matrizR[i].append(matriz[j][i])
    return matrizR
    
def conjugadaM(matriz):
    matrizR=[]
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            tuplaA=matriz[i][j]
            if (type(tuplaA)==int):num=tuplaA;tuplaA=(num,0)
            if (tuplaA[0]>=0 and tuplaA[1]>=0): tuplaA=(tuplaA[0],-tuplaA[1])
            if (tuplaA[0]<=0 and tuplaA[1]>=0): tuplaA=(tuplaA[0],-tuplaA[1])
            if (tuplaA[0]>=0 and tuplaA[1]<=0): tuplaA=(tuplaA[0],abs(tuplaA[1]))
            matriz[i][j]=tuplaA
    return matriz            

def adjuntaM(matriz):
    matrizR=[]
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            adj(i,j,matriz,matrizR)
            
    for i in range(0,len(matrizR)):
        if (i%3==0 and i!=0):
            print()
        print(matrizR[i],end=' ')
        

            
def adj(a,b,matriz,matrizR):
    vector=[]
    for i in range(0,len(matriz)):
        contante=-1
        for j in range(0,len(matriz[i])):
            if (a!=i and b!=j):
                vector.append(matriz[i][j])
                if (len(vector)==4):
                    matrizR.append(determinante(vector,contante**(a+b)))
                    vector=[]

def determinante(vector,constante):
    return (constante*((vector[0]*vector[3])-(vector[1]*vector[2])))
                
            
def accionM():
    print("Ingrese una operacion")
    print('''
////// suma //////
////// resta //////
////// multiplicacion //////
////// division //////
''')



def m():
    matrizR=[]
    k=0
    matrizA=[[(1,0),(1,0)],[(1,0),(0,0)]]
    matrizB=[[(1,0),(0,0)],[(0,0),(1,0)]]
    while (matrizB[0][0]<(1000,0)):
        print(matrizB)
        for i in range(0,len(matrizA)):
            matrizR.append([]);
            suma=0
            for j in range(0,len(matrizA[i])):
                for k in range(0,len(matrizB)):
                    suma=sumaC(suma,multiplicacionC(matrizB[k][j],matrizA[i][k]))
                matrizR[i].append(suma)
                suma=0
        matrizB=matrizR
        matrizR=[]
        k+=1
    print(k)

    
