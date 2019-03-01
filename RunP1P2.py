import Classes as Cls

setOfGames = Cls.SetOfGames(id=0, prob_head=0.5)
setOfGames.simulate(n_games=1000)


print('The Expected reward is', setOfGames.outcomes.get_ave_reward())
print('The 95% CI of the expected reward is', setOfGames.outcomes.get_CI_reward(0.05))

print('Probability of loss in a single game is', setOfGames.outcomes.get_loss_prob())
print('The 95% CI of loss probability is', setOfGames.outcomes.get_CI_prob_Loss(0.05))

# interpretation
print('If we run our simulation many times, '
      'on average 95% of the confidence intervals generated will capture the true mean')
