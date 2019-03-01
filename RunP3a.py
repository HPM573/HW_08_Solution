import Classes as Cls

setOfGames = Cls.SetOfGames(id=0, prob_head=0.5)
setOfGames.simulate(n_games=10000)

print('Expected reward is', setOfGames.outcomes.get_ave_reward())
print('The 95% CI of expected reward is', setOfGames.outcomes.get_CI_reward(0.05))

print('We need a steady-state simulation for this perspective.')
print('We are able to rely on the Law of Large Numbers to make inference.')
print('This lets us use the sample mean and confidence intervals for interpretation.')
