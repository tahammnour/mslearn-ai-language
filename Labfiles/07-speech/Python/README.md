# 🔊 Azure AI Speech Recognition & Synthesis - Speaking Clock

## 🚀 Project Overview

This project demonstrates the **Azure AI Speech Services** capabilities for both **Speech-to-Text** (speech recognition) and **Text-to-Speech** (speech synthesis). The application creates an interactiv- **Language Setting**: Set synthesis language with `xml:lang`

## 🎯 Key Features Explained

### 📱 **Dual Speech Synthesis Approach**
The application demonstrates two different methods for converting text to speech:

1. **Simple Text Synthesis** (using `en-GB-RyanNeural`):
   ```python
   speak = speech_synthesizer.speak_text_async(response_text).get()
   ```

2. **Advanced SSML Synthesis** (using `en-GB-LibbyNeural`):
   ```python
   speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
   ```

This shows the difference between basic text-to-speech and advanced markup-controlled speech.

### 🖥️ **Environment Compatibility Notes**

#### **PlaysSound Library Issues** 🔊
The code includes `playsound` for audio file playback, but it's commented out due to compatibility issues:

```python
# playsound(audioFile)  # GitHub Codespace error: No module named 'gi'
```

- **Issue**: PlaysSound may fail in certain environments (like GitHub Codespaces)
- **Error**: "No module named 'gi'" - missing GTK/GObject introspection libraries
- **Solution**: The audio file is still processed for speech recognition without playback

#### **Cross-Platform File Paths** 🌍
The code demonstrates proper cross-platform file handling:

```python
# ❌ Windows-only (hardcoded backslashes):
# audioFile = current_dir + '\\time.wav'

# ✅ Cross-platform (automatic path separators):
audioFile = os.path.join(current_dir, 'time.wav')
```

**Why this matters:**
- Windows uses `\` (backslash) as path separator
- Linux/macOS use `/` (forward slash) as path separator  
- `os.path.join()` automatically chooses the correct separator

## ⚠️ Important Notes

- **🔐 Security**: Never commit your `.env` file to version control
- **🎤 No Microphone Required**: This version uses audio file input by default
- **🔊 Audio Output**: Ensure speakers/headphones are connected for synthesis
- **💰 Cost Management**: Monitor usage to stay within free tier limits
- **🌐 Internet Required**: Active internet connection needed for speech services
- **📏 Recognition Timeout**: Speech recognizer times out after ~5 seconds of silence

## 🚨 Troubleshootinglock that can understand voice commands and respond with synthesized speech, telling you the current time.

## 🧠 What Does This Code Do?

The `speaking-clock.py` script performs the following operations:

1. **🔧 Configuration Loading**: Loads Azure Speech service key and region from `.env` file
2. **🔗 Azure Connection**: Establishes connection to Azure AI Speech Service
3. **🎤 Speech Recognition**: Listens for voice input (from audio file)
4. **🧠 Command Processing**: Recognizes "what time is it?" command
5. **⏰ Time Calculation**: Gets current system time
6. **🔊 Speech Synthesis**: Converts response text to natural speech with and without SSML
7. **🎭 Voice Customization**: Uses neural voices for natural-sounding output

## 🏗️ Azure Infrastructure Setup

### 📋 Prerequisites

You need to set up one Azure resource:

#### 🧠 Azure AI Speech Service
- Create an **Azure AI Speech** resource in Azure Portal
- **❗ Important**: Note down the **Key** and **Region**
- The service provides both Speech-to-Text and Text-to-Speech capabilities
- Free tier available with generous monthly limits

### 🔑 Authentication Requirements
The Azure Speech SDK requires:
- **🗝️ Speech Key**: Your service key (Key1 or Key2)
- **🌍 Region**: The Azure region where your service is deployed (e.g., 'eastus')

## 🛠️ Project Setup

### Step 1: Navigate to Project Directory 📁
```bash
cd /workspaces/mslearn-ai-language/Labfiles/07-speech/Python/speaking-clock
```

### Step 2: Install Dependencies 📦
```bash
pip install -r requirements.txt
```

## 📋 Dependencies

The project requires the following Python packages (defined in `requirements.txt`):

```
python-dotenv
azure-cognitiveservices-speech==1.30.0
playsound==1.2.2
```

## ⚙️ Environment Configuration

Update the `.env` file in the project directory:

```properties
SPEECH_KEY=your_speech_service_key_here
SPEECH_REGION=eastus
```

**Note**: Replace with your actual Azure Speech service key and region.

## 📁 Project Structure

```
speaking-clock/
├── speaking-clock.py
├── .env
├── requirements.txt
├── time.wav (sample audio file)
└── README.md
```

## 🎤 Input Methods & Cross-Platform File Handling

The application uses an audio file (`time.wav`) for speech recognition input. The code demonstrates proper cross-platform file path handling:

### 📁 Audio File Input with Cross-Platform Support

```python
# Get current working directory
current_dir = os.getcwd()

