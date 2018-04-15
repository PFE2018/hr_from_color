import csv
import numpy as np

print('Data for ecg.csv')

dataECG = np.genfromtxt('ecg.csv', dtype=[('times','f8'), ('hr','f8')], comments='#', delimiter=',')
dataWebcam = np.genfromtxt('test.csv', dtype=[('times','f8'), ('hr','f8')], comments='#', delimiter=',')

meanWc = []
errorArray = []
meanArray = []
ecgArray = []
previousTime = 0
meanError = []

for indexEcg, ecg in enumerate(dataECG):
    timeEcg = ecg[0]
    valueEcg = ecg[1]
    ecgArray.append(valueEcg)

    if indexEcg == 0:
        pass

    for indexWc, webcamHr in enumerate(dataWebcam):
        timeWc = webcamHr[0]
        valueWc = webcamHr[1]

        if(timeWc < timeEcg) and (timeWc > previousTime):
            meanWc.append(valueWc)

        elif timeWc > timeEcg:
            break

    hr = np.mean(meanWc)
    error = hr - valueEcg
    errorArray.append(abs(error))
    previousTime = timeEcg
    meanError = np.mean(errorArray)


toWrite = zip(dataECG, dataWebcam, errorArray)

with open('ErrorOnGetPulse.csv', "w") as f:
    writer = csv.writer(f)
    for row in toWrite:
        writer.writerow(row)


    #output = np.column_stack(dataECG.flatten(), dataWebcam.flatten(), errorArray.flatten())
    #np.savetxt('ErrorOnGetPulse.csv',
    #           output,
    #           delimiter=",",
    #           header="dataECG, dataWebcam, error",
    #           comments="Hello")


    #np.savetxt('ErrorOnGetPulse.csv',
    #           zip(dataECG, dataWebcam, errorArray),
    #           delimiter=",",
    #           header="dataECG, dataWebcam, error",
    #           comments="Hello")

