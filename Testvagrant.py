class PlanetryData:
    def __init__(self,name,surface,moon,rings):
        self.name = name
        self.surface = surface
        self.moon = moon
        self.rings = rings
    def count_of_moons(self,list_items):
        count = 0
        self.list_items = list_items
        new_list = []
        for k,v in list_items.items():
            if v == "Yes":
                new_list.append(k)
        return("Count of moons of all planets having rings is: " + str(sum(new_list)))
    def gas_found(self,new_gases):
        self.new_gases = new_gases
        new_gas = []
        for k,v in new_gases.items():
            new_gas.append(v)
        res = max(new_gas)
        
        for k,v in new_gases.items():
            if v == res:
                return("Gas that is found on maximum planets is: " + k)
      
planetry_obj = PlanetryData("Moon","Carbon Dioxide",0,"No")
print(planetry_obj.name)
print(planetry_obj.surface)
print(planetry_obj.moon)
print(planetry_obj.rings)
print(planetry_obj.count_of_moons({0:"No",
    0:"No",
    1:"No",
    79:"Yes",
    83:"Yes",
    27 : "Yes"
}))

print(planetry_obj.gas_found({
    "jupitor" : 79,
    "saturn" : 83,
    "uranus" : 27
})
)


