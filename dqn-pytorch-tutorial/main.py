import gymnasium as gym
from DQN import Agent
from utils import plot_learning_curve
import numpy as np

if __name__ == '__main__':
    env = gym.make('LunarLander-v2')
    agent = Agent(gamma=0.99, epsilon=1.0, batch_size=64, n_actions=4, eps_end=0.01,
                  input_dims=[8], lr=0.0003)
    scores, eps_history = [], []
    n_games = 500

    #We wanna play each game.
    for i in range(n_games):
        score = 0
        terminated = False
        observation, observation_info = env.reset()
        #playing the game
        while not terminated:
            action = agent.choose_action(observation)#we choose an action based on the observation.
            observation_, reward, terminated, truncated, info = env.step(action)
            score += reward
            agent.store_transition(observation, action, reward, 
                                    observation_, terminated)
            agent.learn()
            observation = observation_#setting the current observation(state) to the next observation(next state)
        scores.append(score)
        eps_history.append(agent.epsilon)

        avg_score = np.mean(scores[-100:])#comparing it to the last 100 scores.(feels familiar right?)

        print('episode ', i, 'score %.2f' % score,
                'average score %.2f' % avg_score,
                'epsilon %.2f' % agent.epsilon)
    x = [i+1 for i in range(n_games)]
    filename = 'lunar_lander.png'
    plot_learning_curve(x, scores, eps_history, filename)