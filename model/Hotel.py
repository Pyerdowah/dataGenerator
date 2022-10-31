class Hotel:
    def __init__(self, hotelId, numberOfStars, name, address, country, facilities):
        self.hotelId = hotelId
        self.numberOfStars = numberOfStars
        self.name = name
        self.address = address
        self.country = country
        self.facilities = facilities

    def __str__(self):
        return str(self.hotelId) + " \n" + str(self.numberOfStars) + " \n" + str(self.name) + " \n" + str(self.address) \
               + " \n" + str(self.country) + " \n" + str(self.facilities) + "\n\n"
