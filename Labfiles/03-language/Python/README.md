# 🕐 Azure AI Language Understanding - Clock Client Project

## 📋 Overview
This Python project demonstrates how to use **Azure AI Language's Conversational Language Understanding (CLU)** service to create an intelligent clock application. Unlike Q&A services, this project uses **custom conversation models** to understand user intents and extract entities from natural language requests about time, dates, and days.

## 🚀 Features
- 🕒 **Time Queries**: Get current time for different locations worldwide
- 📅 **Date Queries**: Find dates for specific weekdays
- 🗓️ **Day Queries**: Determine what day of the week a specific date falls on
- 🧠 **Intent Recognition**: Understands natural language requests
- 🏷️ **Entity Extraction**: Identifies locations, dates, and weekdays from user input
- 💯 **Confidence Scoring**: Shows how confident the AI is in its predictions
- 🌍 **Multi-timezone Support**: Supports major cities around the world

## 📁 Project Structure
```
Python/
├── README.md                   # This comprehensive guide
├── clock-client/
│   ├── clock-client.py        # Main Python application
│   ├── .env                   # Environment configuration
│   ├── requirements.txt       # Python dependencies
│   └── labenv/               # Virtual environment (created after setup)
```

## ⚙️ Complete Setup Instructions

### 1. 🏗️ Create Azure AI Language Resource

