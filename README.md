# Project Setup Guide

This guide provides step-by-step instructions to set up your project environment, including the installation of FFmpeg and PortAudio across macOS, Linux, and Windows, as well as setting up a Python virtual environment using Pipenv, pip, or conda.

## Table of Contents

1. [Installing FFmpeg and PortAudio](#installing-ffmpeg-and-portaudio)
   - [macOS](#macos)
   - [Linux](#linux)
   - [Windows](#windows)
2. [Setting Up a Python Virtual Environment](#setting-up-a-python-virtual-environment)
   - [Using Pipenv](#using-pipenv)
   - [Using pip and venv](#using-pip-and-venv)
   - [Using Conda](#using-conda)
3. [Running the Application](#running-the-application)
4. [Ensuring Audio Player Works in Gradio](#ensuring-audio-player-works-in-gradio)

---

## Installing FFmpeg and PortAudio

### macOS

1. **Install Homebrew** (if not already installed):

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install FFmpeg and PortAudio:**

   ```bash
   brew install ffmpeg portaudio
   ```

### Linux
For Debian-based distributions (e.g., Ubuntu):

1. **Update the package list**

   ```bash
   sudo apt update
   ```

2. **Install FFmpeg and PortAudio:**

   ```bash
   sudo apt install ffmpeg portaudio19-dev
   ```

### Windows

#### Download FFmpeg:
1. Visit the official FFmpeg download page: [FFmpeg Downloads](https://ffmpeg.org/download.html)
2. Navigate to the Windows builds section and download the latest static build.

#### Extract and Set Up FFmpeg:
1. Extract the downloaded ZIP file to a folder (e.g., `C:\ffmpeg`).
2. Add the `bin` directory to your system's PATH:
   - Search for "Environment Variables" in the Start menu.
   - Click on "Edit the system environment variables."
   - In the System Properties window, click on "Environment Variables."
   - Under "System variables," select the "Path" variable and click "Edit."
   - Click "New" and add the path to the `bin` directory (e.g., `C:\ffmpeg\bin`).
   - Click "OK" to apply the changes.

#### Install PortAudio:
1. Download the PortAudio binaries from the official website: [PortAudio Downloads](http://www.portaudio.com/download.html)
2. Follow the installation instructions provided on the website.

---

## Setting Up a Python Virtual Environment

### Using `pip` and `venv`
#### Create a Virtual Environment:
```bash
python -m venv venv
```

#### Activate the Virtual Environment:
**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

#### Install Dependencies:
```bash
pip install -r requirements.txt
```

---

### Using Conda
#### Create a Conda Environment:
```bash
conda create --name myenv python=3.11
```

#### Activate the Conda Environment:
```bash
conda activate myenv
```

#### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Add the Environment Variables:
Create a `.env` file in the root directory of the project and add the following:

```env
GROQ_API_KEY="your_groq_api_key_here"
ELEVEN_API_KEY="your_elevenlabs_api_key_here"
```

---

## Running the Application

To run the Gradio application, execute the following command:

```bash
python gradio_app.py
```

This will launch the Gradio interface in your default web browser.

---

## Ensuring Audio Player Works in Gradio

To ensure the audio player is displayed in the Gradio interface:

1. Verify that the `text_to_speech_with_elevenlabs` function in `voice_of_the_doctor.py` returns the correct file path after saving the audio file. The function should look like this:

   ```python
   def text_to_speech_with_elevenlabs(input_text, output_filepath):
       client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
       audio = client.generate(
           text=input_text,
           voice="Aria",
           output_format="mp3_22050_32",
           model="eleven_turbo_v2",
       )
       elevenlabs.save(audio, output_filepath)
       return output_filepath  # Ensure the file path is returned
   ```

2. Ensure that FFmpeg is correctly installed and added to your system's PATH. You can verify this by running:

   ```bash
   ffmpeg -version
   ```

3. Confirm that the `process_inputs` function in `gradio_app.py` correctly passes the audio file path to the `gr.Audio` output component.

4. If the audio player still does not appear, check the browser console for errors and ensure the audio file is being saved in the correct format (e.g., MP3).

---

With these steps, your Gradio application should display the audio player and function as expected.


