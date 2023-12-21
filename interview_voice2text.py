import dask
import dask.bag as db
from dask.distributed import Client
from transformers import pipeline
import os
import time


# Define the processing functions
def process_file(filestem):
    print("started loading")
    asr_model = pipeline(
            'automatic-speech-recognition', 
            model='jonatasgrosman/wav2vec2-large-xlsr-53-russian'
        )

    print("done loading 1")

    spell_corr_model = pipeline(model='UrukHan/t5-russian-spell')
    print("done loading 2")
    # voice2text
    print(f'start speech recognizing {filestem} ...')
    res = asr_model(f'./distributed_files/input/interview2/{filestem}.mp3')
    text = res['text']
    print(f'done with speech recognition for {filestem}')

    # spell corrector
    res = spell_corr_model(text)[0]
    text = res['generated_text']
    print(f'done with spell correction for {filestem}')

    # saving
    with open(f'./distributed_files/output/{filestem}.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'done processing {filestem}')

# Define the number of files to process
#DIRECTORY = "~/distributed_files/input/interview2"
#file_count = len(next(os.listdir(DIRECTORY)))
file_count = 8
filestems = [f'part_{i+1}' for i in range(file_count)]

# Connect to the Dask cluster
client = Client('tcp://10.128.0.36:8786')
# Convert the list of filestems to a Dask bag
file_bag = db.from_sequence(filestems)

# Use Dask delayed to process each file in parallel
delayed_results = [dask.delayed(process_file)(filestem) for filestem in file_bag]

# Compute the results using the Dask distributed scheduler
start = time.time()
dask.compute(*delayed_results, scheduler='distributed')
end = time.time()
#print(f'Overall time: {end - start} sec')

# Close the Dask client
client.close()