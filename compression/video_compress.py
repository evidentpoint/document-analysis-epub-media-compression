import subprocess
import os

# Bit rate is the amount of bits used to encode one second of video.
# Lowering bit rate may lower fps, may use more agressive audio and image compression, 
# and is one way to reduce video size.
# Lots of code taken from https://stackoverflow.com/questions/3844430/how-to-get-the-duration-of-a-video-in-python.

# maybe if the bitrate is below 300 kbps it's not worth compressing
def get_bitrate(filename):
    result = subprocess.run(
        f'ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 {filename}', 
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    return float(result.stdout)  # in bits/second


def compress_video_bitrate(filename, bitrate):
    '''compress video based on bitrate'''

    # ffmpeg cannot edit existing files in-place
    temp_name = 'placeholder.mp4'
    subprocess.run(
        f'ffmpeg -i {filename} -b:v {bitrate} {temp_name}'
    )
    os.remove(filename)
    os.rename(temp_name, filename)


def compress_video_crf(filename, crf):
    '''compress video based on constant rate factor https://slhck.info/video/2017/02/24/crf-guide.html'''

    # ffmpeg cannot edit existing files in-place
    temp_name = 'placeholder.mp4'
    subprocess.run(
        f'ffmpeg -i {filename} -vcodec libx265 -crf {crf} {temp_name}'
    )
    os.remove(filename)
    os.rename(temp_name, filename)


compress_video_crf('vid_test/random.mp4', 28)