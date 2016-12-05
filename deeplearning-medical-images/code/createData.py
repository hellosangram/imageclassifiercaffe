import os
from shutil import copyfile

baseFolder = '/home/sangram/Desktop/Challenge/train'

source =  baseFolder + 'test1'
for fileName in os.listdir(source):
    category = fileName.split('_')[2]
    destination = baseFolder + 'val' #+ category
    copyfile(source + '/' + fileName, destination + '/' + category + '.' + fileName.split('_')[1] + '.jpg')
