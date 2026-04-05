from fastapi import FastAPI
from env import EmailEnv

app = FastAPI()
env = EmailEnv()

@app.get("/")
def home():
    return {"message": "Email Triage Environment Running"}

# 🔥 MUST BE POST
@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    if "action_type" not in action or "value" not in action:
        return {"error": "Invalid action format"}

    if action["action_type"] not in ["classify", "route", "reply"]:
        return {"error": "Invalid action type"}

    obs, reward, done, info = env.step(action)

    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()
