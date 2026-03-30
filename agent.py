import random

class StudyAgent :
    def get_action(self , state) : 
        subjects = state['subjects']
        total_hours = state['hours_available']

        plan = {}
        equal_time = total_hours//len(subjects)

        for sub in subjects:
            plan[sub] = equal_time
        
        return{'plan' : plan }
    
