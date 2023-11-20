import torch as torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np


class DeepQNetwork(nn.Module):
    def __init__(self, lr, input_dims, fc1_dims, fc2_dims, n_actions):
        super(DeepQNetwork, self).__init__()
        self.lr = lr
        self.input_dims = input_dims
        self.fc1_dims = fc1_dims
        self.fc2_dims = fc2_dims
        
        self.n_actions = n_actions #Output space

        self.fc1_dims = nn.Linear(*self.input_dims, self.fc1_dims)  #layer1
        self.fc2_dims = nn.Linear(self.fc1_dims, self.fc2_dims)     #layer2
        self.fc3_dims = nn.Linear(self.fc2_dims, self.n_actions)    #layer3

        self.optimizer = optim.Adam(self.parameters(), lr=self.lr)
        self.loss = nn.MSELoss()

        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu') #selecting gpu if available
        self.to(self.device) #moving model to selected device.

    def forward(self, state):
        x = F.relu(self.fc1_dims(state)) #computing the output of the first layer
        x = F.relu(self.fc2_dims(x))     #computing the output of the second layer
        actions = self.fc3_dims(x)       #computing the output of the third layer, that is, the output of the network

        return actions
    
class Agent():
    def __init__(self, gamma, epsilon, lr, input_dims, batch_size, n_actions, 
                 max_mem_size=1000000,  #maximum memory size, I do not know anything else either, we shall f'in see, TO BE UNDERSTOOD.
                 eps_end=0.01,          #minimum epsilon value, TO BE UNDERSTOOD
                 eps_dec=5e-4):         #epsilon decay value, TO BE UNDERSTOOD
        self.gamma = gamma              #TF is this? TO BE UNDERSTOOD
        self.epsilon = epsilon          #TF is this? TO BE UNDERSTOOD
        self.lr = lr
        self.input_dims = input_dims
        self.batch_size = batch_size    #TF is this? TO BE UNDERSTOOD
        self.n_actions = n_actions
        self.mem_size = max_mem_size
        
        self.action_space = [i for i in range(self.n_actions)] #action space
        self.mem_cntr = 0 #memory counter, to keep track of the position of the first available memory

        self.Q_eval = DeepQNetwork(self.lr, n_actions=n_actions, input_dims=input_dims, fc1_dims=256, fc2_dims=256) #Q_eval is the main network

        self.state_memory = np.zeros((self.mem_size, *input_dims), dtype=np.float32)        #TO BE UNDERSTOOD
        #Memort to tell the agent next state
        self.new_state_memory = np.zeros((self.mem_size, *input_dims), dtype=np.float32)
        self.action_memory = np.zeros(self.mem_size, dtype=np.int32)    #memory for action
        self.reward_memory = np.zeros(self.mem_size, dtype=np.float32)  #memory for reward
        self.terminal_memory = np.zeros(self.mem_size, dtype=np.bool)   #memory for terminal state, future value of terminal state is 0

    def store_transition(self, state, action, reward, state_, done):
        index = self.mem_cntr % self.mem_size # calculating the index of the current memory to store the transition
        self.state_memory[index] = state      # storing the current state
        self.new_state_memory[index] = state_
        self.reward_memory[index] = reward    # storing the reward
        self.action_memory[index] = action    # storing the action
        self.terminal_memory[index] = done    # storing the terminal state
        self.mem_cntr += 1                    # increasing the memory counter

    #a method for choosing actions
    def choose_action(self, observation):
        if np.random.random() > self.epsilon:#if so, we want to figure out the best "known" action
            #[] is used to convert the observation to a list
            state = torch.tensor([observation]).to(self.Q_eval.device) #sending variables we want to use to the device
            actions = self.Q_eval.forward(state)    #passing the state to DQN, getting the action values, that is, the output of the network
            action = torch.argmax(actions).item()   #selecting the action with the highest value for that state
        else:
            action = np.random.choice(self.action_space)

        return action
    
    #a method for learning, to be called always, a bit stupid and can be improved for sure, but f it.
    def learn(self):
        #the batch is not filled, learn no shit and return.
        if self.mem_cntr < self.batch_size:
            return
        #If batch is filled, we learn!
        self.Q_eval.optimizer.zero_grad()
        max_mem = min(self.mem_cntr, self.mem_size)                         #we get upto the last filled memory
        batch = np.random.choice(max_mem, self.batch_size, replace=False)   #wtf
        batch_index = np.arrange(self.batch_size, dtype=np.int32)           #calculating the batch index...
       
        state_batch = torch.tensor(self.state_memory[batch]).to(self.Q_eval.device)
        new_state_batch = torch.tensor(self.new_state_memory[batch]).to(self.Q_eval.device)
        reward_batch = torch.tensor(self.reward_memory[batch]).to(self.Q_eval.device)
        terminal_batch = torch.tensor(self.terminal_memory[batch]).to(self.Q_eval.device)

        action_batch = self.action_memory[batch]

        q_eval = self.Q_eval.forward(state_batch)[batch_index, action_batch] #for the actions we actually took! hence, subsequence in the array...
        q_next = self.Q_eval.forward(new_state_batch)
        q_next[terminal_batch] = 0.0        #0.0 for terminal??? I geuss this is the logic

        #max function returns the value, as well as the index. We only need the value, hence the [0]
        q_target = reward_batch + self.gamma*torch.max(q_next, dim=1)[0] #calculating the target value

        loss = self.Q_eval.loss(q_target, q_eval).to(self.Q_eval.device) #calculating the loss, giving it to the device.
        loss.backward()
        self.Q_eval.optimizer.step()

        #Each time we learn, we decrease the epsilon by one, so that as time goes we act less randomly. 
        #Please check the previous method to understand why.
        self.epsilon = self.epsilon - self.eps_dec if self.epsilon > self.eps_min else self.eps_min

