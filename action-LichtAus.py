#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes

def action_wrapper(hermes, intentMessage):
    """ Write the body of the function that will be executed once the intent is recognized.
    In your scope, you have the following objects :
    - intentMessage : an object that represents the recognized intent
    - hermes : an object with methods to communicate with the MQTT bus following the hermes protocol.
    - conf : a dictionary that holds the skills parameters you defined

    Refer to the documentation for further details.
    """
    
    if len(intentMessage.slots.objectLocation) > 0:
        myobjectLocation = ((intentMessage.slots.objectLocation.first().value))
        result_sentence = "Schalte das Licht {} aus".format(myobjectLocation)        
    else:
        result_sentence = 	"Schalte das Licht aus"
        
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("Jamoth:LampenAusSchalten", action_wrapper).start()
    

