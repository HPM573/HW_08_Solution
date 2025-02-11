import Classes as Cls

setOfGames = Cls.SetOfGames(id=0, prob_head=0.5)
setOfGames.simulate(n_games=10000)

print('How much is the casino owner expected to pay to a gambler'
      '(if negative, it means that the gambler is paying to the casino owner):', setOfGames.statRewards.get_mean())
print('The 95% CI is', setOfGames.statRewards.get_t_CI(0.05))

print('Since the casio owner gets to play this game many time', 
      'we are able to rely on the Law of Large Numbers to make inference about '
      'how much money the casino owner could make on average from each gambler.')
print('This lets us use the sample mean and confidence intervals for interpretation.')
