# 🌍 Azure AI Speech Translation - Real-Time Language Translator

## 🚀 Project Overview

This project demonstrates **Azure AI Speech Services** for **real-time speech translation** with **text-to-speech synthesis**. The application translates English speech into multiple languages and speaks the translation using native neural voices, including **Egyptian Arabic**! 🇪🇬

### 🎯 What This Project Does

1. **🎤 Speech Recognition**: Converts English audio to text
2. **🌐 Language Translation**: Translates English text to target languages
3. **🔊 Speech Synthesis**: Converts translated text back to speech with native voices
4. **🎵 Interactive Interface**: User-friendly language selection menu

---

## 📋 Prerequisites

### 🔑 **Azure Resources Required**
- **Azure AI Speech Service** (Cognitive Services)
- Valid **Speech API Key** and **Region**

### 🛠️ **Development Environment**
- Python 3.7+ 
- pip package manager
- Audio file: `station.wav` (provided in project)

---

## ⚙️ Setup Instructions

### 1. **Environment Configuration** 📝

Create a `.env` file in the `translator/` directory:

```bash
SPEECH_KEY=your_speech_service_key_here
SPEECH_REGION=your_azure_region_here
```

**Azure Portal Steps:**
1. Create **Azure AI Speech Service** resource
2. Go to **Keys and Endpoint** section
3. Copy **Key 1** → `SPEECH_KEY`
4. Copy **Location/Region** → `SPEECH_REGION`

### 2. **Install Dependencies** 📦

```bash
pip install azure-cognitiveservices-speech python-dotenv playsound
```

### 3. **Project Structure** 📁

```
08-speech-translation/Python/
├── translator/
│   ├── translator.py      # 🎯 Main translation application
│   ├── station.wav        # 🎵 Sample English audio file
│   └── .env              # 🔐 Azure credentials
└── README.md             # 📖 This documentation
```

---

## 🎮 How to Run

```bash
cd translator/
python translator.py
```

### **Interactive Menu** 🎯
```
Enter a target language
 fr = French
 es = Spanish  
 hi = Hindi
 ar = Arabic (Egyptian) 🇪🇬
 save = Save translation audio files  # 🆕 TESTING FEATURE
 Enter anything else to stop
```

### **🎵 Save Feature for Testing**
Type `save` to generate audio files for all languages at once:
- Creates a `translations/` directory
- Saves 4 audio files: French, Spanish, Hindi, and Egyptian Arabic
- Perfect for testing voice quality and translation accuracy

**Generated Files:**
```
translations/
├── translation_french.wav           # 🇫🇷 French (Henri Neural)
├── translation_spanish.wav          # 🇪🇸 Spanish (Elvira Neural)
├── translation_hindi.wav            # 🇮🇳 Hindi (Madhur Neural)
└── translation_arabic_egyptian.wav  # 🇪🇬 Egyptian Arabic (Salma Neural)
```

---

## 🗣️ Supported Languages & Voices

| Language | Code | Neural Voice | Region/Accent |
|----------|------|--------------|---------------|
| 🇫🇷 **French** | `fr` | `fr-FR-HenriNeural` | France |
| 🇪🇸 **Spanish** | `es` | `es-ES-ElviraNeural` | Spain |
| 🇮🇳 **Hindi** | `hi` | `hi-IN-MadhurNeural` | India |
| 🇪🇬 **Arabic** | `ar` | `ar-EG-SalmaNeural` | **Egypt** |

### 🌟 **Special Feature: Egyptian Arabic**
The project uses **`ar-EG-SalmaNeural`** - a high-quality neural voice specifically trained for **Egyptian Arabic dialect**, providing authentic pronunciation and intonation! 🎭

---

## 💻 Code Explanation

### 🔧 **Main Function Architecture**

```python
def main():
    # 🔑 Load Azure credentials from .env file
    load_dotenv()
    ai_key = os.getenv('SPEECH_KEY')
    ai_region = os.getenv('SPEECH_REGION')
    
    # 🌐 Configure translation service
    translation_config = speech_sdk.translation.SpeechTranslationConfig(ai_key, ai_region)
    translation_config.speech_recognition_language = 'en-US'  # 🎤 Source language
    translation_config.add_target_language('fr')  # 🇫🇷 French
    translation_config.add_target_language('es')  # 🇪🇸 Spanish  
    translation_config.add_target_language('hi')  # 🇮🇳 Hindi
    translation_config.add_target_language('ar')  # 🇪🇬 Arabic (Egyptian)
```

### 🎯 **Translation Process Flow**

#### **Step 1: Audio Input** 🎵
```python
audioFile = 'station.wav'
audio_config = speech_sdk.AudioConfig(filename=audioFile)
translator = speech_sdk.translation.TranslationRecognizer(translation_config, audio_config)
```
- Loads pre-recorded English audio file
- Creates audio configuration for speech recognition

#### **Step 2: Speech Recognition** 👂
```python
result = translator.recognize_once_async().get()
print('Translating "{}"'.format(result.text))  # 📝 Display recognized text
```
- Converts English speech to text
- Shows the recognized English text

