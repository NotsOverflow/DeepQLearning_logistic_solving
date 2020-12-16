#
#              _            _
# |\| _ _|_ _ / \    _  ___|_ |  _
# | |(_) |__> \_/\_/(/_ |  |  | (_)\^/
#
# ntest.py created December 1st 2020
# by richard juan (contact@richardjuan-business.com)
#
# ----------------------------------------------
#
# using Deep Q Learning to solve MCDO
#
# ----------------------------------------------

from mcdo import MacDo, Agent, plotLearning
import numpy as np

if __name__ == '__main__':
    env = MacDo()
    brain = Agent(gamma=0.75, epsilon=0.5, batch_size=16, n_actions=30,
                  input_dims=[16], alpha=0.03)

    scores = []
    eps_history = []
    num_games = 800
    score = 0
    for i in range(num_games):
        if i % 10 == 0 and i > 0:
            avg_score = np.mean(scores[max(0, i-10):(i+1)])
            print('episode: ', i,'score: ', score,
                 ' average score %.3f' % avg_score,
                'epsilon %.3f' % brain.EPSILON)
        else:
            print('episode: ', i,'score: ', score)
        eps_history.append(brain.EPSILON)
        done = False
        observation = env.reset()
        score = 0
        while not done:
            action = brain.chooseAction(observation)
            observation_, reward, done, info = env.step(action)
            score += reward
            brain.storeTransition(observation, action, reward, observation_,
                                  done)
            observation = observation_
            brain.learn()
            env.render()
        scores.append(score)

    x = [i+1 for i in range(num_games)]
    filename = str(num_games) + 'Games' + 'Gamma' + str(brain.GAMMA) + \
               'Alpha' + str(brain.ALPHA) + 'Memory'  +'.png'
    plotLearning(x, scores, eps_history, filename)