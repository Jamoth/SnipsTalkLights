#!/usr/bin/env python2
from hermes_python.hermes import Hermes
​
def intent_received(hermes, intent_message):
    print('Intent {}'.format(intent_message.intent))
​
    for (slot_value, slot) in intent_message.slots.items():
        print('Slot {} -> \n\tRaw: {} \tValue: {}'.format(slot_value, slot[0].raw_value, slot[0].slot_value.value.value))
        
        result_sentence= "Licht ist aus!"
        current_session_id = intentMessage.session_id
        hermes.publish_end_session(current_session_id, result_sentence)
​
    hermes.publish_end_session(intent_message.session_id, None)
​
with Hermes('raspberrypi.local:1883') as h:
    h.subscribe_intents(intent_received).start()