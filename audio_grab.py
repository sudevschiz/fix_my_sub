# Developer : Dave
# Contact : (https://github.com/sudevschiz)
# Submit issues at : https:/github.com/fix_my_sub

# Objective : Grab audio from the video file


import subprocess
import os
import sys

def extract_audio(file_path_input,num_samples):
    file_name = os.path.basename(file_path_input)
    raw_file_name = os.path.basename(file_name).split('.')[0]
    file_dir = os.path.dirname(file_path_input)
    file_path_output = file_dir + '/' + raw_file_name + '.wav'
    print('processing file: %s' % file_path_input)
    subprocess.call(
        ['ffmpeg', '-i', file_path_input, '-codec:a', 'pcm_s16le', '-ac', '1', file_path_output])
    print('file %s saved' % file_path_output)