
from backtesting import Backtest, Strategy
from backtesting.test import GOOG

from backtesting.lib import crossover

import talib


class RsiOscillator(Strategy):

    upper_bound = 70
    lower_bound = 30

    # created as soon as objected is created
    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, 14)

    # Goes through each candle and decides if it wants to buy on next candle

    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.buy()


bt = Backtest(GOOG, RsiOscillator, cash=10_000)
stats = bt.run()

print(stats)
