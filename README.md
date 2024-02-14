# Distributed voice2text tool
An application that allows you to speed up your audio interviews processing. First, split the audio into parts with audio_splitter.py,
second, voice2text and spell corrector models process the audios into text, and, lastly, find answers to your questions in audio interviews.

### Distributed part
Using Dask this code distributively processes the file, as it is split into chuncks. I launched the code remotely on cloud platform using SSH. The setup was: 1 master node and 2 worker nodes.
Distribution accelerated the computing by 40%.
