from dotenv import load_dotenv
import os
import json
from datetime import datetime, timedelta, date, timezone
from dateutil.parser import parse as is_date

# Import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

def main():

    try:
        # Get Configuration Settings
        load_dotenv()
        ls_prediction_endpoint = os.getenv('LS_CONVERSATIONS_ENDPOINT')
        ls_prediction_key = os.getenv('LS_CONVERSATIONS_KEY')

        # Get user input (until they enter "quit")
        print("🕐 Welcome to the Azure AI Clock Assistant! 🌍")
        print("Ask me about time, dates, or days. Type 'quit' to exit.")
        print("Examples: 'What time is it?', 'What time in Tokyo?', 'What day is Friday?'")
        
        userText = ''
        while userText.lower() != 'quit':
            userText = input('\n💬 Enter your question ("quit" to stop): ')
            if userText.lower() == 'quit':
                print("👋 Goodbye! Thanks for using the Clock Assistant!")
                break

            # Create a client for the Language service model
            client = ConversationAnalysisClient(
                ls_prediction_endpoint, AzureKeyCredential(ls_prediction_key))
            # Call the Language service model to get intent and entities
            cls_project = 'Clock'
            deployment_slot = 'production'

            with client:
                query = userText
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
                            "projectName": cls_project,
                            "deploymentName": deployment_slot,
                            "verbose": True
                        }
                    }
                )

            top_intent = result["result"]["prediction"]["topIntent"]
            entities = result["result"]["prediction"]["entities"]

            print("\n🎯 Analysis Results:")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"🧠 Top Intent: {top_intent}")
            print(f"📂 Category: {result['result']['prediction']['intents'][0]['category']}")
            print(f"💯 Confidence: {result['result']['prediction']['intents'][0]['confidenceScore']:.2f}\n")

            if entities:
                print("🏷️  Entities Found:")
                for entity in entities:
                    print(f"   📋 Category: {entity['category']}")
                    print(f"   📝 Text: {entity['text']}")
                    print(f"   💯 Confidence: {entity['confidenceScore']:.2f}")
                print()
            else:
                print("🔍 No entities found\n")

            print(f"❓ Your Question: '{result['result']['query']}'")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

            # Apply the appropriate action
            if top_intent == 'GetTime':
                location = 'local'
                # Check for a location entity
                for entity in entities:
                    if entity["category"] == 'Location':
                        location = entity["text"]
                time_result = GetTime(location)
                print(f"\n🕐 {time_result}")

            elif top_intent == 'GetDay':
                date_string = date.today().strftime("%m/%d/%Y")
                for entity in entities:
                    if entity["category"] == 'Date':
                        date_string = entity["text"]
                day_result = GetDay(date_string)
                print(f"\n📅 {day_result}")

            elif top_intent == 'GetDate':
                day = 'today'
                for entity in entities:
                    if entity["category"] == 'Weekday':
                        day = entity["text"]
                date_result = GetDate(day)
                print(f"\n🗓️  {date_result}")

            else:
                print('\n❌ Sorry, I didn\'t understand that.')
                print('💡 Try asking me for:')
                print('   🕒 Time: "What time is it?" or "What time in London?"')
                print('   📅 Day: "What day is 12/25/2024?"')
                print('   🗓️  Date: "What\'s the date next Monday?"')

    except Exception as ex:
        print(f"⚠️ Error occurred: {ex}")
        print("🔧 Please check your Azure configuration and try again.")



def GetTime(location):
    time_string = ''
    location_emoji = ''

    if location.lower() == 'local':
        now = datetime.now()
        time_string = f'The local time is {now.hour:02d}:{now.minute:02d}'
        location_emoji = '🏠'
    elif location.lower() == 'london':
        utc = datetime.now(timezone.utc)
        time_string = f'The time in London is {utc.hour:02d}:{utc.minute:02d}'
        location_emoji = '🇬🇧'
    elif location.lower() == 'sydney':
        time = datetime.now(timezone.utc) + timedelta(hours=11)
        time_string = f'The time in Sydney is {time.hour:02d}:{time.minute:02d}'
        location_emoji = '🇦🇺'
    elif location.lower() == 'new york':
        time = datetime.now(timezone.utc) + timedelta(hours=-5)
        time_string = f'The time in New York is {time.hour:02d}:{time.minute:02d}'
        location_emoji = '🇺🇸'
    elif location.lower() == 'nairobi':
        time = datetime.now(timezone.utc) + timedelta(hours=3)
        time_string = f'The time in Nairobi is {time.hour:02d}:{time.minute:02d}'
        location_emoji = '🇰🇪'
    elif location.lower() == 'tokyo':
        time = datetime.now(timezone.utc) + timedelta(hours=9)
        time_string = f'The time in Tokyo is {time.hour:02d}:{time.minute:02d}'
        location_emoji = '🇯🇵'
    elif location.lower() == 'delhi':
        time = datetime.now(timezone.utc) + timedelta(hours=5.5)
        time_string = f'The time in Delhi is {time.hour:02d}:{time.minute:02d}'
        location_emoji = '🇮🇳'
    else:
        time_string = f"❌ Sorry, I don't know the timezone for {location}"
        location_emoji = '❓'

    return f"{location_emoji} {time_string}"


def GetDate(day):
    date_string = '❌ I can only determine dates for today or named days of the week.'

    weekdays = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
    }

    today = date.today()
    day = day.lower()
    if day == 'today':
        date_string = f"📅 Today's date is {today.strftime('%m/%d/%Y')}"
    elif day in weekdays:
        todayNum = today.weekday()
        weekDayNum = weekdays[day]
        offset = weekDayNum - todayNum
        target_date = today + timedelta(days=offset)
        if offset == 0:
            date_string = f"📅 {day.capitalize()} (today) is {target_date.strftime('%m/%d/%Y')}"
        elif offset > 0:
            date_string = f"📅 Next {day.capitalize()} is {target_date.strftime('%m/%d/%Y')}"
        else:
            date_string = f"📅 Last {day.capitalize()} was {target_date.strftime('%m/%d/%Y')}"

    return date_string


def GetDay(date_string):
    try:
        date_object = datetime.strptime(date_string, "%m/%d/%Y")
        day_string = f"📅 {date_string} falls on a {date_object.strftime('%A')}"
    except:
        day_string = '❌ Please enter a date in MM/DD/YYYY format (e.g., 12/25/2024)'
    return day_string


if __name__ == "__main__":
    main()