#### **Step 3: Language Translation** 🌍
```python
translation = result.translations[targetLanguage]
print(translation)  # 📋 Display translated text
```
- Translates English text to selected target language
- Displays the translated text

#### **Step 4: Speech Synthesis** 🔊
```python
voices = {
    "fr": "fr-FR-HenriNeural",
    "es": "es-ES-ElviraNeural", 
    "hi": "hi-IN-MadhurNeural",
    "ar": "ar-EG-SalmaNeural"  # 🇪🇬 Egyptian Arabic voice!
}
speech_config.speech_synthesis_voice_name = voices.get(targetLanguage)
speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
speak = speech_synthesizer.speak_text_async(translation).get()
```
- Maps each language to its neural voice
- **Egyptian Arabic** uses `ar-EG-SalmaNeural` for authentic pronunciation
- Converts translated text to natural-sounding speech

---

## 🎵 Audio Features

### 🎧 **PlaysSound Compatibility**
```python
# playsound(audioFile)  # Commented out due to GitHub Codespaces compatibility
```
- **Issue**: PlaysSound may fail in certain environments
- **Solution**: Audio processing continues without playback preview
- **Alternative**: Use local development environment for full audio experience

### 🎤 **Microphone vs File Input**
The code supports both input methods:

**File Input** (Current):
```python
audioFile = 'station.wav'
audio_config = speech_sdk.AudioConfig(filename=audioFile)
```

**Microphone Input** (Available):
```python
# Uncomment for live microphone input:
# audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
```

---

## 🌟 Key Features Explained

### 🎯 **Multi-Language Support**
- **4 Target Languages**: French, Spanish, Hindi, and Egyptian Arabic
- **Native Voices**: Each language uses region-specific neural voices
- **Real-time Processing**: Instant translation and synthesis

### 🇪🇬 **Egyptian Arabic Integration**
- **Voice**: `ar-EG-SalmaNeural` - Female Egyptian voice
- **Dialect**: Authentic Egyptian Arabic pronunciation
- **Quality**: High-fidelity neural voice technology

### 🔄 **Interactive Loop**
- **Continuous Operation**: Translate multiple times in one session
- **Language Switching**: Easy switching between target languages
- **Clean Exit**: Type anything other than language codes to stop

---

## 🚨 Troubleshooting

### **Common Issues** 🔧

#### **1. Authentication Errors**
```
Error: Invalid subscription key or service region
```
**Solution**: 
- Verify `SPEECH_KEY` and `SPEECH_REGION` in `.env` file
- Ensure Azure Speech Service is active

#### **2. Audio File Missing**
```
Error: Could not find station.wav
```
**Solution**:
- Ensure `station.wav` exists in the same directory as `translator.py`
- Use absolute path if needed: `audioFile = '/full/path/to/station.wav'`

#### **3. PlaysSound Errors**
```
Error: No module named 'gi'
```
**Solution**:
- This is expected in GitHub Codespaces
- Audio processing continues normally
- For local development, install required system libraries

### **Performance Tips** ⚡
- Use **Standard_S0** tier for production workloads
- Consider **Free tier** limitations for development
- **Network latency** affects real-time translation speed

---

## 🎓 Learning Objectives

After completing this project, you'll understand:

- 🎤 **Speech Recognition**: Converting audio to text
- 🌐 **Language Translation**: Multi-language text translation  
- 🔊 **Speech Synthesis**: Text-to-speech with neural voices
- 🇪🇬 **Regional Voices**: Using dialect-specific voices (Egyptian Arabic)
- 🔄 **Real-time Processing**: Chaining speech services together
- 🛠️ **Azure Integration**: Configuring and using Azure AI Speech Services

---

## 🌍 Supported Azure Regions

Ensure your **Azure Speech Service** is deployed in a supported region:
- **US**: East US, West US 2, Central US
- **Europe**: West Europe, North Europe
- **Asia**: East Asia, Southeast Asia
- **Middle East**: UAE North *(recommended for Arabic)*

---

## 🔗 Additional Resources

- [Azure AI Speech Documentation](https://docs.microsoft.com/azure/cognitive-services/speech-service/)
- [Neural Voice Gallery](https://speech.microsoft.com/portal/voicegallery)
- [Language Support Matrix](https://docs.microsoft.com/azure/cognitive-services/speech-service/language-support)
- [Egyptian Arabic Voice Samples](https://speech.microsoft.com/portal/voicegallery)

---

## 💡 Next Steps

1. **🎤 Try Microphone Input**: Uncomment microphone configuration for live speech
2. **🌍 Add More Languages**: Extend the voices dictionary with additional languages
3. **📱 Build UI Interface**: Create a graphical interface for the translator
4. **🎵 Custom Audio**: Use your own audio files for testing
5. **🔊 Voice Customization**: Experiment with SSML for advanced speech control

---

**🎉 Happy Translating! Enjoy exploring multi-language speech translation with authentic Egyptian Arabic voices! 🇪🇬**
