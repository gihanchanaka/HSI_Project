import scipy as sp
import scipy.io as io
import numpy as np
 
def processFile(fileName,outputFileName):
    unwantedCoulmns=[]
 
    #Put the code to append the unwated columns here :-)
    for i in range(0,6):
        unwantedCoulmns.append(i)
    for i in range(57,76):
        unwantedCoulmns.append(i)
    for i in range(224,241):
        unwantedCoulmns.append(i)
 
    mat = io.loadmat(fileName)['B']
    for i in range(len(unwantedCoulmns)):
        mat=np.delete(mat,unwantedCoulmns[i],axis=1)
 
    np.savetxt(outputFileName,mat)
 
 
def processFileSet(inputFilePrefix,inputFileSuffix,outputFilePrefix,outputFileSuffix,startNo,endNo):
    for i in range(startNo,endNo+1):
        inputFileName=inputFilePrefix+str(i)+inputFileSuffix
        outputFileName=outputFilePrefix+str(i)+outputFileSuffix
        processFile(inputFileName,outputFileName)
 
 
def runFileUnwantedColumnRemoval():
    processFileSet('data/Row_','.mat','data/Processed_Row_','.txt',5627,5627)
 
#MAIN()
 
runFileUnwantedColumnRemoval()
 
ar=np.loadtxt('data/Processed_Row_5627.txt')
print(np.shape(ar))