1. **Go to Azure Portal**: Navigate to [portal.azure.com](https://portal.azure.com)
2. **Create Resource**: Click **"Create a resource"**
3. **Search**: Look for **"Language service"** and select it
4. **Configure**:
   - **Subscription**: Your Azure subscription
   - **Resource Group**: Create new or use existing
   - **Region**: Choose a region near you
   - **Name**: Give your resource a unique name (e.g., `my-language-service`)
   - **Pricing Tier**: **Free (F0)** for learning or **Standard (S)** for production
5. **Create**: Click **"Review + create"** then **"Create"**

### 2. 🔑 Get Service Credentials

After deployment:
1. Go to your **Language service** resource
2. Click **"Keys and Endpoint"** in the left sidebar
3. **Copy these values**:
   - **📍 Endpoint**: `https://your-service-name.cognitiveservices.azure.com/`
   - **🔐 Key 1**: Your secret API key (keep this secure!)

### 3. 🗣️ Create Conversational Language Understanding Project

**⚠️ Important**: This is **NOT a Custom Q&A project**. This is a **Conversational Language Understanding** project for intent recognition!

1. **Go to Language Studio**: Visit [language.cognitive.azure.com](https://language.cognitive.azure.com)
2. **Sign in** with your Azure account
3. **Select your Language resource**
4. **Create CLU Project**:
   - Click **"Create new"** → **"Conversational language understanding"**
   - **Project name**: `Clock` (exactly as shown in the code)
   - **Language**: English
   - **Description**: "Clock application for time and date queries"
   
5. **Define Intents**:
   - **GetTime**: For time-related queries
   - **GetDate**: For date-related queries  
   - **GetDay**: For day-of-week queries

6. **Define Entities**:
   - **Location**: For city/location names
   - **Date**: For specific dates
   - **Weekday**: For days of the week

7. **Add Training Utterances**:
   - "What time is it?"
   - "What time is it in London?"
   - "What's the date next Monday?"
   - "What day is 12/25/2024?"

8. **Train and Deploy** your model to **production** slot

## 🐍 Python Environment Setup

### Step 1: Navigate to Project Directory
```bash
cd /workspaces/mslearn-ai-language/Labfiles/03-language/Python/clock-client
```

### Step 2: Create Virtual Environment
```bash
python -m venv labenv
```

### Step 3: Activate Virtual Environment
```bash
source labenv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
pip install python-dateutil
```

**⚠️ Critical**: The `python-dateutil` package is **essential** for date parsing functionality and must be installed!

### Step 5: Configure Environment Variables
Edit the `.env` file with your Azure credentials:
```env
LS_CONVERSATIONS_ENDPOINT=https://your-service-name.cognitiveservices.azure.com/
LS_CONVERSATIONS_KEY=your-key-1-here
```

**🔍 Key Differences from Q&A Projects:**
- Uses `LS_CONVERSATIONS_ENDPOINT` and `LS_CONVERSATIONS_KEY`
- **NO** `QA_PROJECT_NAME` or `QA_DEPLOYMENT_NAME` needed
- Project name is hardcoded as `'Clock'` in the code
- Deployment slot is hardcoded as `'production'`

## 📦 Dependencies (requirements.txt)

```txt
python-dotenv
azure-ai-language-conversations
python-dateutil  # Essential for date parsing!
```

## 🏃‍♂️ Running the Application

1. **Ensure virtual environment is active**:
   ```bash
   source labenv/bin/activate
   ```

2. **Run the application**:
   ```bash
   python clock-client.py
   ```

3. **Start asking questions**!

## 📊 Expected Output

```
Enter some text ("quit" to stop)
What time is it in London?

view top intent:
	top intent: GetTime
	category: GetTime
	confidence score: 0.95

view entities:
	category: Location
	text: London
	confidence score: 0.88

query: What time is it in London?
14:30

Enter some text ("quit" to stop)
What day is 12/25/2024?

view top intent:
	top intent: GetDay
	category: GetDay
	confidence score: 0.92

view entities:
	category: Date
	text: 12/25/2024
	confidence score: 0.85

query: What day is 12/25/2024?
Wednesday

Enter some text ("quit" to stop)
quit
```

## 🔧 Code Explanation

### 📚 **Imports and Dependencies**
```python
from dotenv import load_dotenv
import os
import json
from datetime import datetime, timedelta, date, timezone
from dateutil.parser import parse as is_date
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient
```

**Key imports:**
- `azure.ai.language.conversations`: For conversational AI (NOT Q&A)
- `python-dateutil`: Essential for advanced date parsing
- `datetime`: Built-in date/time manipulation

### 🔗 **Azure Client Creation**
```python
client = ConversationAnalysisClient(
    ls_prediction_endpoint, AzureKeyCredential(ls_prediction_key))
```

### 🧠 **Conversation Analysis**
```python
result = client.analyze_conversation(
    task={
        "kind": "Conversation",
        "analysisInput": {
            "conversationItem": {
                "participantId": "1",
                "id": "1",
                "modality": "text",
                "language": "en",
                "text": query
            },
            "isLoggingEnabled": False
        },
        "parameters": {
            "projectName": cls_project,  # 'Clock'
            "deploymentName": deployment_slot,  # 'production'
            "verbose": True
        }
    }
)
```

### 🎯 **Intent Processing**
```python
top_intent = result["result"]["prediction"]["topIntent"]
entities = result["result"]["prediction"]["entities"]

if top_intent == 'GetTime':
    # Handle time requests
elif top_intent == 'GetDay':
    # Handle day-of-week requests  
elif top_intent == 'GetDate':
    # Handle date requests
```

### 🌍 **Timezone Support**
The application supports multiple timezones:
- **Local**: System local time
- **London**: UTC time
- **Sydney**: UTC+11
- **New York**: UTC-5
- **Nairobi**: UTC+3
- **Tokyo**: UTC+9
- **Delhi**: UTC+5.5

### 📅 **Date Functions**

**GetTime(location)**: Returns formatted time for specified location
**GetDate(day)**: Gets date for named weekdays (e.g., "Monday", "today")
**GetDay(date_string)**: Returns day of week for a specific date

## 🛠️ Troubleshooting

### **❌ Common Issues & Solutions:**

1. **"Module 'dateutil' not found" Error**:
   ```bash
   pip install python-dateutil
   ```

2. **"Conversation project not found" Error**:
   - Verify your CLU project is named exactly `Clock`
   - Ensure model is deployed to `production` slot
   - Check endpoint and key are correct

3. **"No intent recognized" Error**:
   - Add more training utterances to your CLU model
   - Retrain and redeploy your model
   - Check that intents match: `GetTime`, `GetDate`, `GetDay`

4. **Environment activation issues**:
   ```bash
   source labenv/bin/activate
   # If still issues, recreate environment
   rm -rf labenv
   python -m venv labenv
   source labenv/bin/activate
   pip install -r requirements.txt
   pip install python-dateutil
   ```

5. **Authentication failed**:
   - Verify `.env` file has correct endpoint and key
   - Ensure no extra spaces or quotes in environment variables

## 🔍 Key Differences from Q&A Projects

| Feature | **This Project (CLU)** | **Q&A Projects** |
|---------|------------------------|------------------|
| **Service Type** | 🗣️ Conversational Language Understanding | ❓ Custom Question Answering |
| **Purpose** | 🎯 Intent recognition & entity extraction | 📚 Knowledge base Q&A |
| **Environment Variables** | `LS_CONVERSATIONS_*` | `QA_PROJECT_NAME`, `QA_DEPLOYMENT_NAME` |
| **Project Setup** | Language Studio → CLU | Language Studio → Custom Q&A |
| **Training Data** | Intents & Entities | Question-Answer pairs |
| **Output** | Intents, entities, confidence | Direct answers |

## 🔒 Security Best Practices

- 🚫 **Never commit `.env` files** to version control
- 🔐 **Keep API keys secure** and rotate them regularly
- 📝 **Add `.env` to `.gitignore`**
- 🌐 **Use environment variables** in production

## 📈 Next Steps

1. **🎯 Enhance Intents**: Add more intent types (alarms, reminders)
2. **🌍 Expand Locations**: Add more cities and timezones  
3. **🎨 Improve UI**: Create web interface or voice integration
4. **📊 Add Logging**: Track usage patterns and improve model
5. **🔗 Integration**: Connect to calendar or scheduling systems

## 📚 Azure Resources Used

- **🧠 Azure AI Language Service**: Core conversational AI
- **🗣️ Conversational Language Understanding**: Intent & entity recognition
- **🔐 Azure Key Credential**: Secure authentication
- **🐍 Python SDK**: Azure AI Language conversations client

## 📖 Additional Resources

- 📘 [CLU Documentation](https://learn.microsoft.com/azure/ai-services/language-service/conversational-language-understanding/)
- 🐍 [Python SDK Reference](https://learn.microsoft.com/python/api/azure-ai-language-conversations/)
- 🎓 [Language Studio Tutorial](https://learn.microsoft.com/azure/ai-services/language-service/conversational-language-understanding/quickstart)
- 💡 [Best Practices Guide](https://learn.microsoft.com/azure/ai-services/language-service/conversational-language-understanding/concepts/best-practices)

## 🎯 Quick Start Checklist

- [ ] ✅ Created Azure AI Language service
- [ ] 📋 Copied endpoint and Key 1 from Azure Portal
- [ ] 🗣️ Created **Conversational Language Understanding** project (NOT Q&A!)
- [ ] 🎯 Named project exactly `Clock`
- [ ] 🚀 Deployed model to `production` slot
- [ ] 🐍 Created virtual environment (`python -m venv labenv`)
- [ ] ⚡ Activated environment (`source labenv/bin/activate`)
- [ ] 📦 Installed dependencies (`pip install -r requirements.txt`)
- [ ] 📅 Installed dateutil (`pip install python-dateutil`)
- [ ] 📝 Configured `.env` file with correct variables
- [ ] 🏃‍♂️ Successfully ran `python clock-client.py`

## 🎉 Success!

If everything is set up correctly, you should see:
```
Enter some text ("quit" to stop)
```

Now you can ask questions like:
- "What time is it?"
- "What time is it in Tokyo?"
- "What day is next Friday?"
- "What's the date on Monday?"

Happy conversing! 🕐✨

---

**💡 Pro Tip**: The more diverse training utterances you add to your CLU model, the better it will understand natural language variations!

🎊 **Remember**: This is Conversational AI, not Q&A - it understands intents and extracts entities rather than providing direct answers from a knowledge base!
