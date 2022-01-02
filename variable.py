"""
    in this file, we have some classes that use as a variable in the entire program 
    Expense       -> a class that each object contains a purchase
    Place         -> a class that each object contains a shop or a website or an organization
    Date          -> a class that each object contains a specific time which distinct by year, month, day, hour, minute
    Person        -> a class that each object contains a family member
    PaymentMethod -> a class that each object contains a way to pay for purchase for instance a bank name   
"""

import datetime


class Place:
    def __init__(self, name: str, distance: int, address: str) -> None:
        """
            the place could be a website or a shop or an organization 
            if the place is website put 0 as distance
        """
        self.name = name
        self.distance = distance
        self.address = address

class Date:
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour 
        self.minute = minute
        self._compute_week_day()
    
    def _compute_week_day(self) -> None:
        intDay = datetime.date(year=self.year, month=self.month, day=self.day).weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.week_day = days[intDay]

    def show(self) -> tuple:
        """return year/month/day hour:minut weekday"""
        return f"{self.year}/{self.month}/{self.day}", f"{self.hour}:{self.minute}", self.week_day


class Person:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

class PaymentMethod:
    def __init__(self, name: str, number:str) -> None:
        """if the payment method doesn't have any number, use "0000" as number"""
        self.name = name
        self.number = number

class Expense:
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    today = Date(2022, 1, 2, 21, 38)
    print(*today.show(), sep=' - ')