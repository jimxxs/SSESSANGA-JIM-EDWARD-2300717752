import numpy as np
from agent import Agent
from environment import Environment

def train_agent(episodes, max_steps):
    env = Environment()
    agent = Agent()

    for episode in range(episodes):
        state = env.reset()
        total_reward = 0

        for step in range(max_steps):
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.store_experience(state, action, reward, next_state, done)
            agent.learn()
            state = next_state
            total_reward += reward

            if done:
                break

        print(f"Episode {episode + 1}/{episodes}, Total Reward: {total_reward}")

if __name__ == "__main__":
    train_agent(episodes=1000, max_steps=100)