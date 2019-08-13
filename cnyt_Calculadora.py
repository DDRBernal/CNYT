from sys import stdin
import math
from math import atan

def restaC(tuplaA,tuplaB):
    tuplaFinal=(tuplaA[0]-tuplaB[0],tuplaA[1]-tuplaB[1])
    return(tuplaFinal)
    
def sumaC(tuplaA,tuplaB):
    tuplaFinal=(tuplaA[0]+tuplaB[0],tuplaA[1]+tuplaB[1])
    return(tuplaFinal)

def multiplicacionC(tuplaA,tuplaB):
    tuplaFinal=(tuplaA[0]*tuplaB[0]-tuplaA[1]+tuplaB[1],tuplaA[0]*tuplaB[1]+tuplaA[1]*tuplaB[0])
    return(tuplaFinal)

def divisionC(tuplaA,tuplaB):
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
    tuplaFinal=((tuplaA[0]**2)+(tuplaA[1]**2))**0.5
    return tuplaFinal

def conjugadoC(tuplaA):
    tuplaFinal=(tuplaA[0],-tuplaA[1])
    return(tuplaFinal)

def polarC(tuplaA):
    tupla1=((tuplaA[0]**2)+(tuplaA[1]**2))**0.5
    tuplaFinal=(tupla1,atan(tuplaA[1]/tuplaA[0]))
    return(tuplaFinal)

def cartesianoC(tuplaA):
    tuplaFinal=(tuplaA[0]*math.cos(tuplaA[1]),tuplaA[0]*math.sin(tuplaA[1]))
    return(tuplaFinal)

def faseC(tuplaA):
    tuplaFinal=(math.atan(tuplaA[1]/tuplaA[0]))
    return(tuplaFinal)

#---------------------------- calculadora matriz ----------------------------------------#


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
    print(vector)
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
    matrizR=[]
    if (len(matrizA)==len(matrizB[0])):
        for l in range(len(matrizB)):
            matrizR.append([])
            for k in range(len(matrizB[0])):
                matrizR[l].append(0)
        
        for i in range(len(matrizA)):
            for j in range(len(matrizB[0])):
                matrizR[j][i]=matrizA[j][i]*matrizB[i][j]

    
    return matrizR





