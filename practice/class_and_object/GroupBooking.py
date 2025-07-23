# Group Bookings by Date
# Context: Train/Flight/Hotel Reports
# Input:
# [
#  {"user": "A", "date": "2025-07-10"},
#  {"user": "B", "date": "2025-07-11"},
#  {"user": "C", "date": "2025-07-10"},
# ]

# Output:
# {
#  "2025-07-10": ["A", "C"],
#  "2025-07-11": ["B"]
# }
from collections import defaultdict

class GroupBooking:
    def __init__(self,booking):
        self.booking = booking
        
    def group_by_date(self):
        grouped = defaultdict(list)
        for b in self.booking:
            grouped[b["date"]].append(b["user"])
        return grouped
    
data = [
    {"user": "A", "date": "2025-07-10"},
    {"user": "B", "date": "2025-07-11"},
    {"user": "C", "date": "2025-07-10"},
]

gb = GroupBooking(data)
print(gb.group_by_date())