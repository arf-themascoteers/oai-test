import torch
import random
import gym

env = gym.make("CartPole-v0")
states = env.observation_space.shape[0]
actions = env.action_space.n

episodes = 10

for episode in range(1, episodes+1):
    states = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = random.choice([0,1])
        n_state, reward, done, info = env.step(action)
        print(n_state)
        score += reward

    print(f'Episodes{episode} Score{score}')