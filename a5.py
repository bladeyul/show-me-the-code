from PIL import Image
import os

pics=[".jpg",".JPG"]
norm_size=(256,1024)

def isPic(filePath):
	if os.path.splitext(filePath)[-1] in pics:
		return True
	return False

def modifyPics(filePath):
	for fileName in os.listdir(filePath):
		picFile=os.path.join(filePath,fileName)
		if isPic(picFile):
			modifyPic(picFile)

def modifyPic(filePath):
	im=Image.open(filePath)
	new_size=im.size
	if im.size[0]>norm_size[0]:
		new_size=norm_size[0]
	if im.size[1]>norm_size[1]:
		new_size=norm_size[1]
	im.resize(new_size)
	im.save(filePath)






