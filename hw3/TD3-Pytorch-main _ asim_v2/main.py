from utils import evaluate_policy, Reward_adapter
from datetime import datetime
from TD3 import TD3_agent
import gymnasium as gym
import numpy as np
import os, shutil
import argparse
import torch

class Hyperparameters:
    def __init__(self):
        self.dvc = 'cuda'  # running device: cuda or cpu +
        self.Env_name = 'LunarLanderContinuous-v2'  # +
        self.render = False  # Render or Not 
        self.seed = 0  # random seed
        self.update_every = 50  # training frequency
        self.Max_train_steps = int(3e5)  # Max training steps
        self.save_interval = int(1e5)  # Model saving interval, in steps
        self.delay_freq = 1  # Delayed frequency for Actor and Target Net
        self.gamma = 0.99  # Discounted Factor The discount factor gamma is a number between 0 and 1. If gamma is close to 0, the agent will mostly consider only immediate rewards.
        self.net_width = 256  # Hidden net width, s_dim-400-300-a_dim
        self.a_lr = 1e-4  # Learning rate of actor
        self.c_lr = 1e-4  # Learning rate of critic
        self.batch_size = 128  # batch_size of training
        self.explore_noise = 0.15  # exploring noise when interacting
        self.explore_noise_decay = 0.998  # Decay rate of explore noise

# Initialize hyperparameters
opt = Hyperparameters()

# Now you can access the hyperparameters like opt.dvc, opt.EnvIdex, etc.
print(opt.dvc)
print(opt.Env_name)

opt.dvc = torch.device("cuda") # from str to torch.device
print(opt.dvc , "---" , type(opt.dvc) )
if torch.cuda.is_available():  
  dev = "cuda:0" 
else:  
  dev = "cpu"  
device = torch.device(dev)  
a = torch.zeros(4,3)    
a = a.to(device)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

def main():
    # Build Env
    env = gym.make(opt.Env_name, render_mode = "human" if opt.render else None)
    eval_env = gym.make(opt.Env_name)
    opt.state_dim = env.observation_space.shape[0]
    opt.action_dim = env.action_space.shape[0]
    opt.max_action = float(env.action_space.high[0])   #remark: action space【-max,max】
    opt.max_e_steps = env._max_episode_steps
    print(f'Env:{opt.Env_name}  state_dim:{opt.state_dim}  action_dim:{opt.action_dim}  '
          f'max_a:{opt.max_action}  min_a:{env.action_space.low[0]}  max_e_steps:{opt.max_e_steps}')

    # Seed Everything
    opt.seed = 6
    env_seed = opt.seed
    np.random.seed(opt.seed)
    torch.manual_seed(opt.seed)
    torch.cuda.manual_seed(opt.seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    print("Random Seed: {}".format(opt.seed))

    # Build DRL model
 
    agent = TD3_agent(**vars(opt)) # var: transfer argparse to dictionary
    
    i = 0;
    total = 0;
    avg = 0;
    if opt.render:
        while True:
            score = evaluate_policy(env, agent, turns=1)
            print('EnvName:', opt.Env_name, 'score:', score)
    else:
        total_steps = 0
        while total_steps < opt.Max_train_steps:
            s, info = env.reset(seed=env_seed)  # Do not use opt.seed directly, or it can overfit to opt.seed
            done = False

            '''Interact & trian'''
            while not done:
                if total_steps < (10*opt.max_e_steps): a = env.action_space.sample() # warm up
                else: a = agent.select_action(s, deterministic=False)
                s_next, r, dw, tr, info = env.step(a) # dw: dead&win; tr: truncated
                r = Reward_adapter(r)
                done = (dw or tr)

                agent.replay_buffer.add(s, a, r, s_next, dw)
                s = s_next
                total_steps += 1

                '''train if its time'''
                # train 50 times every 50 steps rather than 1 training per step. Better!
                if (total_steps >= 2*opt.max_e_steps) and (total_steps % opt.update_every == 0):
                    for j in range(opt.update_every):
                        agent.train()

                '''5000 test for 1 episode'''
                if total_steps % 1000 == 0:
                    env_seed += 100
                    agent.explore_noise *= opt.explore_noise_decay
                    ep_r = evaluate_policy(eval_env, agent, turns=3)
                    i = i + 1
                    total = total + ep_r
                    avg = total / i
                    print(f'Episode: {int(total_steps/1000)}, Episode Reward:{ep_r}')

              
        env.close()
        eval_env.close()


if __name__ == '__main__':
    main()




