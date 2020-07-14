import argparse
import os
import shutil


def compress_image(file, quality):
    pass


def compress_audio(file, quality):
    pass


def compress_video(file, quality):
    pass


def compress_media(dir, quality):
    """ Go through an extracted epub directory and compress images, audio, and video files. """
    print(f"Compressing {dir}...")

    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")):
                compress_image(os.path.join(root, file), quality)
            elif file.endswith((".mp3", ".aac", ".wav", ".flac")):
                compress_audio(os.path.join(root, file), quality)
            elif file.endswith((".mp4", ".mov", ".wmv", ".flv", ".avi")):
                compress_video(os.path.join(root, file), quality)


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


def extract_and_compress_media(dir, quality):
    """ Extract an .epub, compress media, then re-archive the new file. """
    temp_dir = dir.replace(".epub", " - Compressed")

    extract_epub(dir, temp_dir)
    compress_media(temp_dir, quality)
    archive_epub(temp_dir)


def main(quality=75): # Placeholder
    dir = input("Enter the path to a directory to process:\n")
    dir = dir.replace("\"", "")
    print("Running...")

    try:
        for root, _, files in os.walk(dir):
            for file in files:
                if file.endswith(".epub"):
                    extract_and_compress_media(os.path.join(root, file), quality)
    except FileNotFoundError:
        print("Invalid path.")
    finally:
        print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--quality", help="choose the quality level to compress media", type=int) # Placeholder
    args = parser.parse_args()

    if args.quality:
        main(args.quality)
    else:
        main()
