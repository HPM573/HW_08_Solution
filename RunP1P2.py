import Classes as Cls

setofgames = Cls.SetOfGames(id=1, prob_head=0.5, n_games=1000)
outcome = setofgames.simulate()

print('The Expected reward is', outcome.get_ave_reward())
print('The 95% CI of the expected reward is',outcome.get_CI_reward(0.05))

print('Probability of loss in a single game is', outcome.get_loss_prob())
print('The 95% CI of loss probability is', outcome.get_CI_probLoss(0.05))

#interpretation
print('If we run our simulation many times, on average 95% of the confidence intervals generated will capture the true mean')
