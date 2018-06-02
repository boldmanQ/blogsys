# coding:utf-8
from __future__ import unicode_literals

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.six import StringIO
from PIL import Image, ImageDraw, ImageFont


class MyStorage(FileSystemStorage):
    def save(self, name, content, max_length=None):
        # 处理逻辑
        if 'image' in content.content_type:
            # 加水印
            image = self.watermark_with_text(content, '@@@@@@@@@', 'black')
            content = self.convert_image_to_file(image, name)

        return super(MyStorage, self).save(name, content, max_length=max_length)

    def convert_image_to_file(self, image, name):
        temp = StringIO()
        image.save(temp, format='PNG')
        return InMemoryUploadedFile(temp, None, name, 'image/png', temp.len, None)

    def watermark_with_text(self, file_obj, text, color, fontfamily="/usr/share/font/comicz.ttf"):
        image = Image.open(file_obj).convert('RGBA')
        imageWatermark = Image.new('RGBA', image.size, (255, 255, 255, 0))

        draw = ImageDraw.Draw(imageWatermark)
        width, height = image.size
        margin = 10
        font = ImageFont.truetype(fontfamily, int(height / 20))
        textWidth, textHeight = draw.textsize(text, font)
        x = (width - textWidth - margin) / 2
        y = height - textHeight - margin

        draw.text((x, y), text, color, font)

        return Image.alpha_composite(image, imageWatermark)
