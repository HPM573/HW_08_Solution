import numpy as np
import SimPy.StatisticalClasses as Stat


class Game(object):
    def __init__(self, id, prob_head):
        self._id= id
        self._rnd = np.random
        self._rnd.seed(id)
        self._probHead = prob_head
        self._countWins = 0

    def simulate(self, n_of_flips):

        count_tails = 0 #number of consecutive tails so far, set to 0

        for i in range(n_of_flips):
            if self._rnd.random_sample() < self._probHead:
                if count_tails >= 2:
                    self._countWins += 1
                count_tails = 0

            else:
                count_tails += 1

    def get_reward(self):
        return 100*self._countWins - 250

class SetOfGames:
    def __init__(self, id, prob_head, n_games):
        self.id = id
        self._gameRewards = []
        self.count_loss = []
        self._num_loss = 0 #number of losses; start with zero
        self.n_games = n_games
        self.prob_head = prob_head

    def simulate(self):
        for n in range(self.n_games):
            #create a new game
            game = Game(id=self.id*self.n_games+n, prob_head=self.prob_head)
            #simulate the game with 20 flips
            game.simulate(20)
            #store the reward
            self._gameRewards.append(game.get_reward())

        for k in self._gameRewards:
            if k < 0:
                i=1
                self.count_loss.append(i)
            else:
                i=0
                self.count_loss.append(i)

        return SetOfGamesOutcomes(self)


    def get_reward_list(self):
        return self._gameRewards

    def get_loss_list(self):
        return self.count_loss


class SetOfGamesOutcomes:
    def __init__(self, simulated_cohort):

        self.simulatedCohort = simulated_cohort
        self.sumStat_gameRewards = Stat.SummaryStat('Reward List', self.simulatedCohort.get_reward_list())
        self.sumStat_gameProbLoss = Stat.SummaryStat('Probability  of loss', self.simulatedCohort.get_loss_list())

    def get_ave_reward(self):
        return self.sumStat_gameRewards.get_mean()

    def get_CI_reward(self,alpha):
        return self.sumStat_gameRewards.get_t_CI(alpha)

    def get_min_reward(self):
        return self.sumStat_gameRewards.get_min()

    def get_max_reward(self):
        return self.sumStat_gameRewards.get_max()

    def get_loss_prob(self):
        return self.sumStat_gameProbLoss.get_mean()

    def get_CI_probLoss(self,alpha):
        return self.sumStat_gameProbLoss.get_t_CI(alpha)


class MultipleGameSets:
    def __init__(self, ids, prob_head, n_games):
        self.ids = ids
        self.probs_head = prob_head
        self.num_games = n_games

        self.game_rewards = []
        self.meanGameReward = []
        self.sumStat_meanGameReward = None

    def simulation(self):
        for i in self.ids:
            setofGames = SetOfGames(i, self.probs_head, self.num_games)
            setofGames.simulate()
            self.game_rewards.append(setofGames.get_reward_list())
            self.meanGameReward.append(setofGames.simulate().get_ave_reward())

        self.sumStat_meanGameReward = Stat.SummaryStat('Mean Rewards', self.meanGameReward)

    def get_setofgames_meanrewards(self,index):
        return self.meanGameReward[index]

    def get_setofgames_CI_meanreward(self,index, alpha):
        stats = Stat.SummaryStat('', self.game_rewards[index])
        return stats.get_t_CI(alpha)

    def get_all_meanrewards(self):
        return self.meanGameReward

    def get_overall_mean_reward(self):
        return self.sumStat_meanGameReward.get_mean()

    def get_cohort_PI_reward(self, index, alpha):
        stats = Stat.SummaryStat('', self.game_rewards[index])
        return stats.get_PI(alpha)

    def get_PI_meanreward(self, alpha):
        return self.sumStat_meanGameReward.get_PI(alpha)


