import numpy as np
import backtester as fin

profit_cap = []
stop_loss = []

for i in range(1, 101, 1):
    profit_cap.append(i)
    stop_loss.append(i)

stop_loss.sort(reverse=True)

