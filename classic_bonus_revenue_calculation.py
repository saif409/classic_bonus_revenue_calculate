class Qtech:

    def __init__(self, r_commission, cb_commission, deposit, agent_commission, profit):
        self.r_commission = r_commission
        self.cb_commission = cb_commission
        self.deposit = deposit
        self.agent_commission = agent_commission
        self.profit = profit

    def determine_total_profit(self):
        total_profit = 0
        if self.r_commission < self.cb_commission:
            total_profit = (self.profit / self.agent_commission) * self.cb_commission
        else:
            total_profit = self.deposit * (self.agent_commission / 1000)
        return total_profit

    def rev_share(self):
        shared_rev = 0
        shared_rev = (self.profit / self.cb_commission) * self.agent_commission
        return shared_rev


def main():
    q_tech = Qtech(1, 2, 3, 4, 5)
    print(q_tech.determine_total_profit())
    print(q_tech.rev_share())


if __name__ == '__main__':
    main()
