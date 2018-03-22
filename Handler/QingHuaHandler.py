#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image, ImageDraw, ImageFont
from AbstractHandler import AbstractHandler
import time

class QingHuaHandler(AbstractHandler):

    def handleData(self, name, sex, colleges, degree, id_number, date, upload_file):
        # 打开模板图像
        im = Image.open('./Templet/qinghua.png')
        # 打开用户头像
        upload = Image.open(upload_file)
        # 设定用户头像在模板图像的位置
        box = (441, 140 , 619 , 370)
        upload = upload.resize((box[2] - box[0], box[3] - box[1]))
        # 把用户头像粘入模板图像
        im.paste(upload, box)
        # 设定画笔
        draw = ImageDraw.Draw(im)
        # 设定字体
        font = ImageFont.truetype('./Font/NotoSansCJKsc-Bold.otf', size=21)
        # 设定颜色
        fillcolor = '#13100d'
        # 写入文字信息
        draw.text((160, 147), name ,font=font, fill=fillcolor)
        draw.text((160, 185), sex ,font=font, fill=fillcolor)
        draw.text((160, 226), colleges ,font=font, fill=fillcolor)
        draw.text((160, 268), degree ,font=font, fill=fillcolor)
        draw.text((160, 308), id_number ,font=font, fill=fillcolor)
        draw.text((160, 348), date, font=font, fill=fillcolor)
        file_name = 'result' + str(time.time()) + '.png'
        # 保存处理后的图片
        im.save('./HandleImage/' + file_name)
        # 返回图片路径
        return 'http://qqxsz.4gun.net/xsz/' + file_name
