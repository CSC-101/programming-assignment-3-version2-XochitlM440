import data

#part 1
def population_total(m:list[data.CountyDemographics])-> int:
    total = 0
    for i in range(len(m)):
        if "2014 Population" in m[i].population:
            total += m[i].population["2014 Population"]
    return total


#part 2
def filter_by_state(m:list[data.CountyDemographics], s:str)-> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(m)):
        if m[i].state == s:
            new_list.append(m[i])
    return new_list
    #return len(new_list)   --> what I used for the tests


#part 3
def population_by_education(m:list[data.CountyDemographics], edu_level:str) -> float:
    total = 0
    for i in range(len(m)):
        if edu_level in m[i].education:
            percentage = m[i].education[edu_level]
            people = population_total(m)
            x = (people*percentage)/100
            total += x
    return total

def population_by_ethnicity(m:list[data.CountyDemographics], ethnicity:str) -> float:
    total = 0
    for i in range(len(m)):
        if ethnicity in m[i].ethnicities:
            percentage = m[i].ethnicities[ethnicity]
            people = population_total(m)
            x = (people*percentage)/100
            total += x
    return total

def population_below_poverty_line(m:list[data.CountyDemographics]) ->float:
    total = 0
    for i in range(len(m)):
        if "Persons Below Poverty Level" in m[i].income:
            percentage = m[i].income["Persons Below Poverty Level"]
            people = population_total(m)
            x = (people*percentage)/100
            total += x
    return total


#part 4
def percent_by_education(m:list[data.CountyDemographics], education:str) -> float:
    total = population_total(m)
    certain_edu = population_by_education(m, education)
    percent = (certain_edu/total)*100
    return percent

def percent_by_ethnicity (m:list[data.CountyDemographics], ethnicity:str) -> float:
    total = population_total(m)
    certain_ethnicity = population_by_ethnicity(m, ethnicity)
    percent = (certain_ethnicity/total)*100
    return percent

def percent_below_poverty_level(m:list[data.CountyDemographics]) -> float:
    total = population_total(m)
    number = population_below_poverty_line(m)
    percent = (number/total)*100
    return percent


#part 5
def education_greater_than(m:list[data.CountyDemographics], education:str, amount:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(m)):
        if education in m[i].education and m[i].education[education] > amount:
            new_list.append(m[i])
    return new_list

def education_less_than(m:list[data.CountyDemographics], education:str, amount:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(m)):
        if education in m[i].education and m[i].education[education] < amount:
            new_list.append(m[i])
    return new_list

def ethnicity_greater_than(m:list[data.CountyDemographics], ethnicity:str, amount:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(m)):
        if ethnicity in m[i].ethnicities and m[i].ethnicities[ethnicity] > amount:
            new_list.append(m[i])
    return new_list

def ethnicity_less_than(m:list[data.CountyDemographics], ethnicity:str, amount:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(m)):
        if ethnicity in m[i].ethnicities and m[i].ethnicities[ethnicity] < amount:
            new_list.append(m[i])
    return new_list

def below_poverty_level_greater_than(m:list[data.CountyDemographics], amount:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(m)):
        if "Persons Below Poverty Level" in m[i].income and m[i].income["Persons Below Poverty Level"] > amount:
            new_list.append(m[i])
    return new_list

def below_poverty_level_less_than(m:list[data.CountyDemographics], amount:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(m)):
        if "Persons Below Poverty Level" in m[i].income and m[i].income["Persons Below Poverty Level"] < amount:
            new_list.append(m[i])
    return new_list