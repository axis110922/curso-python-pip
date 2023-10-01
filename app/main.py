import utils
import readCsv
import charts

def run():  
  data=readCsv.readCsv('data.csv')
  country=input('Type Country => ')
  result=utils.populationByCountry(data,country)

  if len(result)>0:
    country=result[0]
    labels,values=utils.getPopulation(country)
    charts.generateBarChart(country,labels,values)
    #print(keys,values)
    #print(utils.A)
  
''' data=[
    {'Country':'Colombia','Population':500},
    {'Country':'Bolivia','Population':300}
  ]'''

# country=input('Type Country => ')
  
 # print(result)

if __name__=='__main__':
  run()