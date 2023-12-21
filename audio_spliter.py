from pydub import AudioSegment
import math
import os
from dask.distributed import Client
import time


def split_audio(input_file, output_folder, duration):
    audio = AudioSegment.from_mp3(input_file_path)
    total_length = len(audio)
    num_parts = math.ceil(total_length / (duration * 1000))

    for i in range(num_parts):
        start = i * duration * 1000
        end = (i + 1) * duration * 1000
        split_audio = audio[start:end]
        output_path = os.path.join(output_folder, f"part_{i+1}.mp3")
        split_audio.export(output_path, format="mp3")
        #split_audio.export(f'./input/interview2/part_{i+1}', format="mp3")
        print(output_path)


if __name__ == '__main__':
    client = Client("tcp://10.128.0.36:8786")

    SECONDS_PER_FILE = 20

    input_file_path = "./distributed_files/input/interview2.mp3"
    output_folder_path = "./distributed_files/input/interview2/"

    print(input_file_path)

    #client.cluster.scheduler.workdir = '/home/sastsy-head/distributed_files'

    start = time.time()
    client.run(split_audio, input_file=input_file_path, output_folder=output_folder_path, duration=SECONDS_PER_FILE)
    end = time.time()
    #print(f'Overall time: {end - start} sec')
    #split_audio(input_file_path, output_folder_path, SECONDS_PER_FILE)
