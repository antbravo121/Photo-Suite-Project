#Photo Suite Project
#GROUP NAMES: Anthony Bravo, Wentao He

from PIL import Image, ImageFilter, ImageDraw

im1 = Image.open("photo1.png")
im2 = Image.open("photo2.png")
im3 = Image.open("photo3.png")


#Takes in x & y coordinants and a photo width and height
#Returns a tuple with values corresponding with the pixel values of 
#a vignette effect
def vignette(x,y,a,b):
	a, b = a//2.5, b//2.5
	try:
		return 3*(int(255 / (((x**2)/(a**2)) + ((y**2)/(b**2)))),)
	except ZeroDivisionError:
		return 3*(255,)






'''
INPUT: an image

Checks if any side of the image is
larger than 600 pixels. If so, resizes
the image such that the maximum length
of one side is 600 pixels

You MUST ensure you keep a constant
aspect ratio between the original and 
resized image

OUTPUT: The resized image
'''
def resizify(image):
	wid = image.width
	hei = image.height
	if wid > 600 and wid > hei:
		r = wid/600
		wid = wid/r
		hei = hei/r
	elif hei > 600 and hei > wid:
		r = hei/600
		hei = hei/r
		wid = wid/r
	out = image.resize((int(wid),int(hei)))
    return out



    
'''
INPUT: an image and a string 
The string represents a style: valid 
inputs should be "S" (for square) and 
"4x3"

If the style is "S", crop the image to 
the shape of a square (aspect ratio of 1x1)

Otherwise, if the style is "4x3", crop
the image to have aspect ratio of 4x3

You MUST remove the least amount of image 
possible in your crop and your crop must be
centered around the center of the original 
image

OUTPUT: The cropped image
'''
def cropify(image, style):
    wid=image.width
    hei=image.height
    ratio=wid/hei
    if style=="S":
        if wid>hei:
            difference=wid-hei
            m=difference/2
            out=image.crop((m,0,wid-m,hei))
            return out
        elif hei>wid:
            difference=hei-wid
            m=difference/2
            out=image.crop((0,m,wid,hei-m))
            return out
    else:
        lst=style.split('x')
        ideal_ratio=int(lst[0])/int(lst[1])
        if ideal_ratio > ratio:
        #crop the height : top and bottom
        #increase ratio = decrease the height or increase the width(invalid)
            new_hei=wid / ideal_ratio
            m=(hei - new_hei)/2
            out=image.crop((0,m,wid,hei-m))
            return out
        elif ideal_ratio < ratio:
        # crop the width: left and right
        # decrease ratio= decrease the width or increase the height(invalid)
            new_wid=hei * ideal_ratio
            m=(wid - new_wid)/2
            out=image.crop((m,0,wid-m,hei))
            return out




'''
INPUT: an image and a string
The string represents a color: valid
inputs should be "B" (for black) and
"W" (for white)

Draw a rectangular border around the image.
The color of the border should correspond
with the inputted color string

OUTPUT: The bordered image
'''  
def borderify(image, color):
    if color == "B":
    	color = (0,0,0)
    elif color == "W":
    	color = (255,255,255)
    else:
    	return "invalid color, try B for black or W for white"

    borderWidth = int(image.height/7)

    draw = ImageDraw.Draw(image)
    draw.line([(0,0),(0, image.height)], fill= color, width=borderWidth)
    draw.line([(image.width,0),(image.width, image.height)], fill= color,width=borderWidth)
    draw.line([(0,0),(image.width, 0)], fill= color,width=borderWidth)
    draw.line([(0,image.height),(image.width, image.height)], fill= color,width=borderWidth)



'''
INPUT: an image

Create a vignette effect on the image using
the included vignette function.

OUTPUT: The vignetted image
'''
def vignettify(image):
    

#If the image is not square, return an error message
#If the sides of the image are not odd, make them odd
	if image.width != image.height:
		return "Error: Image is not a square"
	elif image.width % 2 == 0:
		image = image.resize((image.width-1,image.height-1))


#Create a new white image for your vignette effect
#Use the vingnette function to create a list of pixel values
	pixelList = []
	y = -(image.height/2)
	x = -(image.width/2)
	while y < image.height/2:
		while x < image.width/2:
			pixelList.append(vignette(x,y,image.width, image.height))
			x+=1
		x = -(image.width/2)
		y+=1

	whiteImage = Image.new("RGB" ,(image.width, image.height), (255,255,255))
	whiteImage.putdata(pixelList)


#Apply your list to the blank image and blend together the 
#vignette mask and the original image
	image = Image.blend(image, whiteImage, 0.5)
	return image



'''
INPUT: an image

Apply any filter you'd like on the inputted
image.

OUTPUT: The filtered image
'''
def filter1(image):
	return image.filter(ImageFilter.BLUR)
	#filter funtions most be assined to a variable to change the acutal 
	#Ex: im1 = filter1(im1)



'''
Same deal as filter 1. Just choose another style
of filter, your choice
'''
def filter2(image): 
    return image.filter(ImageFilter.CONTOUR)




  
