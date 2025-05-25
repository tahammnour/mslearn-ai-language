from dotenv import load_dotenv
import os

# Import Azure SDK
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

def main():
    try:
        # Load environment variables
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        ai_project_name = os.getenv('QA_PROJECT_NAME')
        ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

        # Validate environment variables
        if not all([ai_endpoint, ai_key, ai_project_name, ai_deployment_name]):
            raise ValueError("Missing one or more environment variables. Check your .env file.")

        # Create Azure client
        credential = AzureKeyCredential(ai_key)
        ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)

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

    except Exception as ex:
        print(f"⚠️ Exception occurred: {ex}")

if __name__ == "__main__":
    main()
