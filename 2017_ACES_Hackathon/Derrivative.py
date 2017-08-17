def differenciate(M,wavelengths):
    dM=[[[0 for z in range(len(M[0][0])-1)] for x in range(len(M[0])) for y in range(len(M))]]
    wavelengthsNew=[0 for z in range(len(M[0][0]))]

    for z in range(len(M[0][0])):
        wavelengthsNew[z]=(wavelengths[z+1]+wavelengths[z])/2

    for y in range(len(M)):
        for x in range(len(M[0])):
            for z in range(len(M[0][0])):
                dM[y][x][z]=(M[y][x][z+1]-M[y][x][z])/(wavelengths[z+1]-wavelengths[z])

    return dM,wavelengthsNew

def findSpikes(M,wavelengths,interestedBands):
    matching=[[0 for y in range(len(M))] for x in range(M[0])]
    dM,wavelengthsNew=differenciate(M,wavelengths)
    for y in range(len(M)):
        for x in range(len(M[0])):

            dM_avg=sum(abs(dM[y][x]))/len(dM[y][x])
            interestedBandsDerrivativesSum=0
            interestedBandsDerrivativesSum_count=0

            for w in range(len(wavelengthsNew)):
                interested=0
                for i in range(len(interestedBands)):
                    if wavelengthsNew[w]<interestedBands[i][1] and wavelengthsNew[w]<interestedBands[i][0]:
                        interested=1
                if interested==1:
                    interestedBandsDerrivativesSum+=abs(dM[y][x][w])
                    interestedBandsDerrivativesSum_count+=1

            interestedBandsDerrivativesAverage=interestedBandsDerrivativesSum/interestedBandsDerrivativesSum_count
            matching[y][x]= interestedBandsDerrivativesAverage / 3*dM_avg

    return matching

# interestedBands= [[bandOneLowerEnd,bandOneUpperEnd],[bandTwoLowerEnd,bandTwoUpperEnd]]
interestedBands=[]

