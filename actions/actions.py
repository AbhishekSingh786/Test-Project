# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []
# Automation Code which is not Working
# # from typing import Any, Text, Dict, List
# # from pymongo.database import Database
# # from pymongo import MongoClient
# # from rasa_sdk import Action, Tracker 
# # from rasa_sdk.executor import CollectingDispatcher
# # import pymongo
# # class Pname(Action):
# #     def name(self):
# #         return "product_name"
# #     def run(self, dispatcher, tracker, domain):
# #         client = pymongo.MongoClient("localhost", 27017)
# #         db=client.Data
# #         res = db.product_table.find({'Name':'1'})
# #         print(type(res))
# #         for i in res:
# #             dispatcher.utter_button_message(i['text'],i['buttons'])
# #         return []