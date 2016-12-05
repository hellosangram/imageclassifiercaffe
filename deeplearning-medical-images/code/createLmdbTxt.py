import os

dir = '/home/sangram/deepLearning/deeplearning-medical-images/input/val'
generateTxtFile = open('/home/sangram/deepLearning/deeplearning-medical-images/input/val.txt','a')
for fileName in os.listdir(dir):
    if 'CH' == fileName.split('.')[0]:
        label = 0
    elif 'NR' == fileName.split('.')[0]:
        label = 1
    elif 'VA' == fileName.split('.')[0]:
        label = 2
    elif 'VACH' == fileName.split('.')[0]:
        label = 3
    generateTxtFile.write(str(fileName) + ' ' + str(label) + '\n')
    generateTxtFile.flush()
generateTxtFile.close()