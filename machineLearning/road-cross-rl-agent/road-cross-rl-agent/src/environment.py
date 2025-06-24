class Environment:
    def __init__(self):
        self.state = self.reset()
        self.action_space = ['left', 'right', 'stay']
        self.done = False

    def reset(self):
        self.state = 0  # Reset to initial state
        self.done = False
        return self.state

    def step(self, action):
        if action == 'left':
            self.state -= 1
        elif action == 'right':
            self.state += 1
        # Implement logic for crossing the road and updating done status
        # For example, if state reaches a certain value, set done to True
        return self.state, self.get_reward(), self.done

    def get_reward(self):
        # Define reward structure based on the state
        return 1 if self.state == target_state else -1

    def render(self):
        # Implement rendering logic to visualize the environment
        print(f"Current State: {self.state}")