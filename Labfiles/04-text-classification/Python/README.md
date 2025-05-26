# 📄 Azure AI Text Classification Project

## 🚀 Project Overview

This project demonstrates how to use **Azure AI Language Services** for custom text classification. The application reads text articles from a local folder and classifies them using a pre-trained custom model deployed in Azure AI Language Studio.

## 🧠 What Does This Code Do?

The `classify-text.py` script performs the following operations:

1. **🔧 Configuration Loading**: Loads environment variables from `.env` file
2. **🔗 Azure Connection**: Establishes connection to Azure AI Language Service
3. **📁 File Processing**: Reads all text files from the `articles` folder
4. **🤖 AI Classification**: Uses custom trained model to classify each document
5. **📊 Results Display**: Shows classification results with confidence scores

## 🏗️ Azure Infrastructure Setup

### 📋 Prerequisites

Before running this project, you need to set up the following Azure resources:

#### 1. 🗄️ Azure Storage Account
- Create a Storage Account in Azure Portal
- **❗ Important**: Set blob access to **anonymous read** for public access
- Upload your training articles to blob containers
- Organize articles into folders like:
  - 📂 `train/sports/` - Training articles for sports category
  - 📂 `train/technology/` - Training articles for technology category  
  - 📂 `test/sports/` - Test articles for sports category
  - 📂 `test/technology/` - Test articles for technology category

#### 2. 🧠 Azure AI Language Service
- Create an Azure AI Language resource
- **❗ Important**: Assign **Cognitive Services Contributor** role to your account
- Note down the endpoint and key

#### 3. 🎯 Custom Classification Project
- Go to Azure AI Language Studio
- Create a new **Custom Text Classification** project
- Connect your Storage Account as data source
- Upload and label your training data
- Train your custom model
- Deploy the model (note the deployment name)

## 🛠️ Project Setup

### 1. 📦 Install Dependencies

```bash
pip install azure-ai-textanalytics python-dotenv
```

### 2. ⚙️ Environment Configuration

Create a `.env` file in the project directory:

```properties
AI_SERVICE_ENDPOINT=https://your-ai-service.cognitiveservices.azure.com/
AI_SERVICE_KEY=your_ai_service_key_here
PROJECT=ClassifyLab
DEPLOYMENT=articles
```

### 3. 📁 Prepare Articles Folder

Create an `articles` folder and add text files you want to classify:

```
classify-text/
├── articles/
│   ├── article1.txt
│   ├── article2.txt
│   └── article3.txt
├── classify-text.py
├── .env
└── README.md
```

## 🏃‍♂️ How to Run

1. **Navigate to the project directory:**
   ```bash
   cd /workspaces/mslearn-ai-language/Labfiles/04-text-classification/Python/classify-text
   ```

2. **Run the classification script:**
   ```bash
   python classify-text.py
   ```

## 📋 Expected Output

```
article1.txt was classified as 'sports' with confidence score 0.95.
article2.txt was classified as 'technology' with confidence score 0.87.
article3.txt was classified as 'business' with confidence score 0.92.
```

## 🏗️ Data Organization Strategy

### 📊 Training Data Structure in Azure Storage

```
your-storage-container/
├── train/
│   ├── sports/
│   │   ├── sports_article_1.txt
│   │   ├── sports_article_2.txt
│   │   └── ...
│   ├── technology/
│   │   ├── tech_article_1.txt
│   │   ├── tech_article_2.txt
│   │   └── ...
│   └── business/
│       ├── business_article_1.txt
│       └── ...
└── test/
    ├── sports/
    ├── technology/
    └── business/
```

### 🎯 Classification Categories

Design your classification system with clear categories such as:
- 🏈 **Sports**: Articles about games, athletes, competitions
- 💻 **Technology**: Articles about software, hardware, innovation
- 💼 **Business**: Articles about markets, companies, finance
- 🏥 **Health**: Articles about medicine, wellness, research
- 🌍 **Environment**: Articles about climate, nature, sustainability

## ⚠️ Important Notes

- **🔐 Security**: Never commit your `.env` file to version control
- **📊 Data Quality**: Ensure training data is well-balanced across categories
- **🎯 Model Performance**: Test with diverse articles to validate accuracy
- **💰 Cost Management**: Monitor Azure usage to avoid unexpected charges
- **🔄 Model Updates**: Retrain periodically with new data for better accuracy

## 🚨 Troubleshooting

### Common Issues:

1. **Authentication Error**: Verify your AI service key and endpoint
2. **Project Not Found**: Ensure project name matches Language Studio
3. **Deployment Error**: Check if model is deployed and deployment name is correct
4. **File Not Found**: Verify `articles` folder exists with text files

## 🤝 Contributing

Feel free to enhance this project by:
- Adding more sophisticated error handling
- Implementing batch processing for large datasets
- Adding support for multi-label classification
- Creating a web interface for easier interaction

## 📚 Additional Resources

- [Azure AI Language Documentation](https://docs.microsoft.com/azure/cognitive-services/language-service/)
- [Custom Text Classification Guide](https://docs.microsoft.com/azure/cognitive-services/language-service/custom-text-classification/)
- [Azure Storage Blob Documentation](https://docs.microsoft.com/azure/storage/blobs/)

---

**Happy Classifying! 🎉**
