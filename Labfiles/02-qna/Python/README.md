# 🤖 Azure AI Language QnA Service Project

## 📋 Overview
This Python project demonstrates how to use **Azure AI Language's Question Answering** service to create an interactive Q&A application. The application connects to your custom QnA knowledge base and provides intelligent answers to user questions with confidence scores.

## 🚀 Features
- 🧠 **Interactive Q&A**: Ask questions and get intelligent answers
- 💯 **Confidence Scoring**: See how confident the AI is in its answers
- 🔄 **Continuous Chat**: Keep asking questions until you type 'quit'
- ⚡ **Real-time Processing**: Get instant responses from your knowledge base
- 🛡️ **Error Handling**: Robust error handling for better user experience

## 📁 Project Structure
```
Python/
├── README.md                   # This comprehensive guide
├── qna-app/
│   ├── qna-app.py             # Main Python application
│   ├── .env                   # Environment configuration (you need to create this)
│   └── requirements.txt       # Python dependencies
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
   - **Name**: Give your resource a unique name (e.g., `my-qna-service`)
   - **Pricing Tier**: **Free (F0)** for learning or **Standard (S)** for production
5. **Create**: Click **"Review + create"** then **"Create"**

### 2. 🔑 Get Service Credentials

After deployment:
1. Go to your **Language service** resource
2. Click **"Keys and Endpoint"** in the left sidebar
3. **Copy these values**:
   - **📍 Endpoint**: `https://your-service-name.cognitiveservices.azure.com/`
   - **🔐 Key 1**: Your secret API key (keep this secure!)

### 3. 📚 Create Custom QnA Project

