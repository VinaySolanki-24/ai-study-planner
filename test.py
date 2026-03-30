from env import StudyEnv

env = StudyEnv()
state = env.reset()

action = {
    "plan" : {
        "physics" : 2,
        "biology" : 2
    }
}

state, reward, done = env.step(action)

print("state : ", state)
print("reward :", reward)
print("done :", done)