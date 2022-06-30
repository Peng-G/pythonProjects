import gym
import pygame
import numpy as np


class BespokeAgent:
    """
        create a new agent class, firstly focus on the decision process.
        """

    def __init__(self, env):  # 初始化
        pass

    def decide(self, observation):  # 决策
        position, velocity = observation
        lb = min(-0.09 * (position + 0.25) ** 2 + 0.03,
                 0.3 * (position + 0.9) ** 4 - 0.008)
        ub = -0.07 * (position + 0.38) ** 2 + 0.07
        if lb < velocity < ub:
            action = 2
        else:
            action = 0
        return action  # 返回动作

    def learn(self, *args):  # 学习
        pass


def play_montecarlo(env, agent, render=False, train=False):
    """
    play the game with the agent, and return the total reward.
    :param env: class object, the environment.
    :param agent: class object, the agent.
    :param render: True or False
    :param train: True or False
    :return: episode_reward
    """
    episode_reward = 0.  # 记录回合总奖励，初始化为0
    observation = env.reset()  # 重置游戏环境，开始新回合
    while True:  # 不断循环，直到回合结束
        if render:  # 判断是否显示
            env.render()  # 显示图形界面，图形界面可以用 env.close() 语句关闭
        action = agent.decide(observation)
        next_observation, reward, done, _ = env.step(action)  # 执行动作
        episode_reward += reward  # 收集回合奖励
        if train:  # 判断是否训练智能体
            agent.learn(observation, action, reward, done)  # 学习
        if done:  # 回合结束，跳出循环
            break
        observation = next_observation
    return episode_reward  # 返回回合总奖励


if __name__ == '__main__':
    # create an environment object
    env = gym.make('MountainCar-v0')
    env.reset()
    # take a look at the environment, e.g. the state space.
    print('observation space = {}'.format(env.observation_space))
    print('action space = {}'.format(env.action_space))
    print('observation scale = {} ~ {}'.format(env.observation_space.low, env.observation_space.high))
    print('number of actions = {}'.format(env.action_space.n))

    # env.seed(0)  # 设置随机数种子,只是为了让结果可以精确复现,一般情况下可删去
    agent = BespokeAgent(env)  # create a new agent
    episode_reward = play_montecarlo(env, agent, render=True)
    print('episode reward = {}'.format(episode_reward))
    # env.close()  # 此语句可关闭图形界面
    episode_rewards = [play_montecarlo(env, agent) for _ in range(100)]
    print('average episode reward = {}'.format(np.mean(episode_rewards)))
