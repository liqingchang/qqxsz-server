#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image, ImageDraw, ImageFont
from AbstractHandler import AbstractHandler
import time

class BeiDaHandler(AbstractHandler):
    def handleData(self, name, sex, colleges, degree, id_number, date, upload_file):
        # 读取图像
        im = Image.open('./Templet/beida.png')
        upload = Image.open(upload_file)
        box = (388, 136 , 553 , 344)
        upload = upload.resize((box[2] - box[0], box[3] - box[1]))
        im.paste(upload, box)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype('./Font/NotoSansCJKsc-Bold.otf', size=24)
        fillcolor = '#171113'
        draw.text((144, 153), u'姓名  '+ name ,font=font, fill=fillcolor)
        draw.text((144, 203), colleges,font=font, fill=fillcolor)
        draw.text((144, 253), degree,font=font, fill=fillcolor)
        micro_font = ImageFont.truetype('./Font/NotoSansCJKsc-Bold.otf', size=14)
        draw.text((140, 353), u'发证日期 ' + date ,font=micro_font, fill=fillcolor)
        draw.text((387, 353), u'证号：' + date, font=micro_font, fill=fillcolor)
        file_name = 'result' + str(time.time()) + '.png'
        im.save('./HandleImage/' + file_name)
        return 'http://qqxsz.4gun.net/xsz/' + file_name
