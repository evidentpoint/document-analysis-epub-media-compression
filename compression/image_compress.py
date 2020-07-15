from PIL import Image

# only compress images that are bigger than 100 KB

# this image has a size of 334 KB 
inname = 'testimg\\original_phone.png'
outname = 'testimg\\copy_phone.jpg'


def compress(inname, outname, quality):
    img = Image.open(inname)

    if inname[-3:] != 'jpg':  # convert to jpg because that is the most compact format
        jpgimg = img.convert('RGB')
        print(1)
    else:
        jpgimg = img

    jpgimg.save(outname, optimize=True, quality=quality)


# compress 100 with optimize does not do anything (makes sense)
# compress 90 reduces file size to 140 KB
compress(inname, outname, 90)  # side by side comparison reveals no perceptible change!