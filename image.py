from PIL import Image
img=Image.open('five.png')
data=list(img.getdata())
for i in range(len(data)):
    data[i]=255-data[i]

#Take the data list and go to app.ipynb under handwritten digit recognizer