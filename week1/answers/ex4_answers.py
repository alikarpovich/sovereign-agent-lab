"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = [
    'search_venues', 'get_venue_details'
]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "None of the known Edinburgh venues can accommodate 300 people with vegan options. The closest options have either insufficient capacity or lack vegan availability. Would you like me to:\n1. Suggest alternative venues outside our known list?\n2. Adjust the capacity requirements?\n3. Check for vegan options at other event spaces in Edinburgh?"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
The agent found only one venue that meets the criteria, so it returned the details of that venue.
In the first case, there was another step for the agent to select the best option from the approved venues.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 300   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 290   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP allows the agent to dynamically explore the tools available and select the best one for the task.
Once best tools identified, the agent initiated with those tools and didn't need to change the code.
In case the service behind MCP develops and has new tools, the agent will be able to detect them and use them as well.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- The Planner (autonomous-loop part) is a strong-reasoning model, 
it stays before LangGraph ReAct loop and break unclear tasks into ordered subgoals before tools are used.
- The Executor from research_agent.py is fast worker inside the loop, 
it calls tools and iterates on results until research is finished.
- The shared MCP tool server (mcp_venue_server.py and next versions) is between this two parts, 
so they don’t care where tools are implemented — both discover and use same capabilities.
- The structured Rasa Pro CALM agent from exercise3_rasa/ (structured part) run predefined flows 
and Python action guards for pub-manager calls, so deposits and guest numbers stay clear and trackable.
- The handoff bridge between both parts send phone-call tasks to structured agent, 
and open-ended research tasks goes back to the loop when new info is needed.
- The persistent and vector memory layers (in both parts) stores session context and use RAG, 
so PyNanoClaw don’t repeat same research or ask what it already have.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The LangGraph research agent is the right place for open-ended questions: 
the run for 300 vegan guests returned a careful “no known venue fits” answer instead of inventing a pub, 
which is exactly the kind of exploratory tool-backed reasoning you want before any commitment. 
Exercise 3’s Rasa CALM agent is the right place for the manager’s call because `flows.yml` and `actions.py` enforce 
concrete business rules—like deposit limits. 
Swapping them feels wrong because the loop would be improvising on prices and promises on a live call as it's not bounded by the rules, 
while a research bot would struggle with underspecified research tasks and could not pivot across tools 
the way the ReAct trace did when constraints were impossible.
"""