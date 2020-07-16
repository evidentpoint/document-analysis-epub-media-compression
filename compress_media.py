import argparse
import os
import shutil
import subprocess
from PIL import Image

DEFAULT_IMAGE_QUALITY = 90
DEFAULT_AUDIO_QUALITY = 48000  # Bitrate
DEFAULT_VIDEO_QUALITY = 28  # CRF


def split_ext(name):
    """ Return a file name split into name and extension. """
    dotindex = name.find('.')
    return name[:dotindex], name[dotindex:]  # asdf, .jpg


def compress_image(name, quality):
    """ Convert an image file to jpg and optimize it. """
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


def compress_audio(filename, bitrate):
    '''
    compress audio based on bitrate
    reasonable smallest bitrate is 48 kbps
    96 kbps is decent audio 
    320 kbs is premium audio 
    '''

    # ffmpeg cannot edit existing files in-place
    temp_name = 'placeholder.mp3'
    subprocess.run(
        f'ffmpeg -i {filename} -b:a {bitrate} {temp_name}'
    )
    os.remove(filename)
    os.rename(temp_name, filename)


def compress_video(file, quality):
    pass


def compress_media(dir, image_quality, audio_quality, video_quality):
    """ Go through an extracted epub directory and compress images, audio, and video files. """
    print(f"Compressing {dir}...")

    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")):
                compress_image(os.path.join(root, file), image_quality)
            elif file.endswith((".mp3", ".aac", ".wav", ".flac")):
                compress_audio(os.path.join(root, file), audio_quality)
            elif file.endswith((".mp4", ".mov", ".wmv", ".flv", ".avi")):
                compress_video(os.path.join(root, file), video_quality)


def archive_epub(src_dir):
    """ Archive a directory as an epub and delete the original directory. """
    print(f"Archiving {os.path.basename(os.path.normpath(src_dir))}...")

    shutil.make_archive(src_dir, 'zip', src_dir)
    os.rename(src_dir + ".zip", src_dir + ".epub")
    shutil.rmtree(src_dir)


def extract_epub(src_file, dest_dir):
    """
    Extract an epub file.

    Parameters:
        src_file (str): file path to a .epub file
        dest_dir (str): directory to extract to
    """
    print(f"Extracting {os.path.basename(os.path.normpath(src_file))}...")

    zip_file = src_file.replace(".epub", ".zip")
    os.rename(src_file, zip_file)
    shutil.unpack_archive(zip_file, dest_dir, 'zip')
    os.rename(zip_file, src_file)


def extract_and_compress_media(dir, image_quality, audio_quality, video_quality):
    """ Extract an .epub, compress media, then re-archive the new file. """
    temp_dir = dir.replace(".epub", " - Compressed")

    extract_epub(dir, temp_dir)
    compress_media(temp_dir, image_quality, audio_quality, video_quality)
    archive_epub(temp_dir)


def main(image_quality, audio_quality, video_quality):
    dir = input("Enter the path to a directory to process:\n")
    dir = dir.replace("\"", "")
    print("Running...")

    try:
        for root, _, files in os.walk(dir):
            for file in files:
                if file.endswith(".epub"):
                    extract_and_compress_media(os.path.join(
                        root, file), image_quality, audio_quality, video_quality)
    except FileNotFoundError:
        print("Invalid path.")
    finally:
        print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--image", help="specify the quality level to compress images", type=int)
    parser.add_argument(
        "-a", "--audio", help="specify the bitrate to compress audio", type=int)
    parser.add_argument(
        "-v", "--video", help="specify the birate to compress video", type=int)
    args = parser.parse_args()

    image_quality = args.image if args.image else DEFAULT_IMAGE_QUALITY
    audio_quality = args.audio if args.audio else DEFAULT_AUDIO_QUALITY
    video_quality = args.video if args.video else DEFAULT_VIDEO_QUALITY

    main(image_quality, audio_quality, video_quality)
