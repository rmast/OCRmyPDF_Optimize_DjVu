import io
import tesserocr
import numpy as np
import cv2
from pytesseract import pytesseract as pt
from PIL import Image
#from matplotlib import cm

def compute_ratio_and_resize(img,width,height,model_height):
    img2 = None
    ratio = width/(height * 1.0)
    if ratio<1.0:
        ratio = 1.0 / ratio
        img2 = cv2.resize(img,(model_height,int(model_height*ratio)), interpolation=Image.Resampling.LANCZOS)
    else:
        if height < model_height / 2:
            topped, _ = divmod(model_height,height)
            biggerwidth = int(topped * width)
            biggerheight = int(topped * height)
            img2 = cv2.resize(img,(biggerwidth,biggerheight),interpolation=Image.Resampling.LANCZOS)
        else:
            img2 = cv2.resize(img,(int(model_height*ratio),model_height),interpolation=Image.Resampling.LANCZOS)
    return img2,ratio

result=[([107, 500, 181, 306]), ([546, 659, 212, 303]), ([697, 1079, 209, 333]), ([2187, 2264, 323, 359]), ([546, 1337, 359, 424]), ([2188, 2244, 368, 399]), ([2262, 2340, 368, 399]), ([545, 866, 600, 636]), ([992, 1373, 600, 641]), ([1433, 1853, 600, 641]), ([548, 902, 638, 677]), ([992, 1384, 638, 677]), ([1433, 1752, 638, 677]), ([1894, 2371, 636, 677]), ([544, 922, 670, 718]), ([992, 1398, 676, 715]), ([1432, 1790, 673, 718]), ([545, 899, 715, 754]), ([992, 1359, 712, 748]), ([1430, 1771, 712, 755]), ([994, 1340, 748, 790]), ([1433, 1677, 750, 789]), ([1896, 2124, 750, 789]), ([545, 808, 789, 829]), ([989, 1368, 789, 828]), ([1433, 1850, 789, 828]), ([545, 715, 827, 866]), ([1430, 1831, 827, 866]), ([569, 798, 861, 902]), ([992, 1113, 863, 902]), ([1433, 1826, 863, 903]), ([569, 954, 901, 937]), ([992, 1362, 901, 937]), ([1433, 1798, 901, 940]), ([569, 839, 937, 976]), ([992, 1384, 936, 978]), ([1433, 1847, 940, 978]), ([569, 930, 973, 1017]), ([992, 1368, 974, 1015]), ([1433, 1795, 978, 1014]), ([568, 654, 1012, 1051]), ([992, 1340, 1014, 1050]), ([1433, 1804, 1014, 1052]), ([1896, 2139, 1009, 1053]), ([569, 913, 1048, 1088]), ([1434, 1556, 1053, 1084]), ([569, 726, 1088, 1124]), ([992, 1354, 1090, 1126]), ([1432, 1832, 1084, 1133]), ([569, 954, 1126, 1162]), ([992, 1387, 1126, 1162]), ([1430, 1688, 1126, 1162]), ([569, 907, 1159, 1204]), ([993, 1320, 1165, 1197]), ([1897, 2074, 1165, 1197]), ([569, 921, 1199, 1242]), ([990, 1335, 1201, 1243]), ([545, 957, 1236, 1278]), ([991, 1404, 1236, 1278]), ([552, 573, 1336, 1368]), ([621, 1075, 1328, 1385]), ([112, 343, 1416, 1471]), ([546, 585, 1429, 1460]), ([698, 789, 1425, 1461]), ([787, 1707, 1416, 1472]), ([114, 475, 1461, 1506]), ([112, 477, 1498, 1540]), ([113, 425, 1532, 1581]), ([623, 709, 1541, 1572]), ([111, 473, 1570, 1619]), ([112, 480, 1612, 1655]), ([113, 245, 1653, 1685]), ([112, 452, 1688, 1727]), ([112, 436, 1726, 1765]), ([618, 922, 1718, 1772]), ([619, 984, 1836, 1880]), ([549, 577, 1933, 1970]), ([620, 887, 1924, 1984]), ([112, 343, 2016, 2071]), ([545, 589, 2025, 2061]), ([621, 982, 2021, 2071]), ([114, 403, 2062, 2102]), ([114, 447, 2102, 2141]), ([657, 1236, 2099, 2144]), ([112, 477, 2138, 2179]), ([131, 436, 2176, 2215]), ([697, 1010, 2172, 2221]), ([128, 334, 2214, 2253]), ([128, 310, 2253, 2292]), ([744, 1201, 2246, 2295]), ([546, 594, 2478, 2510]), ([618, 2145, 2471, 2520]), ([657, 1130, 2547, 2592]), ([1496, 1708, 2551, 2590]), ([656, 1317, 2620, 2668]), ([1496, 1708, 2628, 2664]), ([656, 1435, 2697, 2745]), ([1496, 1708, 2702, 2741]), ([656, 1164, 2769, 2818]), ([1496, 1710, 2779, 2815]), ([656, 1060, 2845, 2894]), ([1496, 1708, 2853, 2892]), ([655, 1429, 2919, 2969]), ([1496, 1686, 2927, 2966]), ([657, 1061, 2998, 3040]), ([1496, 1708, 3004, 3040]), ([656, 1010, 3069, 3121]), ([1496, 1708, 3078, 3117]), ([115, 901, 3408, 3440]), ([2278, 2326, 3408, 3436]), ([2342, 2396, 3414, 3435])]



img = cv2.imread("/home/rmast/175789293-f39ddfdb-6f3e-4598-8d16-80a1f4a88b36.png", cv2.IMREAD_GRAYSCALE)
for x in result:
  xc = x[0]
  yc = x[2]
  width = x[1] - xc
  height = x[3] - yc
  #if (height == 0):
  print(height)
 # print(str(xc)+' '+str(yc)+' '+str(xd)+' '+str(yd)+' text')

  crop_img = None
  resized_img = None

  crop_img = img[yc : x[3], xc:x[1]]
  resized_img,ratio = compute_ratio_and_resize(crop_img,width,height,80)

  #ret = pt.image_to_boxes(resized_img, lang="nld", config="--psm 7")
  #ret = pt.image_to_data(resized_img, lang="nld+lat+Latin+eng", config="--psm 7", output_type=pt.Output.DICT)
  #oem=tesserocr.OEM.TESSERACT_ONLY
  #print(ret)
  with tesserocr.PyTessBaseAPI(lang='nld+lat+Latin+eng',oem=tesserocr.OEM.DEFAULT) as api:
    img2 = np.uint8(resized_img) 
    im = Image.fromarray(np.uint8(resized_img))
    api.SetImage(im)
    api.Recognize()  # required to get result from the next line
    iterator = api.GetIterator()
    print(iterator.WordFontAttributes())


    level=tesserocr.RIL.SYMBOL
    boxes = api.GetComponentImages(tesserocr.RIL.TEXTLINE, True)
    text_list = []
    print('Found {} textline image components.'.format(len(boxes)))
    if len(boxes) >0:
        i = 0
        for r in tesserocr.iterate_level(iterator, level):
            symbol = r.GetUTF8Text(level)
            print(symbol)
            conf = r.Confidence(level)
            print(conf)
            bbox = r.BoundingBoxInternal(level)
            im = Image.fromarray(img2[bbox[1]:bbox[3], bbox[0]:bbox[2]])
            im.save("/home/rmast/out" + str(i) + ".tif")
            text_list.append(symbol + " " + str(conf) + "\n")
            i += 1
