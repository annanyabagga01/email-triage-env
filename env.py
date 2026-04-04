from tasks import get_random_email
from grader import grade

class EmailEnv:
    def __init__(self):
        self.current = None

    def reset(self):
        self.current = get_random_email()
        return self.current

    def step(self, action):
        if self.current is None:
            raise Exception("Call /reset first")

        reward = grade(self.current, action)
        done = True

        return self.current, reward, done, {}

    def state(self):
        return self.current