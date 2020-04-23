class TourCard:
    insurance_cost_per_day_in_hryvnas = 40.5

    def __init__(self, country=None, duration_in_days=None, price_in_ukrainian_hryvnas=None,
                 capacity_in_seats=None,
                 guide_name=None, hotel_name=None):
        self.country = country
        self.duration_in_days = duration_in_days
        self.price_in_ukrainian_hryvnas = price_in_ukrainian_hryvnas
        self.capacity_in_seats = capacity_in_seats
        self.guide_name = guide_name
        self.hotel_name = hotel_name

    @staticmethod
    def staticmethod():
        return TourCard.insurance_cost_per_day_in_hryvnas

    def __str__(self):
        country = "Country: {0}\n".format(self.country)
        duration_in_days = "Duration in days: {0}\n".format(self.duration_in_days)
        price_in_ukrainian_hryvnas = "Price in UAH: {0}\n".format(self.price_in_ukrainian_hryvnas)
        capacity_in_seats = "Capacity in seats: {0}\n".format(
            self.capacity_in_seats)
        guide_name = "Guide name: {0}\n".format(self.guide_name)
        hotel_name = "Hotel name: {0}\n".format(self.hotel_name)
        insurance_cost_per_day_in_hryvnas = "Insurance cost per day: {0}\n".format(
            TourCard.insurance_cost_per_day_in_hryvnas)
        return country + duration_in_days + price_in_ukrainian_hryvnas + capacity_in_seats + guide_name + \
               hotel_name + insurance_cost_per_day_in_hryvnas

    def __del__(self):
        print("Delete " + self.__class__.__name__ + " | Object ID: " + str(id(self)))
        return
