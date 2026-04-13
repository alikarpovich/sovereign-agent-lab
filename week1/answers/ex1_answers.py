"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

from itertools import filterfalse


PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
All the answers were correct, because the strong model (llama with 70 billion parameters) 
was processing the the clean dataset, so having results correct is expected.
Two out three answers were The Albanach, because it satisfies all the constraints and appears first - 
this suggests that the model might have a strong primacy bias. That could be a product of the "plain" presentation format.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The results were not changed - 3 correct answers with haymarket as an aswer for the plain format and albanach for more structured requests.
The Holyrood Arms was the most likely to cause a wrong answer, because it satisfies capacity and vegan,
only failing on status which is the third constraint - the very last. And also these options appear rather in the middle.
Model could've missed it due to attention blurring.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C showed that the small model with 8 nillion parameters was able to process the dataset correctly.
All three gave The Haymarket Vaults as an answer, not the Albanach for some of the request formats as stronger model did.
So even with smaller model and noise, I didn't see wrong answers although I could've expected some.
Having haymarket as an answer is consistent which could be the effect of formatting for a smaller model.
Number of tokens required was lower than for B, but not much. Potentially on larger requests it would make a difference.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the model is working with a smaller dataset and less parameters.
In this case, the smaller model was able to process the dataset correctly and get the best answer (with the lowest # of guests that fit requirements).
The number of tokens consumed could be more for a larger requests, for B and C the difference was not significant.
"""
