from __future__ import unicode_literals
from PIL import Image, ImageDraw, ImageFont

def weight(c):
	w, h = (6, 11)
	font = ImageFont.load_default()
	fw, fh = font.getsize(c)
	im = Image.new('L', (fw, fh))
	draw = ImageDraw.Draw(im)
	
	draw.text(((w - fw)/2, (h - fh)/2), c, 255, font=font)
	im.save('out.png')
	n = len([p for p in im.getdata() if p>5])
	return n / (w * h)
