from tasks import get_random_email
from grader import grade

class EmailEnv:
    def __init__(self):
        self.current = None
        self.step_count = 0
        self.max_steps = 3  # multi-step episode

    def reset(self, seed: int = None):
        if seed is not None:
            import random
            random.seed(seed)
        self.current = get_random_email()
        self.step_count = 0
        return self._obs()

    def _obs(self):
        return {
            "email_text": self.current["email_text"],
            "sender": self.current["sender"],
            "subject": self.current["subject"],
            "task_type": self.current["task_type"],
            # action mask → valid actions for this task
            "valid_actions": self._valid_actions()
        }

    def _valid_actions(self):
        t = self.current["task_type"]
        if t == "spam":
            return ["classify"]
        if t == "routing":
            return ["route"]
        if t == "reply":
            return ["reply"]
        return []

    def step(self, action):
        if self.current is None:
            raise Exception("Call /reset first")

        self.step_count += 1

        # invalid action penalty
        if action.get("action_type") not in self._valid_actions():
            reward = -1.0
            done = self.step_count >= self.max_steps
            return self._obs(), reward, done, {"error": "invalid_action"}

        reward = grade(self.current, action)

        done = self.step_count >= self.max_steps
        return self._obs(), reward, done, {}
    
    def state(self):
        return self._obs()