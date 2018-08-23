def whiten(img):
	img.convert("RGBA")
	datas = img.getdata()
	newData = []
	for item in datas:
		if item <= 1:
			newData.append((255, 255, 255, 1))
		else:
			newData.append(item)
			
	img.putdata(newData)
	return img

def find_symbol(p,symbols):
	n = 255/len(symbols)
	
	sections = [n*i for i,v in enumerate(symbols)]
	
	for i,s in enumerate(sections):
		if p < s:
			return symbols[i-1]
	return symbols[-1]

def image_to_ascii(image,w,h,symbols="M@%#*+=-:. "):
	image = image.resize((w,h)).convert('L')
	
	pixels = image.load()
	ascii_art = ''
	
	for i in range(h):
		for j in range(w):
			#print(pixels[j,i])
			ascii_art += find_symbol(pixels[j,i],symbols)
			if j == w-1:
				ascii_art += '\n'
				
	return ascii_art
