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

IA_CHECKED_TYPES = ["H", "Q"]


P2P_START_DATE = datetime(2015, 1, 1)
P2P_END_DATE = datetime(2020, 1, 1)
P2P_TRANCHES = 5

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    s = DashboardService.getInstance()
    
    uptime = s.getUptime(UPTIME_START_DATE, UPTIME_END_DATE, UPTIME_TRANCHES)
    mttResult, mttGroups = s.getMTT()
    iaResult, iaGroups = s.getIntrusionAttempts(IA_CHECKED_TYPES)
    p2pTraffic = s.getP2PTraffic(P2P_START_DATE, P2P_END_DATE, P2P_TRANCHES)
    
    UptimeChart = AreaChart.AreaChart(uptime)
    MTTChart = HorizontalBarChart.HorizontalBarChart(mttResult, mttGroups)
    IntrusionAttemptsChart = VerticalBarChart.VerticalBarChart(iaResult, iaGroups)
    P2PTrafficChart = ScatterPlot.ScatterPlot(p2pTraffic)
    
    context = {"UptimeChart": UptimeChart.series,
               "MTTChart": {"groups": MTTChart.groups,
                            "seriesMTTD": MTTChart.series[0],
                            "seriesMTTR": MTTChart.series[1]},
               "IntrusionAttemptsChart": {"groups": IntrusionAttemptsChart.groups,
                                          "seriesSSH": IntrusionAttemptsChart.series[0],
                                          "seriesSQL": IntrusionAttemptsChart.series[1]},
               "P2PTrafficChart": P2PTrafficChart.series}
    
    return render(request, "dashboard.html", context)
