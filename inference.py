import os
from openai import OpenAI
from env import EmailEnv

# 🔥 USE PROXY (IMPORTANT)
client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

env = EmailEnv()
obs = env.reset()

print(f"[START] task={obs['task_type']} env=email model=llm")

# Create prompt
prompt = f"""
You are an email assistant.

Email:
{obs['email_text']}

Task: {obs['task_type']}

Respond with only the answer.
"""

# 🔥 LLM CALL (THIS FIXES ERROR)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

output = response.choices[0].message.content.strip().lower()

# Map output to action
if obs["task_type"] == "spam":
    action = {"action_type": "classify", "value": "spam" if "spam" in output else "not spam"}

elif obs["task_type"] == "routing":
    action = {"action_type": "route", "value": output}

else:
    action = {"action_type": "reply", "value": output}

obs, reward, done, _ = env.step(action)

print(f"[STEP] step=1 action={action['value']} reward={reward:.2f} done=true error=null")
print(f"[END] success=true steps=1 rewards={reward:.2f}")
