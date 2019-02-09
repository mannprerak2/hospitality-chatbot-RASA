## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_name
* name{"name":"Sam"}
 - utter_greet

## story_01
* greet
 - utter_greet
* event-request
 - utter_event
* event_location
 - utter_location
* event_time
 - utter_time
* goodbye
 - utter_goodbye

 ## story_02
* greet
 - utter_greet
* event_location
 - utter_location
* event_time
 - utter_time
* goodbye
 - utter_goodbye

 ## story_03
* greet
 - utter_greet
* event-request
 - utter_event
* event_location
 - utter_location
* event_time
 - utter_time

 ## story_01
* event-request
 - utter_event

## story_01
* event_time
 - utter_time

 ## story_01
* event_location
 - utter_location

