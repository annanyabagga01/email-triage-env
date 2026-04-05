from tasks import get_random_email
from grader import grade

class EmailEnv:
    def __init__(self):
        self.current = None
        self.steps = 0
        self.max_steps = 3

    def reset(self):
        self.current = get_random_email()
        self.steps = 0
        return self.current

    def step(self, action):
        if self.current is None:
            raise Exception("Call reset first")

        self.steps += 1

        reward = grade(self.current, action)
        done = self.steps >= self.max_steps

        return self.current, reward, done, {}

    def state(self):
        return self.current
