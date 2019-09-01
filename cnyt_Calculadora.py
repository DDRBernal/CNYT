from sys import stdin
import math
from math import atan
print('''
/////// numeros_complejos ///////

restaC(tuplaA,tuplaB)
sumaC(tuplaA,tuplaB)
multiplicacionC(tuplaA,tuplaB)
divisionC(tuplaA,tuplaB)
moduloC(tuplaA)
conjugadoC(tuplaA)
polarC(tuplaA)
cartesianoC(tuplaA)
faseC(tuplaA)
////// matrices ///////

multiplicacionEscalar(tupla,c)
sumaV(vectorA,vectorB)
inversaV(vector)
sumaM(matrizA,matrizB)
restaM(matrizA,matrizB)
multiplicacionM(matrizA,matrizB)
multiplicacionMV(matriz,vector)
inversaM(matriz)
multiplicacionME(matriz,c)
transpuestaM(matriz)
conjugadaM(matriz)
adjuntaM(matriz)
distanciaM(matrizA,matrizB)
normaM(matriz)
checkHermitian(matriz)
checkUnitaria(matriz)
productoTensor(matrizA,matrizB)
accionM(matriz,vector)
    ''')
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


def multiplicacionEscalar(tupla,c):
    tuplaF = (tupla[0]*c,tupla[1]*c)
    return tuplaF

def sumaV(vectorA,vectorB):
    vectorR=[]
    for i in range(len(vectorA)):
        vectorR.append(sumaC(vectorA[0],vectorB[0]))
    return vectorR

def inversaV(vector):
    tuplaF=(-tupla[0],-tupla[1])
    return tuplaF

def sumaM(matrizA,matrizB):
    matrizR=[]
    if ((len(matrizA)==len(matrizB)) and (len(matrizA[0])==len(matrizB[0]))):            
        for q in range(len(matrizA)):
            matrizR.append([])
            for k in range(len(matrizA[0])):matrizR[q].append(0)
        for i in range(0,len(matrizA)):
            for j in range(len(matrizA[0])):matrizR[i][j]=sumaC(matrizA[i][j],matrizB[i][j])
            
    return matrizR

def restaM(matrizA,matrizB):
    matrizR=[]
    if ((len(matrizA)==len(matrizB)) and (len(matrizA[0])==len(matrizB[0]))):
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
    posA=0
    posB=0
    if (len(matrizA[0])==len(matrizB)):
        for algo in range(len(matrizA)):
            matrizR.append([i for i in range(len(matrizB[0]))])
        while (posA<len(matrizA)):
            for i in range(0,len(matrizA)):
                suma=0
                for j in range(len(matrizB)):
                    suma=sumaC(suma,multiplicacionC(matrizA[posA][j],matrizB[j][posB]))
                matrizR[posA][posB]=suma
                suma=0
                posB+=1
            posA+=1
            posB=0
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

def multiplicacionME(matriz,c):
    matrizR=[]
    for i in range(0,len(matriz)):
        matrizR.append([int(i) for i in range(0,len(matriz[0]))]);
        for j in range(0,len(matriz[0])):
            matrizR[i][j]= c*matriz[i][j]
    return matriz

def transpuestaM(matriz):
    matrizR=[]
    posi=0
    for i in range(0,len(matriz[0])):
            matrizR.append([])
            for j in range(0,len(matriz)):
                matrizR[i].append(matriz[j][posi])
            posi+=1
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
    global matrizR
    matrizR=[]
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            adj(i,j,matriz)
            
    for i in range(0,len(matrizR)):
        if (i%3==0 and i!=0):
            print()
        print(matrizR[i],end=' ')
                    
def adj(a,b,matriz):
    global matrizR
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
                
def distanciaM(matrizA,matrizB):
    suma=-float("inf")
    if ((len(matrizA)==len(matrizB))and(len(matrizA[0])==len(matrizB[0]))):
        matrizC=restaM(matrizA,matrizB)
        matrizCC=conjugadaM(transpuestaM(matrizC))
        matrizS=multiplicacionM(matrizC,matrizCC)
        for i in range(len(matrizS)):
            for j in range(matrizS[0]):
                suma+ matrizS[i][j]
    if (suma!=-float("inf")):return suma
    else: print("Las matrices deben tener el mismo tamaño")
        
    
def normaM(matriz):
    suma=0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if (type(matriz[i][j])!=int):
                tupla = matriz[i][j]
                tupla2 = (matriz[i][j][0],-matriz[i][j][1])
                tuplaF = (multiplicacionC(tupla,tupla2))
                suma+= (tuplaF[0]**1)
            else:
                suma+= (matriz[i][j]**2)
    return (suma**0.5)


def checkHermitian(matriz):
    matrizR=transpuestaM(conjugadaM(matriz))
    return(matriz==matrizR)

def checkUnitaria(matriz):
    if ((len(matrizA)==len(matrizA[0]))):
        pass


def productoTensor(matrizA,matrizB):
    matrizR=[]
    indice=indice2=indice3=0
    m=[]
    mm=[]
    for a in range(len(matrizB)*2):
        matrizR.append([])
    for i in range(len(matrizB)):
        for j in range(len(matrizA)):
            for k in range(len(matrizA[0])):
                while (indice2<len(matrizB[0])):
                    if (len(matrizR[indice3])==((len(matrizB[0])*2))): indice3+=1
                    matrizR[indice3].append(matrizA[j][k]*matrizB[i][indice2])
                    indice2+=1
                indice2=0
        indice+=1
    for algo in range(len(matrizR)):
        if (algo%2==0):m.append(matrizR[algo]);
        else: mm.append(matrizR[algo])
    return m+mm 

    
def accionM(matriz,vector):
    print("Ingrese una operacion")
    print('');print ('////// suma //////');print ('////// resta //////')
    print ('////// multiplicacion //////')
    print ('////// division //////');print()
    a=input()
    a=a.lower().strip()
    print(a)
    
    if (a=='*'): return multiplicacionMV(matriz,vector)
    
    
          




    
