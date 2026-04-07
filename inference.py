import os
from openai import OpenAI
from env import EmailEnv

print("[INIT] Starting inference")

# safe client setup
client = None
try:
    if os.environ.get("API_BASE_URL") and os.environ.get("API_KEY"):
        client = OpenAI(
            base_url=os.environ["API_BASE_URL"],
            api_key=os.environ["API_KEY"]
        )
        print("[INIT] LLM client initialized")
    else:
        print("[WARN] Missing API env vars")
except Exception as e:
    print(f"[ERROR] Client init failed: {e}")

# init env
env = EmailEnv()
obs = env.reset()

print(f"[START] task={obs.get('task_type')}")

output = "spam"  # fallback

# 🔥 SAFE LLM CALL
try:
    if client:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Reply with 'spam'"}],
            timeout=5
        )
        output = response.choices[0].message.content.strip().lower()
        print("[LLM] Response received")
    else:
        print("[LLM] Skipped (no client)")

except Exception as e:
    print(f"[ERROR] LLM call failed: {e}")
    output = "spam"

# action
action = {"action_type": "classify", "value": output}

try:
    obs, reward, done, _ = env.step(action)
    print(f"[STEP] reward={reward}")
except Exception as e:
    print(f"[ERROR] Step failed: {e}")

print("[END] Inference completed")
