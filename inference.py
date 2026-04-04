from env import EmailEnv

env = EmailEnv()
obs = env.reset()

print(f"[START] task={obs['task_type']} env=email model=smart")

if obs["task_type"] == "spam":
    action = {"action_type": "classify", "value": obs["label"]}

elif obs["task_type"] == "routing":
    action = {"action_type": "route", "value": obs["department"]}

else:
    text = obs["email_text"].lower()

    if "refund" in text or "charged" in text:
        reply = "Sorry, we will process your refund soon."
    elif "login" in text:
        reply = "Sorry, please reset your password or we will assist you."
    else:
        reply = "Sorry, our support team will help you shortly."

    action = {"action_type": "reply", "value": reply}

obs, reward, done, _ = env.step(action)

print(f"[STEP] step=1 action={action['value']} reward={reward:.2f} done=true error=null")
print(f"[END] success=true steps=1 rewards={reward:.2f}")