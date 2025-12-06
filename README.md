# AI Doctor with Vision and Voice

This project is an AI-powered virtual doctor that combines voice and vision capabilities to analyze user inputs. It uses speech-to-text (STT) for transcribing audio, a multimodal large language model (LLM) for analyzing images and queries, and text-to-speech (TTS) for generating voice responses. The application is built with Gradio for an interactive user interface.

## Features
- **Speech-to-Text (STT):** Converts user speech into text using the GROQ API.
- **Image Analysis:** Analyzes uploaded images in combination with user queries using a multimodal LLM.
- **Text-to-Speech (TTS):** Converts the AI's response into speech using ElevenLabs or gTTS.
- **Interactive UI:** Provides an easy-to-use interface for audio and image inputs, and displays both text and audio outputs.

---

## Table of Contents

1. [Project Files and Their Functions](#project-files-and-their-functions)
2. [Installing FFmpeg and PortAudio](#installing-ffmpeg-and-portaudio)
   - [macOS](#macos)
   - [Linux](#linux)
   - [Windows](#windows)
3. [Setting Up a Python Virtual Environment](#setting-up-a-python-virtual-environment)
   - [Using Pipenv](#using-pipenv)
   - [Using pip and venv](#using-pip-and-venv)
   - [Using Conda](#using-conda)
4. [Running the Application](#running-the-application)
5. [Ensuring Audio Player Works in Gradio](#ensuring-audio-player-works-in-gradio)

---

## Project Files and Their Functions

### `gradio_app.py`
- **Purpose:** The main entry point of the application.
- **Functionality:**
  - Sets up the Gradio interface for audio and image inputs.
  - Calls functions from other modules to process inputs and generate outputs.
  - Displays the transcription, AI's response, and voice output in the UI.

### `voice_of_the_patient.py`
- **Purpose:** Handles audio recording and transcription.
- **Functionality:**
  - Records audio from the microphone and saves it as an MP3 file.
  - Uses the GROQ API to transcribe the audio into text.

### `brain_of_the_doctor.py`
- **Purpose:** Handles image analysis and query processing.
- **Functionality:**
  - Encodes images into base64 format for processing.
  - Uses a multimodal LLM to analyze the image and user query, generating a response.

### `voice_of_the_doctor.py`
- **Purpose:** Handles text-to-speech conversion.
- **Functionality:**
  - Converts the AI's text response into speech using ElevenLabs or gTTS.
  - Plays the generated audio file on the user's system.

### `.env.example`
- **Purpose:** Provides a template for environment variables.
- **Functionality:**
  - Contains placeholders for the GROQ and ElevenLabs API keys.

### `requirements.txt`
- **Purpose:** Lists all the dependencies required for the project.
- **Functionality:**
  - Ensures all necessary Python packages are installed.

### `README.md`
- **Purpose:** Provides setup instructions and an overview of the project.
- **Functionality:**
  - Guides users through installation, setup, and running the application.

### `.gitignore`
- **Purpose:** Specifies files and directories to be ignored by Git.
- **Functionality:**
  - Prevents unnecessary files (e.g., cache, logs, virtual environments) from being tracked.

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


