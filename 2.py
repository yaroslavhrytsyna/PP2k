class Aircraft:
    def __init__(self, id_aircraft, reg_code, id_type, id_owner):
        self._id_aircraft = id_aircraft
        self.reg_code = reg_code
        self.id_type = id_type
        self.id_owner = id_owner

    @property
    def id_aircraft(self):
        return self._id_aircraft

    def display_info(self):
        return f"Aircraft ID: {self.id_aircraft}, Registration Code: {self.reg_code}"

    def update_registration(self, new_reg_code):
        self.reg_code = new_reg_code

    @staticmethod
    def aircraft_type_description():
        return "This method returns a description of the aircraft type."

class Service:
    def __init__(self, id_service, name, price):
        self.id_service = id_service
        self.name = name
        self.price = price

    def display_service_info(self):
        return f"Service ID: {self.id_service}, Name: {self.name}, Price: {self.price}"

class Timetable(Aircraft):
    def __init__(self, id_aircraft, reg_code, id_type, id_owner, id_timetable, date, hour, quarter, type_):
        super().__init__(id_aircraft, reg_code, id_type, id_owner)
        self.id_timetable = id_timetable
        self.date = date
        self.hour = hour
        self.quarter = quarter
        self.type_ = type_

    def display_timetable(self):
        return f"Timetable ID: {self.id_timetable}, Date: {self.date}, Hour: {self.hour}, Quarter: {self.quarter}, Type: {self.type_}"

class Parked(Aircraft, Service):
    def __init__(self, id_aircraft, reg_code, id_type, id_owner, id_service, name, price, id_parked, id_place, starting_date, starting_hour, ending_date, ending_hour):
        Aircraft.__init__(self, id_aircraft, reg_code, id_type, id_owner)
        Service.__init__(self, id_service, name, price)
        self.id_parked = id_parked
        self.id_place = id_place
        self.starting_date = starting_date
        self.starting_hour = starting_hour
        self.ending_date = ending_date
        self.ending_hour = ending_hour

    def display_parked_info(self):
        return f"Parked ID: {self.id_parked}, Place ID: {self.id_place}, Starting: {self.starting_date} {self.starting_hour}, Ending: {self.ending_date} {self.ending_hour}"

    def calculate_service_cost(self):
        duration_hours = (self.ending_hour - self.starting_hour)
        if duration_hours < 0:
            duration_hours += 24  
        total_cost = duration_hours * self.price
        return f"Total Service Cost: {total_cost}"

def main():
    
    timetable = Timetable(1, "AB123", 2, 3, 1001, "2024-09-28", 14, 30, 1)
    parked = Parked(2, "CD456", 4, 5, 2001, "Maintenance", 500, 3001, 4001, "2024-09-28", 8, "2024-09-28", 18)

    print(timetable.display_info())
    print(timetable.display_timetable())
    
    print(parked.display_info())
    print(parked.display_service_info())
    print(parked.display_parked_info())
    
    aircrafts = [timetable, parked]
    for aircraft in aircrafts:
        print(aircraft.display_info())
    
    timetable.update_registration("EF789")
    print(timetable.display_info())

    print(parked.calculate_service_cost())

if __name__ == "__main__":
    main()
