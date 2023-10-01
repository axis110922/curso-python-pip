import matplotlib.pyplot as plt

def generateBarChart(name,labels,values):
  #labels=['a','b','c']
  #values=[100,200,300]
  fig,ax=plt.subplots()
  ax.bar(labels,values)
  plt.savefig(f'./imgs/{name}.png')
  plt.show()

def generatePieChart (labels,values):
  fig,ax=plt.subplots()
  ax.pie(values,labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.show()

if __name__ =='__main__':
  labels=['a','b','c']
  values=[10,20,5]
  #generateBarChart(labels,values)
  generatePieChart(labels,values)
