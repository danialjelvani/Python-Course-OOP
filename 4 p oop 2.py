# train:

class Train:
    def __init__(
            self,
            Last_visited_city: str,
            Weight_Capacity: float,
            Is_On_Trip: bool
    ):
        self.lvc = Last_visited_city
        self.wc = Weight_Capacity
        self.iot = Is_On_Trip


class Trip:
    all_cities = (
        'arak', 'ardabil', 'isfahan',
        'ahvaz', 'bojnurd', 'mashad',
    )

    def __init__(
        self,
        train: Train,
        origin_city: str,
        destination_city: str,
    ):
        if not isinstance(train, Train):
            raise Exception('this input is not a train')

        self.train = train
        self.origin_city = origin_city
        self.destination_city = destination_city
        self.passengers = []

    def origin_city_validation(self):
        if self.origin_city not in self.all_cities:
            raise Exception('this input is not a verified city')
        return self.origin_city


train1 = Train('isfahan', 2000, True)

trip1 = Trip(train1, 'ahvaz', 'mashad')
