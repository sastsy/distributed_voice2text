# Distributed Voice to Text Application

This application utilizes distributed computing to perform voice-to-text transcription, question-answering, and text processing tasks efficiently.

## Introduction

This application consists of three main Python scripts:

1. **audio_splitter.py**: Splits an input audio file into smaller segments.
2. **interview_voice2text.py**: Transcribes audio files into text using automatic speech recognition (ASR) and performs spell correction.
3. **interview_qa.py**: Performs question-answering tasks on text data.

## Setup

Ensure the following dependencies are installed:

- Python 3.x
- pydub
- dask
- transformers
- dask.distributed

## Usage

1. **audio_splitter.py**:
    - Split an audio file into smaller segments.
    - Specify the input audio file path, output folder path, and duration of each segment in seconds.

    ```bash
    python audio_splitter.py
    ```

2.  **interview_voice2text.py**:
    - Transcribe audio files into text and perform spell correction.
    - Requires input audio files in the specified folder.

    ```bash
    python interview_voice2text.py
    ```

3. **interview_qa.py**:
    - Perform question-answering tasks on text data.
    - Requires pre-split text files in the output folder.

    ```bash
    python interview_qa.py
    ```


## Dependencies

- **pydub**: Audio processing library.
- **dask**: Parallel computing library.
- **transformers**: Library for natural language processing tasks.
- **dask.distributed**: Distributed computing framework.

## Configuration

- Ensure that the Dask client is configured with the correct address and port for distributed computing.
- Modify the paths and parameters in the scripts as per your requirements.

## Acknowledgments

- This application utilizes various open-source libraries and models for audio processing and natural language understanding.
