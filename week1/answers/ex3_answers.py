"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  hello                                                                                                                                                                   

I'm sorry, I'm not trained to help with that.
Your input ->                                                                                                                                                                          
2026-04-13 23:31:46 INFO     rasa.dialogue_understanding.generator.command_generator  - [info     ] Invalid message                errors=[{'error_type': 'rasa_internal_error_user_input_empty', 'info': {}, 'command': 'error'}] event_key=command_generator.evaluate_message.error
I see an empty message. What can I assist you with?
Your input ->  calling to confirm a booking                                                                                                                                            
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                                                                                                              
50 veAnd how many of those guests will need vegan meals?
Your input ->  50 vegan                                                                                                                                                                
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  200 GBP deposit                                                                                                                                                         
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking                                                                                                                                            

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

;
^[How many guests are you confirming for tonight's event?
Your input ->  ;                                                                                                                                                                       

How many guests are you confirming for tonight's event?
Your input ->                                                                                                                                                                          
2026-04-13 23:35:23 INFO     rasa.dialogue_understanding.generator.command_generator  - [info     ] Invalid message                errors=[{'error_type': 'rasa_internal_error_user_input_empty', 'info': {}, 'command': 'error'}] event_key=command_generator.evaluate_message.error
I see an empty message. What can I assist you with?
How many guests are you confirming for tonight's event?
Your input ->  160                                                                                                                                                                     
And how many of those guests will need vegan meals?
Your input ->  40                                                                                                                                                                      
100000000What deposit amount in GBP are you proposing to secure the booking?
Your input ->  100000000                                                                                                                                                               
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £100000000 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "deposit exceeds the organiser's authorised limit"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  do you have parking by the way?                                                                                                                                         
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
It didn't escalate and returned a fallback message that it can only help with confirming tonight's venue booking.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
LangGraph agent processed user input, reasoned about it and suggested 3 options so that user could choose what to do next.
RASA CALM agent returned a fallback message that it can only help with confirming tonight's venue booking - no deviation from the flow.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
Ran chat in two terminals, one for the action server and one for the chat.
Went through the conversation steps and verified it told that it's late for the reservation.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
Every time the user provides info that needs to fit some template, it's not a deterministic that checks it but llm.
That is not 100% predictable, but it's more flexible and can handle more cases, while the old approach was fully deterministic so more trusted. 
The old approach also costed less tokens as it didn't spawn llm call.

Python logic still verifies business requirements (that requests are within the limits) and that's still deterministic.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
FILL ME IN

Be specific. What can the Rasa CALM agent NOT do that LangGraph could?
Is that a feature or a limitation for the confirmation use case?
Think about: can the CALM agent improvise a response it wasn't trained on?
Can it call a tool that wasn't defined in flows.yml?

Rasa CALM agent can't improvise a response it wasn't trained on. That's a limitation form one hand as it can't handle unexpected situations, 
but on the other hand it's more predictable and less hallucinates. All the business rules are checked by python logic.

"""
