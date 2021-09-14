from Data_Structures.List_Month import List_Month
from Data_Structures.List_Semester import List_Semester


class Year:
    def __init__(self, _number_year):
        self.number_year = _number_year
        self.list_semesters = List_Semester()
        self.list_months = List_Month()
