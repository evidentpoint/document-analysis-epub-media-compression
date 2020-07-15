import subprocess
import os

# Bit rate is the amount of bits used to encode one second of video.
# Lowering bit rate may lower fps, may use more agressive audio and image compression, 
# and is one way to reduce video size.
# Lots of code taken from https://stackoverflow.com/questions/3844430/how-to-get-the-duration-of-a-video-in-python.


def get_bitrate(filename):
    result = subprocess.run(
        f'ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 {filename}', 
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    return float(result.stdout)  # in bits/second


def compress_video(filename, bitrate):

    # ffmpeg cannot eddit existing files in-place
    temp_name = 'placeholder.mp4'
    subprocess.run(
        f'ffmpeg -i {filename} -b:v {bitrate} {temp_name}'
    )
    os.remove(filename)
    os.rename(temp_name, filename)


print(get_bitrate('vid_test/random.mp4'))
compress_video('vid_test/random.mp4', 128000)  # it's half the size now, but quality is bad