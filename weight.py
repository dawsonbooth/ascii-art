from __future__ import unicode_literals
from PIL import Image, ImageDraw, ImageFont

def weigh(c):
	w, h = (6, 11)
	font = ImageFont.load_default()
	fw, fh = font.getsize(c)
	im = Image.new('L', (fw, fh))
	draw = ImageDraw.Draw(im)
	
	draw.text(((w - fw)/2, (h - fh)/2), c, 255, font=font)
	#im.save('out.png')
	n = len([p for p in im.getdata() if p>5])
	return n / (w * h)

def weigh_chars(chars):
	weighted_chars = dict()
	max_weight = 0
	for c in chars:
		w =  weigh(c)
		if w > max_weight:
			max_weight = w
		weighted_chars[c] = w

	for c in weighted_chars.keys():
		weighted_chars[c] *= (1 / max_weight)

	return weighted_chars

