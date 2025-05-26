# 🔍 Azure AI Custom Entity Recognition Project

## 🚀 Project Overview

This project demonstrates how to use **Azure AI Language Services** for custom entity recognition. The application reads advertisement text files and extracts custom entities like products, prices, locations, and other relevant information using a pre-trained custom model deployed in Azure AI Language Studio.

## 🧠 What Does This Code Do?

The `custom-entities.py` script performs the following operations:

1. **🔧 Configuration Loading**: Loads environment variables from `.env` file
2. **🔗 Azure Connection**: Establishes connection to Azure AI Language Service
3. **📁 File Processing**: Reads all text files from the `ads` folder
4. **🤖 Entity Extraction**: Uses custom trained model to extract entities from each document
5. **📊 Results Display**: Shows extracted entities with their categories and confidence scores

## 🏗️ Azure Infrastructure Setup

### 📋 Prerequisites

Before running this project, you need to set up the following Azure resources:

#### 1. 🗄️ Azure Storage Account
- Create a Storage Account in Azure Portal
- **❗ Important**: Set blob access to **anonymous read** for public access
- Upload your training data (advertisements) to blob containers
- Organize data into folders like:
  - 📂 `train/` - Training advertisements with labeled entities
  - 📂 `test/` - Test advertisements for validation

#### 2. 🧠 Azure AI Language Service
- Create an Azure AI Language resource
- **❗ Important**: Assign **Cognitive Services Contributor** role to your account
- Note down the endpoint and key

#### 3. 🎯 Custom Entity Recognition Project
- Go to Azure AI Language Studio
- Create a new **Custom Named Entity Recognition** project
- Connect your Storage Account as data source
- Label entities in your training data (e.g., Product, Price, Location, ContactInfo)
- Train your custom model
- Deploy the model (note the deployment name)

## 🛠️ Project Setup

### Step 1: Navigate to Project Directory 📁
```bash
cd /workspaces/mslearn-ai-language/Labfiles/05-custom-entity-recognition/Python/custom-entities
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
azure-ai-textanalytics==5.3.0
```

## ⚙️ Environment Configuration

Create or update the `.env` file in the project directory:

```properties
AI_SERVICE_ENDPOINT=https://your-ai-service.cognitiveservices.azure.com/
AI_SERVICE_KEY=your_ai_service_key_here
PROJECT=CustomEntityLab
DEPLOYMENT=AdEntities
```

## 📁 Project Structure

```
custom-entities/
├── ads/
│   ├── test1.txt
│   ├── test2.txt
│   └── ... (more advertisement files)
├── custom-entities.py
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

2. **Run the entity extraction script:**
   ```bash
   python custom-entities.py
   ```

## 📋 Expected Output

```
test1.txt
	Entity 'Bluetooth earbuds' has category 'Product' with confidence score of '0.95'
	Entity '$100' has category 'Price' with confidence score of '0.92'
	Entity 'Sacramento, CA' has category 'Location' with confidence score of '0.88'

test2.txt
	Entity 'iPhone 12' has category 'Product' with confidence score of '0.97'
	Entity '$500' has category 'Price' with confidence score of '0.94'
	Entity 'contact@email.com' has category 'ContactInfo' with confidence score of '0.89'
```

## 🏷️ Custom Entity Categories

Design your entity recognition system with categories such as:

- 📱 **Product**: Items being sold (e.g., "iPhone 12", "Bluetooth earbuds")
- 💰 **Price**: Monetary values (e.g., "$100", "fifty dollars")
- 📍 **Location**: Geographic locations (e.g., "Sacramento, CA", "downtown")
- 📞 **ContactInfo**: Contact details (e.g., "555-1234", "john@email.com")
- 🏢 **Brand**: Product brands (e.g., "Apple", "Samsung")
- 🎨 **Condition**: Item condition (e.g., "new", "used", "refurbished")
- 📅 **DateTime**: Time-related information (e.g., "Monday", "next week")

## 🏗️ Training Data Organization

### 📊 Data Structure in Azure Storage

```
your-storage-container/
├── train/
│   ├── ad_001.txt
│   ├── ad_002.txt
│   ├── ad_003.txt
│   └── ...
├── test/
│   ├── test_ad_001.txt
│   ├── test_ad_002.txt
│   └── ...
└── labels/
    ├── labels.json
    └── ...
```

### 📝 Sample Training Data

**Example Advertisement Text:**
```
For sale: MacBook Pro 2021, excellent condition. 
Price: $1200 OBO. 
Located in Seattle, WA. 
Contact me at seller@email.com or 206-555-0123.
Available this weekend.
```

**Labeled Entities:**
- MacBook Pro 2021 → Product
- excellent condition → Condition  
- $1200 → Price
- Seattle, WA → Location
- seller@email.com → ContactInfo
- 206-555-0123 → ContactInfo
- this weekend → DateTime

## ⚠️ Important Notes

- **🔐 Security**: Never commit your `.env` file to version control
- **📊 Data Quality**: Ensure training data covers diverse entity examples
- **🎯 Model Performance**: Test with various advertisement formats
- **💰 Cost Management**: Monitor Azure usage to avoid unexpected charges
- **🔄 Model Updates**: Retrain periodically with new labeled data
- **📏 Text Limits**: Be aware of text length limits in the API

## 🚨 Troubleshooting

### Common Issues:

1. **Authentication Error**: Verify your AI service key and endpoint
2. **Project Not Found**: Ensure project name matches Language Studio
3. **Deployment Error**: Check if model is deployed and deployment name is correct
4. **No Ads Folder**: Verify `ads` folder exists with text files
5. **Virtual Environment**: Make sure virtual environment is activated
6. **Permission Error**: Check Azure role assignments

### Debug Steps:

```bash
# Check if virtual environment is active
which python

# Verify dependencies are installed
pip list

# Test Azure connection
python -c "from azure.ai.textanalytics import TextAnalyticsClient; print('Azure SDK imported successfully')"
```

## 🎯 Use Cases

This custom entity recognition system is perfect for:

- 🛒 **E-commerce**: Extract product details from listings
- 📰 **Content Analysis**: Identify key information in articles
- 📧 **Email Processing**: Extract contact information and locations
- 📱 **Social Media**: Analyze posts for products and prices
- 🏢 **Business Intelligence**: Extract insights from customer feedback

## 🤝 Contributing

Enhance this project by:
- Adding more entity categories
- Implementing confidence threshold filtering
- Creating batch processing capabilities
- Adding export functionality for results
- Building a web interface for easier interaction

## 📚 Additional Resources

- [Azure AI Language Documentation](https://docs.microsoft.com/azure/cognitive-services/language-service/)
- [Custom Named Entity Recognition Guide](https://docs.microsoft.com/azure/cognitive-services/language-service/custom-named-entity-recognition/)
- [Entity Labeling Best Practices](https://docs.microsoft.com/azure/cognitive-services/language-service/custom-named-entity-recognition/concepts/guidelines)
- [Azure Storage Documentation](https://docs.microsoft.com/azure/storage/)

## 🎉 Next Steps

1. **Expand Entity Types**: Add more specific categories for your domain
2. **Improve Accuracy**: Collect more training data and refine labels
3. **Integration**: Connect to databases or APIs for automated processing
4. **Monitoring**: Set up logging and performance tracking
5. **Production**: Deploy as a web service or API

---

**Happy Entity Extracting! 🎉🔍**
