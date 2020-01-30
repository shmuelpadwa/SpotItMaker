from PIL import Image
import random
import glob
import os
image_list = []
for filename in glob.glob(r'C:\Users\Shmuel\Downloads\256logos/*'):
    im=Image.open(filename)
    image_list.append(im)
print(len(image_list))
y = len(image_list)

if y == 7: # 7 = 2 * 2 + 2 + 1
    math = [
        [0, 1, 4],
        [2, 3, 4],
        [0, 2, 5],
        [1, 3, 5],
        [0, 3, 6],
        [1, 2, 6],
        [4, 5, 6]
            ]
elif y == 13: # 13 = 3 * 3 + 3 + 1
    math = [
            [0, 1, 2, 9],
            [9, 3, 4, 5],
            [8, 9, 6, 7],
            [0, 10, 3, 6],
            [1, 10, 4, 7],
            [8, 2, 10, 5],
            [0, 8, 11, 4],
            [1, 11, 5, 6],
            [11, 2, 3, 7],
            [0, 12, 5, 7],
            [8, 1, 3, 12],
            [12, 2, 4, 6],
            [9, 10, 11, 12]
                ]
elif y == 31: # 31 = 5 * 5 + 5 + 1
    math = [
            [0, 1, 2, 3, 4, 25],
            [5, 6, 7, 8, 9, 25],
            [10, 11, 12, 13, 14, 25],
            [15, 16, 17, 18, 19, 25],
            [20, 21, 22, 23, 24, 25],
            [0, 5, 10, 15, 20, 26],
            [1, 6, 11, 16, 21, 26],
            [2, 7, 12, 17, 22, 26],
            [3, 8, 13, 18, 23, 26],
            [4, 9, 14, 19, 24, 26],
            [0, 6, 12, 18, 24, 27],
            [1, 7, 13, 19, 20, 27],
            [2, 8, 14, 15, 21, 27],
            [3, 9, 10, 16, 22, 27],
            [4, 5, 11, 17, 23, 27],
            [0, 7, 14, 16, 23, 28],
            [1, 8, 10, 17, 24, 28],
            [2, 9, 11, 18, 20, 28],
            [3, 5, 12, 19, 21, 28],
            [4, 6, 13, 15, 22, 28],
            [0, 8, 11, 19, 22, 29],
            [1, 9, 12, 15, 23, 29],
            [2, 5, 13, 16, 24, 29],
            [3, 6, 14, 17, 20, 29],
            [4, 7, 10, 18, 21, 29],
            [0, 9, 13, 17, 21, 30],
            [1, 5, 14, 18, 22, 30],
            [2, 6, 10, 19, 23, 30],
            [3, 7, 11, 15, 24, 30],
            [4, 8, 12, 16, 20, 30],
            [25, 26, 27, 28, 29, 30]
                ]
