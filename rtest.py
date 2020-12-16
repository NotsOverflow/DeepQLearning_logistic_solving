#              _            _
# |\| _ _|_ _ / \    _  ___|_ |  _
# | |(_) |__> \_/\_/(/_ |  |  | (_)\^/
#
# rtest.py created December 1st 2020
# by richard juan (contact@richardjuan-business.com)
#
#
# ----------------------------------------------
#
# using Random to solve MCDO
#
# ----------------------------------------------

from mcdo import MacDo
import random
import matplotlib.pyplot as plt

totals = []
run_times = 800
env = MacDo()

def basic_policy(obs):
    return random.choice(env.action_space)


if __name__ == '__main__':
    day = 0.0
    for episode in range(run_times):
        episode_reward = 0
        env.set_day(day)
        obs = env.reset()
        done = False
        while not done:
            action = basic_policy(obs)
            obs, reward, done, info = env.step(action)
            episode_reward += reward
            # uncoment to render 
            #env.render()
        totals.append(episode_reward)
        day = round( day + 0.1, 1)
        if day > 0.7:
            day = 0.0
    plt.plot(totals)
    plt.show()
