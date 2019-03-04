import Classes as Cls
import SimPy.FigureSupport as Fig

# create a multiple game sets
multipleGameSets = Cls.MultipleGameSets(ids=range(5000), prob_head=0.5)
# simulate all game sets
multipleGameSets.simulate(n_games_in_set=10)

# print projected reward
print('Projected reward',
      multipleGameSets.statGameRewards.get_mean())
# print projection interval
print('95% projection interval of average rewards',
      multipleGameSets.statGameRewards.get_PI(0.05))

# distribution of reward from playing the game 10 times
Fig.graph_histogram(
    data=multipleGameSets.gameSetRewards,
    bin_width=100,
    title='Reward from playing the game 10 times',
    x_label='Mean Rewards',
    y_label='Count')

print('We need a transient-state simulation for this perspective.')
print('We are not able to rely on the Law of Large Numbers to make inference because our data is very limited.')
print('Therefore, we must use the sample mean and projection intervals for interpretation.')
