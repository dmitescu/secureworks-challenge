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
        mttd_groups = set([d["department"] for d in model.MTTD.objects.values("department").distinct()])
        mttr_groups = set([d["department"] for d in model.MTTR.objects.values("department").distinct()])
        
        mttds = model.MTTD.objects.all()
        mttrs = model.MTTR.objects.all()

        all_groups = list(mttd_groups.union(mttr_groups))

        mttd_result = []
        mttr_result = []
        
        for group in all_groups:
            relevant_mttds = [mt.duration for mt in mttds if mt.department == group]
            relevant_mttrs = [mt.duration for mt in mttrs if mt.department == group]

            mttd = sum(relevant_mttds)/len(relevant_mttds)
            mttr = sum(relevant_mttrs)/len(relevant_mttds)

            mttd_result.append(mttd)
            mttr_result.append(mttr)

        return [mttd_result, mttr_result], all_groups
            
    def getIntrusionAttempts(self, checked_types):
        ias = [ia["subnet"] for ia in model.IntrusionAttempt.objects.values("subnet").distinct()]
        iaz = model.IntrusionAttempt.objects.all()

        result = []

        for ct in checked_types:
            ct_result = []
            for subnet in ias:
                relevant_ia = [ia for ia in iaz if ia.subnet == subnet and ia.intrusion_type == ct]
                ct_result.append(len(relevant_ia))
            result.append(ct_result)

        return result, ias
        
    def getP2PTraffic(self, start_date, end_date, tranches):
        traffic = model.P2PPacket.objects.all()

        day_count = ((end_date - start_date).days)/tranches
        minute_count = day_count * 24 * 60

        result = []
        
        for i in range(0, tranches):
            relevant_traffic = [t for t in traffic
                                  if t.date > (start_date + timedelta(days = day_count) * i) and t.date < (start_date + timedelta(days = day_count) * (i + 1))]
            packet_count = len(relevant_traffic)
            result.append(packet_count)
            print("!!! ", result)

        return result