# ❌ Windows-only approach (not recommended):
# audioFile = current_dir + '\\time.wav'  # Only works on Windows

# ✅ Cross-platform approach (recommended):
audioFile = os.path.join(current_dir, 'time.wav')  # Works on Windows, Linux, and macOS

# Note: playsound may have issues in some environments (like GitHub Codespaces)
# playsound(audioFile)  # Commented out due to potential 'gi' module error

# Configure audio input from file
audio_config = speech_sdk.AudioConfig(filename=audioFile)
speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
```

### 🔍 **File Path Explanation:**

#### **Windows Path Handling** 🪟
```python
# Windows uses backslashes (\) as path separators
audioFile = current_dir + '\\time.wav'  # Example: C:\Users\project\time.wav
```

#### **Cross-Platform Path Handling** 🌍
```python
# os.path.join() automatically uses the correct separator for any OS
audioFile = os.path.join(current_dir, 'time.wav')
# Windows: C:\Users\project\time.wav
# Linux/macOS: /home/user/project/time.wav
```

### 🎙️ Alternative: Microphone Input (Optional)

To use live microphone input instead of the audio file, you can modify the code:

```python
# Uncomment these lines for microphone input:
# audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
# speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
# print('Speak now...')
```

## 🏃‍♂️ How to Run

1. **Navigate to the project directory:**
   ```bash
   cd /workspaces/mslearn-ai-language/Labfiles/07-speech/Python/speaking-clock
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the speaking clock:**
   ```bash
   python speaking-clock.py
   ```

4. **Expected behavior:**
   - The program reads the `time.wav` audio file for speech recognition
   - It recognizes "What time is it?" from the audio
   - The application responds with synthesized speech telling the time

## 📋 Sample Session

```
Ready to use speech service in: eastus
What time is it?
The time is 14:30
[Synthesized voice]: "The time is 14:30. Time to end this lab!"
```

## 🔍 Code Explanation

### 🏗️ Core Components

#### 1. **Configuration Setup** 🔧
```python
load_dotenv()
ai_key = os.getenv('SPEECH_KEY')
ai_region = os.getenv('SPEECH_REGION')
speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)
```
- Loads environment variables for Azure Speech service
- Creates configuration object for the service

#### 2. **Cross-Platform File Path Handling** 🌍
```python
current_dir = os.getcwd()
# ❌ Windows-only: audioFile = current_dir + '\\time.wav'
# ✅ Cross-platform: 
audioFile = os.path.join(current_dir, 'time.wav')
```
- Uses `os.path.join()` for cross-platform compatibility
- Automatically handles different path separators (\ for Windows, / for Linux/macOS)

#### 3. **Speech Recognition** 🎤
```python
audio_config = speech_sdk.AudioConfig(filename=audioFile)
speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
speech = speech_recognizer.recognize_once_async().get()
```
- Configures audio input from file
- Creates speech recognizer with service configuration
- Performs asynchronous speech recognition

#### 4. **Dual Speech Synthesis Approaches** 🔊

**Method 1: Simple Text-to-Speech**
```python
# Configure voice
speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

# Simple synthesis without markup
speak = speech_synthesizer.speak_text_async(response_text).get()
```

**Method 2: Advanced SSML Synthesis**
```python
# Create SSML markup for advanced speech control
responseSsml = " \
    <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'> \
        <voice name='en-GB-LibbyNeural'> \
            {} \
            <break strength='weak'/> \
            Time to end this lab! \
        </voice> \
    </speak>".format(response_text)

# Synthesize with SSML
speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
```

#### 5. **Voice Configuration & Neural Voices** 🎭
The application demonstrates using different neural voices:
- **en-GB-RyanNeural** - British English, Male (for simple synthesis)
- **en-GB-LibbyNeural** - British English, Female (for SSML synthesis)

#### 6. **Error Handling** ⚠️
```python
if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
    command = speech.text
    print(command)
else:
    print(speech.reason)
    if speech.reason == speech_sdk.ResultReason.Canceled:
        cancellation = speech.cancellation_details
        print(cancellation.reason)
        print(cancellation.error_details)
```
- Handles successful recognition vs. errors
- Provides detailed error information for debugging

## 🎭 Voice Customization & SSML Features

### 🌟 Available Neural Voices
The application demonstrates using different neural voices for natural-sounding speech:

- **en-GB-RyanNeural** - British English, Male (used for simple text synthesis)
- **en-GB-LibbyNeural** - British English, Female (used for SSML synthesis)
- **en-US-AriaNeural** - American English, Female
- **en-US-GuyNeural** - American English, Male
- **en-AU-NatashaNeural** - Australian English, Female

