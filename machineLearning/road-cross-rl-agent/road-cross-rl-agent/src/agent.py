class Agent:
    def __init__(self, action_space, state_space, learning_rate=0.01, discount_factor=0.99):
        self.action_space = action_space
        self.state_space = state_space
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_table = {}  # Initialize Q-table

    def choose_action(self, state, exploration_rate):
        # Implement epsilon-greedy action selection
        if np.random.rand() < exploration_rate:
            return np.random.choice(self.action_space)  # Explore
        else:
            return np.argmax(self.q_table.get(state, np.zeros(len(self.action_space))))  # Exploit

    def learn(self, state, action, reward, next_state):
        # Update Q-value using the Q-learning formula
        current_q = self.q_table.get(state, np.zeros(len(self.action_space)))[action]
        max_future_q = np.max(self.q_table.get(next_state, np.zeros(len(self.action_space))))
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)
        
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.action_space))
        self.q_table[state][action] = new_q

    def store_experience(self, state, action, reward, next_state):
        # This method can be used to store experiences for replay (if implementing experience replay)
        pass  # Placeholder for experience storage logic