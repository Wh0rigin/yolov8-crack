# voc_to_yolo.py
 
import os
import xml.etree.ElementTree as ET
from fnmatch import fnmatch
 
 
# 转换之前先修改类别和路径
classes  = ["crack"]
# 指定路径
IN_PATH  = "./datasets/crack/xmls"           # xml文件夹路径
OUT_PATH = "./datasets/crack/labels"        # txt文件夹路径
 
# 一般情况不修改：类别起始编号start_number
start_number = 0
 
 
 
# (lx,ly,rx,ry) -> (cx,xy,w,h)
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h
 
def convert_annotation(in_path, out_path, img_id):
    i_p = os.path.join(in_path, img_id+'.xml')
    in_file = open(i_p, 'rb')
    o_p = os.path.join(out_path, img_id + '.txt')
    out_file = open(o_p, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls) + start_number
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
            float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
 
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
 
def xml2txt(in_path,out_path):
    file_lst = os.listdir(in_path)
    for f in file_lst:
        if fnmatch(f, '*.xml'):
            print("Translate...",f)
            img_id = f.split('.')[0]
            convert_annotation(in_path, out_path, img_id)
 
 
xml2txt(IN_PATH, OUT_PATH)