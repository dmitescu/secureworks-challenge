from django.shortcuts import render, redirect

from .plots import AreaChart
from .plots import HorizontalBarChart
from .plots import VerticalBarChart
from .plots import ScatterPlot

from .DashboardService import DashboardService

from datetime import datetime

UPTIME_START_DATE = datetime(2015, 1, 1)
UPTIME_END_DATE = datetime(2020, 1, 1)
UPTIME_TRANCHES = 5

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    s = DashboardService.getInstance()
    uptime = s.getUptime(UPTIME_START_DATE, UPTIME_END_DATE, UPTIME_TRANCHES)
    
    UptimeChart = AreaChart.AreaChart(uptime)
    MTTChart = HorizontalBarChart.HorizontalBarChart([], [])
    IntrusionAttemptsChart = VerticalBarChart.VerticalBarChart([], [])
    P2PTrafficChart = ScatterPlot.ScatterPlot([])
    
    context = {"UptimeChart": UptimeChart.series,
               "MTTChart": {"groups": ["MTTD", "MTTR"], "seriesMTTD": MTTChart[0], "seriesMTTR": MTTChart[1]},
               "IntrusionAttemptsChart": {},
               "P2PTrafficChart": {},}
    
    return render(request, "dashboard.html", context)
