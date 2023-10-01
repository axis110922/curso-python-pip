def getPopulation(countryDict):
  populationDict={
    '2022':int(countryDict['2022 Population']),
    '2020':int(countryDict['2020 Population']),
    '2015':int(countryDict['2015 Population']),
    '2010':int(countryDict['2010 Population']),
    '2000':int(countryDict['2000 Population']),
    '1990':int(countryDict['1990 Population']),
    '1980':int(countryDict['1980 Population']),
    '1970':int(countryDict['1970 Population'])
  }
  #keys=['col','bol']
  #values=[300,400]
  labels=populationDict.keys()
  values=populationDict.values()
  return labels,values

A='Hola'

def populationByCountry(data,country):
  result=list(filter(lambda item:item['Country/Territory']==country, data))
  return result

