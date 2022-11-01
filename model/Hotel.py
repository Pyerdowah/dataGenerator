class Hotel:
    def __init__(self, hotelId, numberOfStars, name, address, country, facilities):
        self.hotelId = hotelId
        self.numberOfStars = numberOfStars
        self.name = name
        self.address = address
        self.country = country
        self.facilities = facilities

    def __str__(self):
        return str(self.hotelId) + "|" + str(self.numberOfStars) + "|" + str(self.name) + "|" + self.address.replace('\n', ', ') \
               + "|" + str(self.country) + "|" + str(self.facilities)

    def getHotelId(self):
        return self.hotelId
