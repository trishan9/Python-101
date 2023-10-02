class TourForm:
    def __init__(self, name, batch, phone):
        self._name = name
        self._batch = batch
        self._phone = phone

    def check_status(self):
        print(f"{self._name} from {self._batch} is going to tour. His contact Details: {self._phone}")

    @property #Getter
    def info(self):
        information = {
            "name": self._name,
            "batch": self._batch,
            "phone": self._phone,
        }
        return information
    
    @info.setter #Setter
    def info(self, new_data):
        self._name = new_data["name"]
        self._batch = new_data["batch"]
        self._phone = new_data["phone"]


class TeacherTourForm(TourForm):
    def check_bill(self):
        print("Tour's Total Bill is $991999.99")


trishan = TourForm("Trishan Wagle", "C35B", "+977-9898989898")
trishan.check_status()
trishan.info = {
    "name": "Trishan",
    "batch": "C35C",
    "phone": "100",
}
print(trishan.info, "\n")

wagle = TourForm("Wagle", "C35A", "+977-9898989898")
wagle.check_status()
print(wagle.info, "\n")

trishan_sir = TeacherTourForm("Trishan Sir", "Computing HOD", "999")
trishan_sir.check_status()
trishan_sir.check_bill()