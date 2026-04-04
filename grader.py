def grade(obs, action):
    task = obs.get("task_type")

    # SPAM
    if task == "spam":
        if action.get("action_type") != "classify":
            return -1.0
        pred = action.get("value","").lower()
        gt = obs.get("label","").lower()
        return 1.0 if pred == gt else -1.0

    # ROUTING
    if task == "routing":
        if action.get("action_type") != "route":
            return -0.5
        pred = action.get("value","").lower()
        gt = obs.get("department","").lower()
        return 1.0 if pred == gt else -0.5

    # REPLY (graded)
    if task == "reply":
        if action.get("action_type") != "reply":
            return -1.0

        text = action.get("value","").lower()
        score = 0.0

        # keywords (0.6 max)
        for w in obs.get("ideal_keywords", []):
            if w in text:
                score += 0.3

        # tone (0.2)
        if "sorry" in text or "apologize" in text:
            score += 0.2

        # actionability (0.2)
        if any(k in text for k in ["will", "process", "resolve", "assist"]):
            score += 0.2

        return min(score, 1.0)

    return 0.0