1. **Go to Language Studio**: Visit [language.cognitive.azure.com](https://language.cognitive.azure.com)
2. **Sign in** with your Azure account
3. **Select your Language resource**
4. **Create QnA Project**:
   - Click **"Create new"** → **"Custom question answering"**
   - **Project name**: `custom-qa` (or your preferred name)
   - **Language**: English (or your preferred language)
   - **Description**: Add a meaningful description
5. **Add QnA pairs** to your knowledge base
6. **Train** your model
7. **Deploy** your model

### 4. 🚀 Get Deployment Information

After deploying your model:
1. **In Language Studio**: Go to your QnA project
2. **Click "Deploy knowledge base"**
3. **Click "Get prediction URL"**
4. **Copy these values**:
   - **Project Name**: Usually `custom-qa`
   - **Deployment Name**: Usually `production` or the name you chose

## 🐍 Python Environment Setup

### Step 1: Navigate to Project Directory
```bash
cd /workspaces/mslearn-ai-language/Labfiles/02-qna/Python/qna-app
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
```

### Step 5: Create Environment File
Create a `.env` file in the `qna-app` directory:
```bash
touch .env
```

### Step 6: Configure Environment Variables
Edit the `.env` file with your Azure credentials:
```env
AI_SERVICE_ENDPOINT=https://your-service-name.cognitiveservices.azure.com/
AI_SERVICE_KEY=your-key-1-here
QA_PROJECT_NAME=custom-qa
QA_DEPLOYMENT_NAME=production
```

## 📦 Dependencies (requirements.txt)

The project requires these packages:
```txt
python-dotenv
azure-ai-textanalytics==5.3.0
```

**⚠️ Important**: The `azure-ai-textanalytics==5.3.0` package is crucial for compatibility and must be included!

## 🏃‍♂️ Running the Application

1. **Ensure virtual environment is active**:
   ```bash
   source labenv/bin/activate
   ```

2. **Run the application**:
   ```bash
   python qna-app.py
   ```

3. **Start asking questions**!

## 📊 Expected Output

```
✅ Azure QnA service is ready. Type your question or type 'quit' to exit.

Question:
What is Azure AI?

🧠 Answer: Azure AI is Microsoft's comprehensive suite of artificial intelligence services and tools that enable developers to build intelligent applications with capabilities like vision, speech, language understanding, and decision making.
💯 Confidence Score: 0.95

Question:
How do I create a storage account?

🧠 Answer: To create an Azure Storage account, go to the Azure portal, click 'Create a resource', search for 'Storage account', fill in the required details like subscription, resource group, and account name, then click 'Create'.
💯 Confidence Score: 0.87

Question:
quit

👋 Exiting.
```

## 🔧 Code Explanation

### 📚 **Imports and Setup**
```python
from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient
```
- `dotenv`: Loads environment variables from `.env` file
- `azure.ai.language.questionanswering`: Azure SDK for QnA service

### 🔐 **Environment Configuration**
```python
load_dotenv()
ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
ai_key = os.getenv('AI_SERVICE_KEY')
ai_project_name = os.getenv('QA_PROJECT_NAME')
ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')
```
Loads sensitive configuration from environment variables for security.

### 🔗 **Azure Client Creation**
```python
credential = AzureKeyCredential(ai_key)
ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)
```
Creates an authenticated client to communicate with Azure QnA service.

### 🔄 **Interactive Loop** (Enhanced Version)
```python
print("✅ Azure QnA service is ready. Type your question or type 'quit' to exit.")
while True:
    user_question = input('\nQuestion:\n')
    if user_question.strip().lower() == "quit":
        print("👋 Exiting.")
        break

    response = ai_client.get_answers(
        question=user_question,
        project_name=ai_project_name,
        deployment_name=ai_deployment_name
    )

    if response.answers:
        top_answer = response.answers[0]
        print(f"\n🧠 Answer: {top_answer.answer}")
        print(f"💯 Confidence Score: {top_answer.confidence:.2f}")
    else:
        print("❌ No answer found.")
```

**🆕 Enhanced Features Added:**
- ✅ User-friendly startup message
- 💬 Clear prompts for questions
- 🔄 Continuous conversation loop
- 👋 Graceful exit with 'quit' command
- 💯 Confidence score display
- ❌ Proper handling when no answers found

## 🛠️ Troubleshooting

### **❌ Common Issues & Solutions:**

1. **"Module not found" Error**:
   ```bash
   source labenv/bin/activate
   pip install -r requirements.txt
   ```

2. **"Authentication failed" Error**:
   - Verify `AI_SERVICE_KEY` is correct
   - Check `AI_SERVICE_ENDPOINT` format
   - Ensure no extra spaces in `.env` file

3. **"Project not found" Error**:
   - Verify `QA_PROJECT_NAME` matches your Language Studio project
   - Check `QA_DEPLOYMENT_NAME` matches your deployed model

4. **"No answers found" repeatedly**:
   - Ensure your QnA project has knowledge base pairs
   - Check if your model is properly trained and deployed
   - Try asking questions that match your knowledge base content

5. **Environment activation issues**:
   ```bash
   # If activation fails, recreate the environment
   rm -rf labenv
   python -m venv labenv
   source labenv/bin/activate
   ```

## 🔒 Security Best Practices

- 🚫 **Never commit `.env` files** to version control
- 🔐 **Keep API keys secure** and rotate them regularly
- 🌐 **Use environment variables** in production environments
- 📝 **Add `.env` to `.gitignore`**

## 📈 Next Steps

1. **🔧 Customize Knowledge Base**: Add more QnA pairs relevant to your domain
2. **⚡ Optimize Performance**: Fine-tune confidence thresholds
3. **🎨 Enhance UI**: Add web interface with Flask/Django
4. **📊 Add Analytics**: Track common questions and improve answers
5. **🔗 Integration**: Connect to chatbots or web applications

## 📚 Azure Resources Used

- **🧠 Azure AI Language Service**: Core QnA functionality
- **📚 Custom Question Answering**: Knowledge base management
- **🔐 Azure Key Credential**: Secure authentication
- **🐍 Python SDK**: Azure AI Language client library

## 📖 Additional Resources

- 📘 [Azure QnA Documentation](https://learn.microsoft.com/azure/ai-services/language-service/question-answering/)
- 🐍 [Python SDK Reference](https://learn.microsoft.com/python/api/azure-ai-language-questionanswering/)
- 🎓 [Language Studio Tutorial](https://learn.microsoft.com/azure/ai-services/language-service/question-answering/quickstart/sdk)
- 💡 [Best Practices Guide](https://learn.microsoft.com/azure/ai-services/language-service/question-answering/concepts/best-practices)

## 🎯 Quick Start Checklist

- [ ] ✅ Created Azure AI Language service
- [ ] 📋 Copied endpoint and Key 1 from Azure Portal
- [ ] 📚 Created Custom QnA project in Language Studio
- [ ] 🚀 Deployed model and got project/deployment names
- [ ] 🐍 Created virtual environment (`python -m venv labenv`)
- [ ] ⚡ Activated environment (`source labenv/bin/activate`)
- [ ] 📦 Installed dependencies (`pip install -r requirements.txt`)
- [ ] 📝 Created and configured `.env` file
- [ ] 🏃‍♂️ Successfully ran `python qna-app.py`

## 🎉 Success!

If everything is set up correctly, you should see:
```
✅ Azure QnA service is ready. Type your question or type 'quit' to exit.
```

Now you can start asking questions and get intelligent answers from your custom knowledge base! 🚀

---

**💡 Pro Tip**: The more comprehensive and well-structured your knowledge base, the better the answers will be!

Happy questioning! 🎊