elif y == 57: # 57 = 7 * 7 + 7 + 1
    
    math = [
            [0, 1, 2, 3, 4, 5, 6, 49],
            [7, 8, 9, 10, 11, 12, 13, 49],
            [49, 14, 15, 16, 17, 18, 19, 20],
            [49, 21, 22, 23, 24, 25, 26, 27],
            [32, 33, 34, 49, 28, 29, 30, 31],
            [35, 36, 37, 38, 39, 40, 41, 49],
            [42, 43, 44, 45, 46, 47, 48, 49],
            [0, 35, 7, 42, 14, 50, 21, 28],
            [1, 36, 8, 43, 15, 50, 22, 29],
            [2, 37, 9, 44, 16, 50, 23, 30],
            [3, 38, 10, 45, 17, 50, 24, 31],
            [32, 4, 39, 11, 50, 46, 18, 25],
            [33, 5, 40, 12, 47, 50, 19, 26],
            [34, 6, 41, 13, 48, 50, 20, 27],
            [0, 32, 48, 8, 16, 40, 51, 24],
            [1, 33, 41, 42, 17, 51, 9, 25],
            [34, 35, 10, 43, 2, 18, 51, 26],
            [51, 3, 36, 11, 44, 19, 27, 28],
            [4, 37, 12, 45, 51, 20, 21, 29],
            [5, 38, 13, 14, 51, 46, 22, 30],
            [6, 39, 7, 15, 51, 23, 47, 31],
            [0, 38, 9, 47, 18, 52, 27, 29],
            [1, 39, 10, 48, 19, 52, 21, 30],
            [2, 40, 42, 11, 20, 22, 52, 31],
            [32, 3, 41, 43, 12, 14, 52, 23],
            [33, 35, 4, 44, 13, 15, 52, 24],
            [34, 36, 5, 7, 45, 16, 52, 25],
            [37, 6, 8, 46, 17, 52, 26, 28],
            [0, 33, 36, 10, 46, 20, 53, 23],
            [1, 34, 37, 11, 14, 47, 53, 24],
            [2, 38, 12, 15, 48, 53, 25, 28],
            [3, 39, 42, 13, 16, 53, 26, 29],
            [4, 7, 40, 43, 17, 53, 27, 30],
            [5, 8, 41, 44, 18, 21, 53, 31],
            [32, 35, 6, 9, 45, 19, 53, 22],
            [0, 41, 11, 45, 15, 54, 26, 30],
            [1, 35, 12, 46, 16, 54, 27, 31],
            [32, 2, 36, 13, 47, 17, 21, 54],
            [33, 3, 37, 7, 48, 18, 22, 54],
            [34, 4, 38, 8, 42, 19, 54, 23],
            [5, 39, 9, 43, 20, 54, 24, 28],
            [6, 40, 10, 44, 14, 54, 25, 29],
            [0, 34, 39, 44, 12, 17, 22, 55],
            [1, 40, 55, 13, 45, 18, 23, 28],
            [2, 7, 41, 46, 19, 55, 24, 29],
            [3, 8, 47, 35, 20, 55, 25, 30],
            [4, 9, 14, 48, 55, 36, 26, 31],
            [32, 37, 10, 15, 55, 27, 42, 5],
            [33, 43, 38, 6, 11, 16, 21, 55],
            [0, 37, 43, 13, 19, 56, 25, 31],
            [32, 1, 38, 7, 44, 20, 56, 26],
            [33, 2, 39, 8, 45, 14, 56, 27],
            [34, 3, 40, 9, 46, 15, 21, 56],
            [4, 41, 10, 47, 16, 22, 56, 28],
            [35, 5, 11, 48, 17, 23, 56, 29],
            [36, 6, 42, 12, 56, 18, 24, 30],
            [49, 50, 51, 52, 53, 54, 55, 56]
                                                    ]
else:
    math = False

filename = 'PutSomethingHere'
os.chdir(r'C:\Users\Shmuel\Documents\Python!!')
os.mkdir(filename)

rotatelist = [0,90,180,270]
scalelist = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
boxes = [(0, 0, 256, 256), (0, 256, 256, 512), (256, 0, 512, 256), (256, 256, 512, 512), (512, 0, 768, 256), (512, 256, 768, 512), (768, 0, 1024, 256), (768, 256, 1024, 512)]
if not math == False:
    random.shuffle(math)
    for x in range(0, y):
        myimage = Image.new(mode = "RGB", size = (1024, 512), color = (255, 255, 255))
        random.shuffle(boxes)

        if y == 57:
            
            a= random.choice(rotatelist)
            b= random.choice(rotatelist)
            c= random.choice(rotatelist)
            d= random.choice(rotatelist)
            e= random.choice(rotatelist)
            f= random.choice(rotatelist)
            g= random.choice(rotatelist)
            h= random.choice(rotatelist)
            a1 = random.choice(scalelist)
            b1 = random.choice(scalelist)
            c1 = random.choice(scalelist)
            d1 = random.choice(scalelist)
            e1 = random.choice(scalelist)
            f1 = random.choice(scalelist)
            g1 = random.choice(scalelist)
            h1 = random.choice(scalelist)
            

            myimage.paste(im = image_list[math[x][0]].rotate(a), box = boxes[0])
            myimage.paste(im = image_list[math[x][1]].rotate(b), box = boxes[1])
            myimage.paste(im = image_list[math[x][2]].rotate(c), box = boxes[2])
            myimage.paste(im = image_list[math[x][3]].rotate(d), box = boxes[3])
            myimage.paste(im = image_list[math[x][4]].rotate(e), box = boxes[4])
            myimage.paste(im = image_list[math[x][5]].rotate(f), box = boxes[5])
            myimage.paste(im = image_list[math[x][6]].rotate(g), box = boxes[6])
            myimage.paste(im = image_list[math[x][7]].rotate(h), box = boxes[7])
        imname = "card" + str(x)
        myimage = myimage.save(filename + r'/' + imname + '.jpg')
elif math == False:
    print("this only works with 7, 13, 31, or 57 images.")
