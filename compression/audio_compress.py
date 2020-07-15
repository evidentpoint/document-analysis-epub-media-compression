import subprocess
import os


def compress_audio_bitrate(filename, bitrate):
    '''compress audio based on bitrate'''

    # ffmpeg cannot edit existing files in-place
    temp_name = 'placeholder.mp3'
    subprocess.run(
        f'ffmpeg -i {filename} -b:a {bitrate} {temp_name}'
    )
    os.remove(filename)
    os.rename(temp_name, filename)


compress_audio_bitrate('audio_test/edm-song.mp3', 48000)