### 🎨 SSML Features Demonstrated
The application showcases several SSML (Speech Synthesis Markup Language) capabilities:

```xml
<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>
    <voice name='en-GB-LibbyNeural'>
        The time is 14:30
        <break strength='weak'/>
        Time to end this lab!
    </voice>
</speak>
```

- **Voice Selection**: Specify exact voice to use
- **Pauses**: Add natural breaks in speech with `<break strength='weak'/>`
- **Language Setting**: Set synthesis language with `xml:lang`
- **en-US-GuyNeural** - American English, Male
- **en-AU-NatashaNeural** - Australian English, Female

### 🎨 SSML Features Used
The application demonstrates several SSML capabilities:

```xml
<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>
    <voice name='en-GB-LibbyNeural'>
        The time is 14:30
        <break strength='weak'/>
        Time to end this lab!
    </voice>
</speak>
```

- **Voice Selection**: Specify exact voice to use
- **Pauses**: Add natural breaks in speech
- **Language Setting**: Set synthesis language

## ⚠️ Important Notes

- **🔐 Security**: Never commit your `.env` file to version control
- **🎤 Microphone Permissions**: Ensure microphone access is granted
- **🔊 Audio Output**: Ensure speakers/headphones are connected
- **💰 Cost Management**: Monitor usage to stay within free tier limits
- **🌐 Internet Required**: Active internet connection needed for speech services
- **📏 Recognition Timeout**: Speech recognizer times out after ~5 seconds of silence

## 🚨 Troubleshooting

### Common Issues:

1. **Authentication Error**:
   - Verify your speech service key and region
   - Check the `.env` file configuration

2. **No Microphone Input**:
   - Ensure microphone permissions are granted
   - Check default audio device settings
   - Verify microphone is not muted

3. **Audio File Not Found**:
   ```bash
   # Ensure time.wav exists in the project directory
   ls -la time.wav
   ```

4. **No Audio Output**:
   - Check speaker/headphone connections
   - Verify system audio settings
   - Test with other audio applications

5. **Module Import Errors**:
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt
   
   # Check if packages are installed
   pip list | grep azure
   pip list | grep playsound
   ```

6. **Recognition Result "No Match"**:
   - Speak more clearly and loudly
   - Ensure the command is exactly "what time is it?"
   - Check microphone positioning

## 🎯 Use Cases

This speech-enabled application demonstrates patterns for:

- 🏠 **Smart Home Devices**: Voice-controlled home automation
- 📱 **Mobile Applications**: Hands-free app interaction
- ♿ **Accessibility Tools**: Voice interfaces for users with disabilities
- 🚗 **Automotive Systems**: In-car voice assistants
- 📞 **Call Centers**: Automated phone systems
- 🎮 **Gaming**: Voice-controlled game interactions
- 🏥 **Healthcare**: Hands-free medical record systems

## 🤝 Contributing

Enhance this project by:
- Adding more voice commands (set alarms, timers, etc.)
- Implementing conversation context and memory
- Adding multi-language support
- Creating a GUI interface
- Adding emotion recognition
- Implementing wake word detection
- Building voice-controlled applications

## 🔄 Advanced Features

### Multiple Voice Commands:
```python
if command.lower() == 'what time is it?':
    TellTime()
elif command.lower() == 'what day is it?':
    TellDate()
elif command.lower() == 'set alarm':
    SetAlarm()
```

### Continuous Listening:
```python
# Implement continuous recognition
speech_recognizer.start_continuous_recognition()
```

### Custom Wake Words:
```python
# Implement keyword recognition
from azure.cognitiveservices.speech import KeywordRecognitionModel
```

## 📚 Additional Resources

- [Azure Speech Service Documentation](https://docs.microsoft.com/azure/cognitive-services/speech-service/)
- [Speech SDK for Python](https://docs.microsoft.com/python/api/azure-cognitiveservices-speech/)
- [SSML Reference](https://docs.microsoft.com/azure/cognitive-services/speech-service/speech-synthesis-markup)
- [Neural Voice Gallery](https://speech.microsoft.com/portal/voicegallery)
- [Speech Recognition Best Practices](https://docs.microsoft.com/azure/cognitive-services/speech-service/how-to-recognize-speech)

## 🎉 Next Steps

1. **Voice Commands**: Add more sophisticated voice interactions
2. **Conversation AI**: Integrate with chat completion services
3. **Multi-Modal**: Combine speech with computer vision
4. **Production**: Deploy as voice assistant or smart device
5. **Real-Time**: Build streaming speech applications

---

**Happy Voice Coding! 🎉🔊**
