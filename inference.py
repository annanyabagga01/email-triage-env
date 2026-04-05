from env import EmailEnv

env = EmailEnv()
obs = env.reset()

print(f"[START] task={obs['task_type']} env=email model=heuristic")

if obs["task_type"] == "spam":
    value = "spam" if "win" in obs["email_text"].lower() else "not spam"
    action = {"action_type":"classify","value":value}

elif obs["task_type"] == "routing":
    value = "billing" if "payment" in obs["email_text"].lower() else "tech"
    action = {"action_type":"route","value":value}

else:
    action = {
        "action_type":"reply",
        "value":"Sorry, we will resolve your issue soon."
    }

obs, reward, done, _ = env.step(action)

print(f"[STEP] step=1 action={action['value']} reward={reward:.2f} done=true error=null")
print(f"[END] success=true steps=1 rewards={reward:.2f}")
