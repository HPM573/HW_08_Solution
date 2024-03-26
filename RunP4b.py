import deampy.plots.histogram as hist

import Classes as Cls

# create a multiple game sets
multipleGameSets = Cls.MultipleGameSets(ids=range(1000), prob_head=0.5)
# simulate all game sets
multipleGameSets.simulate(n_games_in_set=10)

# print projected reward
print('Projected reward from playing the game 20 times:',
      multipleGameSets.statGameSetRewards.get_mean())
# print projection interval
print('95% projection interval of average rewards',
      multipleGameSets.statGameSetRewards.get_PI(0.05))

# distribution of reward from playing the game 10 times
hist.plot_histogram(
    data=multipleGameSets.gameSetRewards,
    bin_width=100,
    title='Reward from playing the game 10 times',
    x_label='Mean Rewards',
    y_label='Count')


print('Since the gambler gets to play this game only 10 times, '
      'knowing the distribution of the '
      'reward from these 10 games is important.'
      '\nTherefore, we provide the gambler with the '
      'sample mean of the reward and the projection interval to communicate the uncertainty in the possible '
      'reward after playing the game 10 times.')
