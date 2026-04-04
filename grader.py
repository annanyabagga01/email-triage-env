def grade(obs, action):
    task = obs.get("task_type")

    if task == "spam":
        if action.get("action_type") != "classify":
            return -1.0
        return 1.0 if action.get("value","").lower() == obs.get("label","").lower() else -1.0

    if task == "routing":
        if action.get("action_type") != "route":
            return -0.5
        return 1.0 if action.get("value","").lower() == obs.get("department","").lower() else -0.5

    if task == "reply":
        if action.get("action_type") != "reply":
            return -1.0

        text = action.get("value","").lower()
        score = 0.0

        for word in obs.get("ideal_keywords", []):
            if word in text:
                score += 0.3

        if "sorry" in text:
            score += 0.2

        if "will" in text or "resolve" in text:
            score += 0.2

        return min(score, 1.0)

    return 0.0