# 🧠 Azure AI Language Text Analysis Project

## 📋 Overview
This Python project demonstrates how to use **Azure AI Language** services to analyze text content. The application processes hotel reviews and performs various text analytics operations including language detection, sentiment analysis, key phrase extraction, and entity recognition.

## 🚀 Features
- 🌍 **Language Detection**: Automatically detect the language of text
- 😊 **Sentiment Analysis**: Determine if text is positive, negative, or neutral
- 🔑 **Key Phrase Extraction**: Extract important phrases and topics
- 🏷️ **Entity Recognition**: Identify people, places, organizations, and other entities
- 🔗 **Linked Entity Recognition**: Find entities with Wikipedia links

## 📁 Project Structure
```
Python/
├── README.md                   # This file
├── text-analysis/
│   ├── text-analysis.py       # Main Python script
│   ├── .env                    # Environment configuration (you need to create this)
│   ├── requirements.txt        # Python dependencies
│   └── reviews/               # Sample text files for analysis
│       ├── review1.txt        # English hotel review (positive)
│       ├── review2.txt        # English hotel review (negative)
│       ├── review3.txt        # English hotel review
│       ├── review4.txt        # English hotel review
│       └── review5.txt        # French hotel review
```

## ⚙️ Setup Instructions

### 1. 🏗️ Create Azure AI Language Resource

1. Go to the [Azure Portal](https://portal.azure.com)
2. Click **"Create a resource"**
3. Search for **"Language"** and select **"Language service"**
4. Click **"Create"**
5. Fill in the details:
   - **Subscription**: Your Azure subscription
   - **Resource Group**: Create new or use existing
   - **Region**: Choose a region near you (e.g., East US, West Europe)
   - **Name**: Give your resource a unique name
   - **Pricing Tier**: Choose **Free (F0)** for learning or **Standard (S)** for production

### 2. 🔑 Get Your Credentials

After your resource is deployed:

1. Go to your **Language service** resource in the Azure Portal
2. Click on **"Keys and Endpoint"** in the left menu
3. Copy the following values:
   - **📍 Endpoint**: Something like `https://your-resource-name.cognitiveservices.azure.com/`
   - **🔐 Key 1**: A long string of characters (keep this secret!)

### 3. 🐍 Environment Setup

1. **Navigate to the project directory**:
   ```bash
   cd /workspaces/mslearn-ai-language/Labfiles/01-analyze-text/Python/text-analysis
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   ```

3. **Install dependencies**:
   ```bash
   pip install python-dotenv azure-ai-textanalytics==5.3.0
   ```

4. **Create environment file**:
   ```bash
   cp .env.example .env  # If example exists, or create new file
   ```

5. **Edit the `.env` file** with your Azure credentials:
   ```env
   AI_SERVICE_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com/
   AI_SERVICE_KEY=your-key-1-value-here
   ```

## 🏃‍♂️ Running the Application

1. **Make sure you're in the correct directory**:
   ```bash
   cd /workspaces/mslearn-ai-language/Labfiles/01-analyze-text/Python/text-analysis
   ```

2. **Run the script**:
   ```bash
   python text-analysis.py
   ```

## 📊 Expected Output

The application will process each review file and display:

```
-------------
review1.txt

Good Hotel and staff
The Royal Hotel, London, UK
...

Language: English

Sentiment: positive

Key Phrases:
    good service
    great location
    Buckingham Palace
    Westminster Abbey
    ...

Entities
    Royal Hotel (Location)
    London (Location)
    UK (Location)
    Buckingham Palace (Location)
    ...

Links
    Buckingham Palace (https://en.wikipedia.org/wiki/Buckingham_Palace)
    Westminster Abbey (https://en.wikipedia.org/wiki/Westminster_Abbey)
    ...
```

## 🔧 Code Explanation

### Main Components:

1. **🔗 Client Creation**:
   ```python
   credential = AzureKeyCredential(ai_key)
   ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)
   ```

2. **📁 File Processing**:
   ```python
   for file_name in os.listdir(reviews_folder):
       text = open(os.path.join(reviews_folder, file_name), encoding='utf8').read()
   ```

3. **🌍 Language Detection**:
   ```python
   detectedLanguage = ai_client.detect_language(documents=[text])[0]
   ```

4. **😊 Sentiment Analysis**:
   ```python
   sentimentAnalysis = ai_client.analyze_sentiment(documents=[text])[0]
   ```

5. **🔑 Key Phrase Extraction**:
   ```python
   phrases = ai_client.extract_key_phrases(documents=[text])[0].key_phrases
   ```

6. **🏷️ Entity Recognition**:
   ```python
   entities = ai_client.recognize_entities(documents=[text])[0].entities
   ```

## 🛠️ Troubleshooting

### Common Issues:

1. **❌ "Invalid API Key" Error**:
   - Check that your `AI_SERVICE_KEY` in `.env` is correct
   - Ensure no extra spaces or quotes around the key

2. **❌ "Endpoint not found" Error**:
   - Verify your `AI_SERVICE_ENDPOINT` URL is correct
   - Make sure it ends with `/`

3. **❌ "Module not found" Error**:
   - Run `pip install -r requirements.txt`
   - Make sure your virtual environment is activated

4. **❌ "Reviews folder not found"**:
   - Ensure you're running the script from the `text-analysis` directory
   - Check that the `reviews` folder exists

## 📚 Azure Resources Used

- **🧠 Azure AI Language**: Multi-language text analytics service
- **🔐 Azure Key Credential**: Secure authentication
- **📊 Text Analytics Client**: Python SDK for Azure AI Language

## 📖 Learn More

- 📘 [Azure AI Language Documentation](https://learn.microsoft.com/azure/ai-services/language-service/)
- 🐍 [Python SDK Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-textanalytics-readme)
- 💡 [Text Analytics Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics/samples)

## 🔒 Security Notes

- ⚠️ Never commit your `.env` file to version control
- 🔐 Keep your API keys secure and rotate them regularly
- 🌐 Use environment variables in production

## 📄 License

This project is part of Microsoft Learn AI Language exercises.

---

## 🎯 Quick Start Checklist

- [ ] ✅ Created Azure AI Language resource
- [ ] 📋 Copied endpoint and key from Azure Portal
- [ ] 📝 Created `.env` file with credentials
- [ ] 🐍 Installed Python dependencies
- [ ] 🏃‍♂️ Successfully ran `python text-analysis.py`

Happy analyzing! 🎉
