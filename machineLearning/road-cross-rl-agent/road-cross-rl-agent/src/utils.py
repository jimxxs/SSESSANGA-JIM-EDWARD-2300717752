def log_results(episode, total_reward, filename='results.log'):
    with open(filename, 'a') as f:
        f.write(f'Episode: {episode}, Total Reward: {total_reward}\n')

def save_model(agent, filename='model.pth'):
    import torch
    torch.save(agent.state_dict(), filename)

def load_model(agent, filename='model.pth'):
    import torch
    agent.load_state_dict(torch.load(filename))

def visualize_performance(rewards, filename='performance.png'):
    import matplotlib.pyplot as plt
    plt.plot(rewards)
    plt.title('Agent Performance Over Episodes')
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.savefig(filename)
    plt.close()