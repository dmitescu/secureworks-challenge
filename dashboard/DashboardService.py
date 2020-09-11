from . import model

from datetime import datetime, timedelta

class DashboardService():
    __instance = None
           
    @staticmethod 
    def getInstance():
      if DashboardService.__instance == None:
          DashboardService()
      return DashboardService.__instance
       
    def __init__(self):
       if DashboardService.__instance != None:
           raise Exception("This class is a singleton!")
       else:
           DashboardService.__instance = self

    def getUptime(self, start_date, end_date, tranches):
        downtime_entries = model.Downtime.objects.filter(date__gte=start_date, date__lte=end_date).all()

        result = []

        day_count = ((end_date - start_date).days)/tranches
        minute_count = day_count * 24 * 60

        for i in range(0, tranches):
            relevant_downtimes = [d for d in downtime_entries
                                  if d.date > (start_date + timedelta(days = day_count) * i) and d.date < (start_date + timedelta(days = day_count) * (i + 1))]
            duration_per_tranche = sum([d.duration for d in relevant_downtimes])
            result.append(1 - duration_per_tranche/minute_count)
            
        return result

    def getMTT(self):
        mttds = model.MTTD.objects.all()
        mttrs = model.MTTR.objects.all()
