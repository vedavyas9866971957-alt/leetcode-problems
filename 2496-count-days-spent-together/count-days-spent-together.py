class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def date(date1,date2):
            month1,day1=map(int,date1.split("-"))
            month2,day2=map(int,date2.split("-"))
            total1=sum(months[:month1-1])+day1
            total2=sum(months[:month2-1])+day2
            return total1,total2

        return max(0,1+min(date(leaveAlice,leaveBob))-max(date(arriveAlice,arriveBob)))
        