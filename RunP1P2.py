import Classes as Cls

setOfGames = Cls.SetOfGames(id=0, prob_head=0.5)
setOfGames.simulate(n_games=1000)


print('\nExpected reward from playing this game is', setOfGames.statRewards.get_mean())
print('The 95% CI of the expected reward is', setOfGames.statRewards.get_t_CI(0.05))

print('\nProbability of loss in a single game is', setOfGames.statIfLoss.get_mean())
print('The 95% CI of loss probability is', setOfGames.statIfLoss.get_t_CI(0.05))

# interpretation
print('\nIf we run our simulation many times and build a confidence interval for each simulation run, '
      'on average 95% of these confidence intervals will capture the true mean.')


current_ci = setOfGames.statRewards.get_t_CI(0.05)
current_hl = (current_ci[1] - current_ci[0])/2
current_n = 1000  # current number of simulation runs
new_hl = 2  # dollars

new_n = int(current_n * pow(current_hl/new_hl, 2))

print('\nTo reduce the half-length for the expected award to ${}, '
      'the number of simulation runs should be at least increased to {}.'. format(new_hl, new_n))
