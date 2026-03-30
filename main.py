from env import StudyEnv
from agent import StudyAgent

# create object
env = StudyEnv()
agent = StudyAgent()

# start enviroment
state = env.reset()

total_reward = 0

print("😀✨---STARTING AI STUDY PLANNER---✨😀\n")

for step in range(5):
    print(f"step{step+1}")

    # agent decides action
    action = agent.get_action(state)
    print("Action:",action)

    # env response
    state , reward , done = env.step(action)
    print('state : ',state)
    print('reward : ',reward)
    print('done : ',done)
    print('-' * 30)

    total_reward += reward

    if done:
        print('✅ ALL TASK COMPLETED')
        break

print('\n🎯 TOTAL REWARD : ' , total_reward)

