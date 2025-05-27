# 🎧 Azure AI Audio Chat Application

## 🚀 Overview
This is a **revolutionary audio chat application** that uses Azure AI to analyze and understand audio content! 🎵✨ The application processes audio files and answers questions about their content using multimodal AI capabilities.

## 🎯 What This Application Does
- 🎤 **Processes audio files** (MP3 format)
- 💬 **Interactive chat interface** for asking questions about audio content
- 🤖 **AI-powered responses** using Azure's Phi-4 multimodal model
- 🔄 **Real-time audio analysis** and conversation

## ⚠️ Important Setup Notes

### 🏢 Azure AI Foundry Setup
**CRITICAL**: When creating your project in Azure AI Foundry:
- ✅ **Choose "AI Hub"** instead of "AI Resource Foundry"
- ❌ **DO NOT use "AI Resource Foundry"** - it doesn't provide connection strings!
- 🔗 You need the proper connection string format for the PROJECT_ENDPOINT

### 📦 Version Requirements
This application requires **specific versions** to work correctly:
- 🔧 `azure-ai-projects==1.0.0b9`
- 🔧 `azure-ai-inference==1.0.0b9`

**Why these versions?** 🤔
- ❌ `azure-ai-inference==1.0.0b3` causes: `Session.request() got an unexpected keyword argument 'model'`
- ❌ Older versions cause: `'str' object has no attribute 'items'AudioContentItem`
- ✅ Version `1.0.0b9` fixes all these issues!

## 📋 Requirements

### 🐍 Python Dependencies
```txt
python-dotenv
azure-identity
azure-ai-projects==1.0.0b9
azure-ai-inference==1.0.0b9
```

### 🔐 Environment Variables
Create a `.env` file with:
```properties
PROJECT_ENDPOINT="your-azure-ai-project-connection-string"
MODEL_DEPLOYMENT="Phi-4-multimodal-instruct"
```

## 🛠️ Installation

1. **Install dependencies** 📦:
```bash
pip install -r requirements.txt
```

2. **Configure environment** ⚙️:
   - Set up your Azure AI project in AI Foundry (choose AI Hub!)
   - Copy your connection string to `.env` file
   - Ensure you have the Phi-4-multimodal-instruct model deployed

## 🎮 How to Run

```bash
python audio-chat.py
```

## 🔍 Code Explanation with Emojis

### 📚 Imports Section
```python
import os  # 🖥️ Operating system interface

# 🔐 Authentication and configuration
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential

# 🤖 Azure AI services
from azure.ai.projects import AIProjectClient
from azure.ai.inference.models import (
     SystemMessage,    # 🎭 System instructions for AI
     UserMessage,      # 👤 User input messages
     TextContentItem,  # 📝 Text content handling
)
```

### 🏗️ Main Function Breakdown

#### 1. 🧹 Console Clearing
```python
os.system('cls' if os.name=='nt' else 'clear')
```
- 🪟 Clears Windows console (`cls`) 
- 🐧 Clears Linux/Mac console (`clear`)

#### 2. ⚙️ Configuration Loading
```python
load_dotenv()  # 📁 Load environment variables
project_connection = os.getenv("PROJECT_ENDPOINT")  # 🔗 Get connection string
model_deployment = os.getenv("MODEL_DEPLOYMENT")    # 🤖 Get model name
```

#### 3. 🔌 Client Initialization
```python
# 🏢 Create project client with authentication
project_client = AIProjectClient.from_connection_string(
    conn_str=project_connection,
    credential=DefaultAzureCredential()
)

# 💬 Get chat client for the specific model
chat_client = project_client.inference.get_chat_completions_client(model=model_deployment)
```

#### 4. 🎭 System Message Setup
```python
system_message = "You are an AI assistant for a produce supplier company."
```
- 🏪 Sets the AI's role as a produce supplier assistant
- 🍓 Perfect for analyzing customer voice messages about food orders!

#### 5. 🔄 Interactive Chat Loop
```python
while True:  # 🔁 Infinite loop for continuous chat
    prompt = input("\nAsk a question about the audio\n(or type 'quit' to exit)\n")
    
    if prompt.lower() == "quit":  # 🚪 Exit condition
        break
    elif len(prompt) == 0:        # ❌ Empty input validation
        print("Please enter a question.\n")
    else:                         # ✅ Process valid input
        print("Getting a response ...\n")
```

#### 6. 🎵 Audio Processing Magic
```python
# 🌐 Audio file URL (strawberry customer message)
file_path = "https://github.com/MicrosoftLearning/mslearn-ai-language/raw/refs/heads/main/Labfiles/09-audio-chat/data/fresas.mp3"

# 🤖 Send multimodal request (text + audio)
response = chat_client.complete(
    messages=[
        SystemMessage(system_message),  # 🎭 AI role
        UserMessage([
            TextContentItem(text=prompt),  # 📝 User question
            {
                "type": "audio_url",       # 🎵 Audio content type
                "audio_url": {"url": file_path}  # 🔗 Audio file location
            }
        ])
    ]
)

# 💬 Display AI response
print(response.choices[0].message.content)
```

## 🎯 Sample Usage & Output

### 📝 Example Interaction 1:
```
Ask a question about the audio
(or type 'quit' to exit)
 Can you summarize this customer's voice message? Is it time-sensitive?
Getting a response ...

The customer is requesting two deliveries of strawberries this Friday before the spring festival, not emergency.
```

### 📝 Example Interaction 2:
```
Ask a question about the audio
(or type 'quit' to exit)
 Can you summarize this customer's voice message?
Getting a response ...

This customer is a local bakery from Kelly.
```

## 🎵 Audio File Information
- 📁 **File**: `fresas.mp3` (Spanish for "strawberries")
- 🍓 **Content**: Customer voice message about strawberry delivery
- 🏪 **Context**: Local bakery requesting produce delivery
- ⏰ **Timing**: Before spring festival (time-sensitive)

## 🔧 Troubleshooting

### ❌ Common Errors & Solutions:

1. **`Session.request() got an unexpected keyword argument 'model'`**
   - 🔧 **Solution**: Update to `azure-ai-inference==1.0.0b9`

2. **`'str' object has no attribute 'items'AudioContentItem`**
   - 🔧 **Solution**: Use `azure-ai-inference==1.0.0b9`

3. **Connection string issues**
   - 🔧 **Solution**: Use AI Hub (not AI Resource Foundry) in Azure AI Foundry
   - ✅ Correct format: `"region.api.azureml.ms;subscription-id;resource-group;project-name"`

4. **Model not found**
   - 🔧 **Solution**: Ensure `Phi-4-multimodal-instruct` is deployed in your Azure AI project

## 🌟 Key Features

- 🎤 **Multimodal AI**: Processes both text and audio simultaneously
- 🔄 **Interactive**: Continuous conversation about audio content
- 🍓 **Domain-specific**: Optimized for produce supplier business
- 🌐 **Cloud-powered**: Uses Azure's latest AI capabilities
- 🔐 **Secure**: Proper authentication with Azure credentials

## 💡 Use Cases

- 📞 **Customer Service**: Analyze customer voice messages
- 📋 **Order Processing**: Extract order details from audio
- 🕐 **Priority Assessment**: Determine urgency of requests
- 📊 **Business Intelligence**: Understand customer needs from voice data

## 🎉 Success Indicators

When working correctly, you should see:
- ✅ Clean console startup
- ✅ Successful Azure connection
- ✅ Prompt for audio questions
- ✅ Meaningful AI responses about audio content
- ✅ Continuous chat capability

---

🎯 **Happy Audio Chatting!** 🚀✨
