__author__ = 'tli47'

from PIL import Image,ImageDraw,ImageFont

msgNum = 47

# Read image
im = Image.open('pic.jpg')
w,h = im.size
wDraw = 0.8 * w
hDraw = 0.08 * h

# Draw image
font = ImageFont.truetype('C:\Windows\Fonts\msyh.ttc', 40) # use absolute font path to fix 'IOError: cannot open resource'
draw = ImageDraw.Draw(im)
draw.text((wDraw,hDraw), str(msgNum), font=font, fill='red')
# draw.text((wDraw,hDraw), msgNum, fill='red')

# Save image
im.save('pic_msg.jpg')