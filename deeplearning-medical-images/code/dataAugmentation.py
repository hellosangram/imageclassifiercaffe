from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import os

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

baseFolder = '/home/sangram/Desktop/Challenge/'
source =  baseFolder + 'trainImages'
destination =  baseFolder + 'trainImagesAugmented'
for fileName in os.listdir(source):
    category = fileName.split('.')[0]
    img = load_img(source+ '/' + fileName)  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

    i = 0
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir=destination, save_prefix=category, save_format='jpg'):
        i += 1
        if i > 200:
            break  # otherwise the generator would loop indefinitely