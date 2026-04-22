
import json
from typing import Dict

# ---- Mock LLM (replace with GPT-4o-mini in real use) ----
def llm_intent_classifier(text: str) -> str:
    text = text.lower()
    if any(x in text for x in ["hi", "hello"]):
        return "greeting"
    if any(x in text for x in ["price", "plan", "cost"]):
        return "pricing"
    if any(x in text for x in ["buy", "subscribe", "try", "signup"]):
        return "high_intent"
    return "other"

# ---- Load KB ----
with open("knowledge_base.json") as f:
    KB = json.load(f)

# ---- RAG ----
def retrieve_info(query: str) -> str:
    return f"""
Basic Plan: {KB['basic']}
Pro Plan: {KB['pro']}
Policies: {KB['policies']}
"""

# ---- Tool ----
def mock_lead_capture(name, email, platform):
    print(f"✅ Lead captured: {name}, {email}, {platform}")

# ---- State Machine ----
class AgentState:
    def __init__(self):
        self.stage = "start"
        self.user_data: Dict[str, str] = {}

def run_agent():
    state = AgentState()
    print("Agent: Hello! Ask me about AutoStream 🚀")

    while True:
        user_input = input("User: ")
        intent = llm_intent_classifier(user_input)

        if intent == "greeting":
            print("Agent: Hi there! How can I help you?")

        elif intent == "pricing":
            print("Agent:", retrieve_info(user_input))

        elif intent == "high_intent":
            print("Agent: Awesome! Let's get you started.")
            state.stage = "collect_name"

        # ---- Data Collection Flow ----
        if state.stage == "collect_name":
            state.user_data["name"] = input("Agent: What's your name? ")
            state.stage = "collect_email"

        if state.stage == "collect_email":
            state.user_data["email"] = input("Agent: Your email? ")
            state.stage = "collect_platform"

        if state.stage == "collect_platform":
            state.user_data["platform"] = input("Agent: Which platform (YouTube/Instagram)? ")
            state.stage = "done"

        if state.stage == "done":
            mock_lead_capture(
                state.user_data["name"],
                state.user_data["email"],
                state.user_data["platform"]
            )
            print("Agent: You're all set! 🎉")
            state.stage = "start"

if __name__ == "__main__":
    run_agent()
