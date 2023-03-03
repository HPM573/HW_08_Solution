import Classes as Cls

setOfGames = Cls.SetOfGames(id=0, prob_head=0.5)
setOfGames.simulate(n_games=10000)

print('How much is the casino owner expected to pay to a gambler'
      '(if negative, it means that the gambler is paying to the casino owner):', setOfGames.statRewards.get_mean())
print('The 95% CI is', setOfGames.statRewards.get_t_CI(0.05))

print('\nWe need a steady-state simulation for this perspective.')
print('We are able to rely on the Law of Large Numbers to make inference about '
      'home much the casino owner could make from each gambler.')
print('This lets us use the sample mean and confidence intervals for interpretation.')
