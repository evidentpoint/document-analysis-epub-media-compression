import subprocess

# bit rate is the amount of bits used to encode one second of video
# lowering bit rate may lower fps, and may use more agressive audio and image compression
# our aim is to reduce video size to 1/2

# ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 asdfmovie.mp4

def get_length(filename):  # taken from https://stackoverflow.com/questions/3844430/how-to-get-the-duration-of-a-video-in-python
    result = subprocess.run(f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {filename}',
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

    return float(result.stdout)


# print(get_length('vid_original/asdfmovie.mp4'))  # 107 seconds
