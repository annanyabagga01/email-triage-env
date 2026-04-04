from fastapi import FastAPI
from env import EmailEnv

app = FastAPI()
env = EmailEnv()

@app.get("/")
def home():
    return {"message": "Email Triage Environment Running"}

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    try:
        if "action_type" not in action or "value" not in action:
            return {"error": "Invalid action format"}

        obs, reward, done, _ = env.step(action)

        return {
            "observation": obs,
            "reward": reward,
            "done": done
        }

    except Exception as e:
        return {"error": str(e)}

@app.get("/state")
def state():
    return env.state()