from backtester import hammer
print(hammer("AEHR","./datasets/AEHR_History.csv").best_fit_line([1,1.1,1.2,1.3,1.4,1.5],[0.19,0.2,0.22,0.235,0.25,0.27]))