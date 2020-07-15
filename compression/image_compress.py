from PIL import Image
import os 

name = r'C:\Users\Ben Smus\Evident_Point\da-epub-media-compression\compression\test_img\f0112-01.png'


def split_ext(name):
    dotindex = name.find('.')
    return name[:dotindex], name[dotindex:]  # asdf, .jpg


def compress_image(name, quality):
    pre, ext = split_ext(name)
    
    if ext != '.jpg':  # convert to jpg because that is the most compact format

        print('converting to jpg...')
        outname = pre + '.jpg'
        
        with Image.open(name) as img:
            jpgimg = img.convert('RGB')

        # need to explicitly delete uncompressed file
        os.remove(name)
        
    else:
        img = Image.open(name)
        jpgimg = img
        outname = name

    jpgimg.save(outname, optimize=True, quality=quality)


compress_image(name, 90)  