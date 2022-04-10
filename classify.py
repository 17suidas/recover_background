from PIL import Image
import os
import shutil
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

file_dir = 'E:/大创/test/Necaptcha'
new_dir = 'E:/大创/test/classified_Necaptcha/Necaptcha'
image_filenames = [os.path.join(file_dir, x) for x in os.listdir(file_dir)] #get all url
lenth = len(image_filenames)


def SortCaptcha(k): #start with pic[0], compare all, move to k
    flag = 0
    sorted_dir = new_dir + str(k)
    os.mkdir(sorted_dir)
    imagine = Image.open(image_filenames[0])
    # imagine.show()
    width, height = imagine.size
    listR = []
    listG = []
    listB = []
    for x in range(width):
        for y in range(height):
            r, g, b = imagine.getpixel((x, y))
            listR.append(r)
            listG.append(g)
            listB.append(b)

    for i in range(1, lenth):
        print(i)
        comImagine = Image.open(image_filenames[i])
        comWidth, comHeight = comImagine.size
        if comWidth != width or comHeight != height:
            continue
        comListR = []
        comListG = []
        comListB = []
        for x in range(width):
            for y in range(height):
                r, g, b = comImagine.getpixel((x, y))
                comListR.append(r)
                comListG.append(g)
                comListB.append(b)

        cnt = 0
        pickNum = 0
        for x in range(0, width * height, 5):
            pickNum += 1
            if abs(listR[x] - comListR[x]) <= 10 and abs(listG[x] - comListG[x]) <= 10 and abs(listB[x] - comListB[x]) <= 10:
                cnt += 1
        if cnt / pickNum > 0.6:
            shutil.move(image_filenames[i], sorted_dir)
            flag = 1

    shutil.move(image_filenames[0], sorted_dir)
    return flag


if __name__ == '__main__':
    runTimes = 0
    repeat = 0
    while lenth > 0:
        runTimes += 1
        print(runTimes)
        SortCaptcha(runTimes)
        image_filenames = [os.path.join(file_dir, x) for x in os.listdir(file_dir)]  # get all url
        lenth = len(image_filenames)