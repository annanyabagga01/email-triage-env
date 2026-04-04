from env import EmailEnv

env = EmailEnv()
obs = env.reset(seed=42)

total_reward = 0.0
steps = 0

print(f"[START] task={obs['task_type']} env=email model=heuristic")

while True:
    text = obs["email_text"].lower()
    t = obs["task_type"]

    if t == "spam":
        if any(k in text for k in ["win","free","offer","prize","lottery"]):
            value = "spam"
        else:
            value = "not spam"
        action = {"action_type":"classify","value":value}

    elif t == "routing":
        if any(k in text for k in ["payment","invoice","charged","refund"]):
            value = "billing"
        elif any(k in text for k in ["login","password","crash","bug","access"]):
            value = "tech"
        else:
            value = "hr"
        action = {"action_type":"route","value":value}

    else:
        if "refund" in text or "charged" in text:
            reply = "Sorry for the inconvenience. We will process your refund shortly."
        elif "login" in text or "password" in text:
            reply = "Sorry, please try resetting your password. We will assist if the issue continues."
        else:
            reply = "Sorry for the inconvenience. Our support team will assist you soon."
        action = {"action_type":"reply","value":reply}

    obs, reward, done, info = env.step(action)
    steps += 1
    total_reward += reward

    print(f"[STEP] step={steps} action={action['value']} reward={reward:.2f} done={str(done).lower()} error={info.get('error',None)}")

    if done:
        break

print(f"[END] success=true steps={steps} rewards={total_reward:.2f}")