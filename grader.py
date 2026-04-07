def grade(obs, action):
    task = obs.get("task_type")

    # 🔥 SPAM TASK
    if task == "spam":
        if action.get("action_type") != "classify":
            return 0.2

        if action.get("value","").lower() == obs.get("label","").lower():
            return 0.9 
        else:
            return 0.3

    # 🔥 ROUTING TASK
    if task == "routing":
        if action.get("action_type") != "route":
            return 0.2

        if action.get("value","").lower() == obs.get("department","").lower():
            return 0.85
        else:
            return 0.4

    # 🔥 REPLY TASK
    if task == "reply":
        if action.get("action_type") != "reply":
            return 0.2

        text = action.get("value","").lower()
        score = 0.3

        for word in obs.get("ideal_keywords", []):
            if word in text:
                score += 0.2

        if "sorry" in text:
            score += 0.1

        if "resolve" in text:
            score += 0.1

        return min(score, 0.95)

    return 0.5
