# 🌍 Azure AI Translator SDK Project

## 🚀 Project Overview

This project demonstrates how to use the **Azure AI Translator SDK** for real-time text translation. The application provides an interactive command-line interface that allows users to translate text from any language to their target language of choice, supporting 137+ languages worldwide.

## 🧠 What Does This Code Do?

The `translate.py` script performs the following operations:

1. **🔧 Configuration Loading**: Loads translator key and region from `.env` file
2. **🔗 Azure Connection**: Establishes connection to Azure Translator Service using SDK
3. **🌐 Language Discovery**: Fetches all supported languages (137+ languages)
4. **🎯 Target Selection**: Prompts user to select target language for translation
5. **💬 Interactive Translation**: Provides continuous translation until user types 'quit'
6. **🔍 Language Detection**: Automatically detects source language of input text
7. **📊 Results Display**: Shows original text, detected language, and translation

## 🏗️ Azure Infrastructure Setup

### 📋 Prerequisites

You only need to set up one Azure resource:

#### 🧠 Azure Translator Service
- Create an **Azure Translator** resource in Azure Portal
- **❗ Important**: Note down the **Key** and **Region** (no endpoint needed!)
- The service supports 137+ languages for translation
- Free tier available with generous monthly limits

### 🔑 Authentication Requirements
Unlike other Azure AI services, the Translator SDK only requires:
- **🗝️ Translator Key**: Your service key (Key1 or Key2)
- **🌍 Region**: The Azure region where your service is deployed (e.g., 'westus2')
- **❌ No Endpoint Required**: The SDK automatically handles the endpoint

## 🛠️ Project Setup

### Step 1: Navigate to Project Directory 📁
```bash
cd /workspaces/mslearn-ai-language/Labfiles/06b-translator-sdk/Python/translate-text
```

### Step 2: Create Virtual Environment 🐍
```bash
python -m venv labenv
```

### Step 3: Activate Virtual Environment ⚡
```bash
source labenv/bin/activate
```

### Step 4: Install Dependencies 📦
```bash
pip install -r requirements.txt
```

## 📋 Dependencies

The project requires the following Python packages (defined in `requirements.txt`):

```
python-dotenv
azure-ai-translation-text==1.0.0b1
```

## ⚙️ Environment Configuration

Create or update the `.env` file in the project directory:

```properties
TRANSLATOR_KEY=your_translator_key_here
TRANSLATOR_REGION=westus2
```

**Note**: Replace `your_translator_key_here` with your actual Azure Translator key, and update the region if different.

## 📁 Project Structure

```
translate-text/
├── translate.py
├── .env
├── requirements.txt
├── labenv/ (virtual environment)
└── README.md
```

## 🏃‍♂️ How to Run

1. **Ensure your virtual environment is activated:**
   ```bash
   source labenv/bin/activate
   ```

2. **Run the translation script:**
   ```bash
   python translate.py
   ```

3. **Follow the interactive prompts:**
   - Select target language (e.g., 'es' for Spanish, 'fr' for French)
   - Enter text to translate
   - Type 'quit' to exit

## 📋 Sample Session

```
137 languages supported.
(See https://learn.microsoft.com/azure/ai-services/translator/language-support#translation)
Enter a target language code for translation (for example, 'en'):
es
Enter text to translate ('quit' to exit):
man
'man' was translated from en to es as 'hombre'.
Enter text to translate ('quit' to exit):
Hello, how are you?
'Hello, how are you?' was translated from en to es as 'Hola, ¿cómo estás?'.
Enter text to translate ('quit' to exit):
quit
```

## 🔍 Code Explanation

### 🏗️ Core Components

#### 1. **Configuration Setup** 🔧
```python
load_dotenv()
translatorRegion = os.getenv('TRANSLATOR_REGION')
translatorKey = os.getenv('TRANSLATOR_KEY')
```
- Loads environment variables from `.env` file
- Retrieves translator key and region

#### 2. **Client Initialization** 🔗
```python
credential = TranslatorCredential(translatorKey, translatorRegion)
client = TextTranslationClient(credential)
```
- Creates translator credentials with key and region
- Initializes the Text Translation client

#### 3. **Language Support Discovery** 🌍
```python
languagesResponse = client.get_languages(scope="translation")
print("{} languages supported.".format(len(languagesResponse.translation)))
```
- Fetches all supported languages from Azure
- Displays count (137+ languages)

#### 4. **Target Language Validation** ✅
```python
while supportedLanguage == False:
    targetLanguage = input()
    if targetLanguage in languagesResponse.translation.keys():
        supportedLanguage = True
    else:
        print("{} is not a supported language.".format(targetLanguage))
```
- Validates user input against supported languages
- Continues prompting until valid language code is entered

