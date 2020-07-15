import subprocess
import os


def compress_audio_bitrate(filename, bitrate):
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


compress_audio_bitrate('audio_test/edm-song.mp3', 48000)