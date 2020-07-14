from PIL import Image

# only compress images that are bigger than 100 KB
# first get it working with jpg 
# as it seems like the most common format

# this image has a size of 937 KB 
name = r'C:\Users\Ben Smus\Evident_Point\FTP\Carnegie_Clone\ftpfiles_original_TEST_WITH_EPUBS\american_promise\OEBPS\images\ROA_04249_EM_M03.jpg'


def compress(name, quality):
    '''
    Warning: Overwrites the image! 
    Will be copying from the ftp server anyways, so there is a backup.
    Quality is from 0 -> 100, 100 being original qualty.
    '''

    img = Image.open(name)
    img.save(name, optimize=True, quality=quality)


# wow, it compressed it to only 283 KB, was not expecting that
compress(name, 90)