# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_start"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         user_message = tracker.latest_message.get('text')
#         intent = tracker.latest_message['intent'].get('name')

#         if intent == 'leave_policy':
#             dispatcher.utter_message("Our leave policy is that employees get 15 days of paid time off per year, which increases to 20 days after 5 years of service.")
#         elif intent == 'goodbye':
#             dispatcher.utter_message("We follow a structured salary system based on employee roles and experience. You can check with your HR representative for more details.")
#         else:
#             dispatcher.utter_message("I cant understand")
#         return []