#### 5. **Translation Process** 🔄
```python
input_text_elements = [InputTextItem(text=inputText)]
translationResponse = client.translate(content=input_text_elements, to=[targetLanguage])
translation = translationResponse[0] if translationResponse else None
```
- Wraps input text in required format
- Calls Azure Translator API
- Processes response for display

#### 6. **Language Detection & Output** 🔍
```python
sourceLanguage = translation.detected_language
for translated_text in translation.translations:
    print(f"'{inputText}' was translated from {sourceLanguage.language} to {translated_text.to} as '{translated_text.text}'.")
```
- Automatically detects source language
- Displays original text, source language, target language, and translation

## 🌍 Supported Languages

The Azure Translator supports 137+ languages including:

### Popular Languages 🔥
- **English** (en) - English
- **Spanish** (es) - Español  
- **French** (fr) - Français
- **German** (de) - Deutsch
- **Chinese** (zh) - 中文
- **Japanese** (ja) - 日本語
- **Korean** (ko) - 한국어
- **Arabic** (ar) - العربية
- **Russian** (ru) - Русский
- **Portuguese** (pt) - Português

### Regional Variants 🗺️
- **zh-Hans** - Chinese Simplified
- **zh-Hant** - Chinese Traditional
- **pt-BR** - Portuguese (Brazil)
- **pt-PT** - Portuguese (Portugal)
- **en-US** - English (United States)
- **en-GB** - English (United Kingdom)

For complete list: [Azure Translator Language Support](https://learn.microsoft.com/azure/ai-services/translator/language-support#translation)

## ⚠️ Important Notes

- **🔐 Security**: Never commit your `.env` file to version control
- **🌍 No Endpoint**: Unlike other Azure services, Translator SDK doesn't require an endpoint
- **🔑 Key & Region Only**: Only translator key and region are needed for authentication
- **🔍 Auto-Detection**: Source language is automatically detected
- **💰 Cost Management**: Monitor usage to stay within free tier limits
- **📏 Text Limits**: Be aware of character limits per request
- **🌐 Internet Required**: Active internet connection needed for translation

## 🚨 Troubleshooting

### Common Issues:

1. **Authentication Error**: 
   - Verify your translator key is correct
   - Check that the region matches your Azure resource

2. **Unsupported Language Error**:
   - Use correct language codes (e.g., 'es' not 'spanish')
   - Check the official language support documentation

3. **Virtual Environment Issues**:
   ```bash
   # Check if virtual environment is active
   which python
   
   # Verify dependencies are installed
   pip list | grep azure
   ```

4. **Module Import Error**:
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

5. **Network Connection**:
   - Ensure stable internet connection
   - Check if Azure services are accessible from your network

## 🎯 Use Cases

This translator application is perfect for:

- 🗣️ **Language Learning**: Practice with translations
- 📝 **Content Localization**: Translate documents and text
- 💬 **Communication**: Bridge language barriers in conversations
- 🌐 **Web Development**: Integrate translation into applications
- 📚 **Research**: Analyze text in multiple languages
- 🏢 **Business**: International communication and documentation

## 🤝 Contributing

Enhance this project by:
- Adding batch translation capabilities
- Implementing file translation (text files, documents)
- Creating a GUI interface with tkinter or web framework
- Adding translation history and favorites
- Implementing voice-to-text + translation pipeline
- Adding confidence scores and alternative translations

## 🔄 Advanced Features

### Batch Translation Example:
```python
texts = ["Hello", "World", "How are you?"]
input_items = [InputTextItem(text=text) for text in texts]
responses = client.translate(content=input_items, to=['es', 'fr'])
```

### Multiple Target Languages:
```python
# Translate to multiple languages at once
translationResponse = client.translate(
    content=input_text_elements, 
    to=['es', 'fr', 'de', 'ja']
)
```

## 📚 Additional Resources

- [Azure Translator Documentation](https://docs.microsoft.com/azure/cognitive-services/translator/)
- [Azure Translator SDK Documentation](https://docs.microsoft.com/python/api/azure-ai-translation-text/)
- [Language Support Reference](https://learn.microsoft.com/azure/ai-services/translator/language-support)
- [Translator REST API](https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-reference)
- [Best Practices for Translation](https://docs.microsoft.com/azure/cognitive-services/translator/translator-text-features)

## 🎉 Next Steps

1. **Explore More Features**: Try document translation and custom models
2. **Build Applications**: Integrate into web apps or mobile applications
3. **Language Detection**: Use standalone language detection features
4. **Custom Training**: Create domain-specific translation models
5. **Production Deployment**: Scale for production workloads

---

**Happy Translating! 🎉🌍**