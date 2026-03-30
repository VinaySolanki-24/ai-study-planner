class StudyEnv:
    def __init__(self):
        self.state = {}
        self.done = False

    def reset(self):
        # initial state (starting condition)
        self.state = {
            "hours_available" : 6,
            "subject" : ['Physics' , 'Biology'],
            "completed" : []
        }
        self.done = False
        return self.state

    def get_state(self):
        return self.state
    
    def step(self , action):
        reward = 0

        # total hours check
        total_hours = sum(action["plan"].values())
        
        if total_hours > self.state["hours_available"]:
            reward -= 2                                  # over planning panalty

        else:
            reward += 2                                  # valid planning reward

            # mark subject as complete

        for subject , hrs in action ["plan"].items():
            if hrs > 0:
                if subject not in self.state['completed']:
                    self.state["completed"].append(subject)
                else:
                    reward -= 1                           # duplicate penalty

            # check if all subject completed
        if set(self.state["completed"]) == set(self.state["subject"]):
            self.done = True
            reward += 3                                       # bonus reward

        return self.state , reward , self.done
