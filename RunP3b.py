import Classes as Cls
import SimPy.Plots.Histogram as Hist

# create a multiple game sets
multipleGameSets = Cls.MultipleGameSets(ids=range(1000), prob_head=0.5)
# simulate all game sets
multipleGameSets.simulate(n_games_in_set=10)

# print projected reward
print('Projected reward',
      multipleGameSets.statMultipleGameRewards.get_mean())
# print projection interval
print('95% projection interval of average rewards',
      multipleGameSets.statMultipleGameRewards.get_PI(0.05))

# distribution of reward from playing the game 10 times
Hist.plot_histogram(
    data=multipleGameSets.gameSetRewards,
    bin_width=100,
    title='Reward from playing the game 10 times',
    x_label='Mean Rewards',
    y_label='Count')

print('We need a transient-state simulation for this perspective.')
print('We are not able to rely on the Law of Large Numbers to make inference because '
      'the gambler gets to play this game only 10 times.')
print('Therefore, we must use the sample mean and projection intervals for interpretation.')
