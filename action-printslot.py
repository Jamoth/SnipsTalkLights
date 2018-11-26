#!/usr/bin/env python2
from hermes_python.hermes import Hermes
​
def intent_received(hermes, intent_message):
    result_sentence= "Da geht was lokal!"
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, result_sentence)
​
with Hermes('raspberrypi.local:1883') as h:
    h.subscribe_intents(intent_received).start()
