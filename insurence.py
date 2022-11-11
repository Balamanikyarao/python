class vehicle:
    def _init_(self):
        self.__vehicleid=None
        self.__vehicletype=None
        self.__vehiclecost=None
        self.__vehiclepremium=None
    def setvehicleid(self,vid):
        self.__vehicleid=vid
    def setvehicletype(self,typ):
        self.__vehicletype=type
    def setvehiclecost(self,cost):
        self.__vehiclecost=cost
    def setvehiclepremium(self):
        if(self.__vehicletype=="two wheeler"):
            self._vehiclepremium=self._vehiclecost*2/100
            print("premium for two wheeler",self.__vehiclepremium)
        elif(self.__vehicletype=="four wheeler"):
            self._vehiclepremium=self._vehiclecost*6/100
            print("premium for four wheeler",self.__vehiclepremium)
        else:
            print("u enterd invalid vehicle")
    def getvehicleid(self):
        return self.__vehicleid
    def getvehicletype(self):
        return self.__vehicletype
    def getvehiclecost(self):
        return self.__vehiclecost
wecare=vehicle()
vid=input("enter vehicle id")
wecare.setvehicleid(vid)
type=input("enter type")
wecare.setvehicletype(type)
cost=int(input("enter cost"))
wecare.setvehiclecost(cost)
print("vehicle id",wecare.getvehicleid())
print("vehicle type",wecare.getvehicletype())
print("vehicle cost",wecare.getvehiclecost())

wecare.setvehiclepremium()
