import Classes as Cls
import SimPy.FigureSupport as Fig

trial = Cls.SetOfGames(id = 1,prob_head= 0.5, n_games=1000)
test = trial.simulate()

print('Expected reward is', test.get_ave_reward())
print('The 95% CI of expected reward is', test.get_CI_reward(0.05))

Fig.graph_histogram(
    data = trial.get_reward_list(),
    title = 'Histogram of rewards from 1000 Games obtained from steady state simulation model',
    x_label='Game Rewards',
    y_label='Frequency'
)
