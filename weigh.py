from __future__ import unicode_literals
from PIL import Image, ImageDraw, ImageFont

def weight(c):
	im = Image.new("RGB", (6,11)) # default size
	draw = ImageDraw.Draw(im)
	font = ImageFont.load_default()
	draw.text((0, 0), c, font=font)
	n = len([p for p in im.getdata() if p[0]>5])
	return n
	
chars = [chr(c) for c in range(32,127)]

sorted_chars = sorted(chars, key=weight, reverse=True)
