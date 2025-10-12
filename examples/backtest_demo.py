# examples/demo_backtest_report.py

from reports.backtest_report_generator import build_report_html
import pandas as pd
import numpy as np

# Simulate a simple backtest
days = pd.date_range('2020-01-01', periods=250)
backtests = {
    'Demo Strategy': pd.Series(10000*(1+0.001)**np.arange(250), index=days)
}

# Generate HTML report
build_report_html(backtests, 'demo_report.html')
print("Demo report generated: demo_report.html")
