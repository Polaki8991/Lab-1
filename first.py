import matplotlib.pyplot as plt

#Ploting sample 4
position=[0, 20, 40, 60, 80, 100] #x-axis list for Load in percentage
y1=[0.11,0.07,0.04,0.03,0.03,0.03] #y-axis list for CO in g/Km(Vol)
y2=[1.5,1.7,2,2.4,2.6,3.4]	#y-axis list for CO2 in g/Km(Vol)
y3=[18.69,18.42,18.05,17.36,17.13,16.04]	#y-axis for O2 in g/Km(Vol)
#Ploting 3 graphs in the same plot
plt.plot(position,y1,color='r',label='CO')
plt.plot(position,y2,color='g',label='CO2')
plt.plot(position,y3,color='b',label='O2')
plt.title("Sample 4 plot for CO, O2, CO2")
plt.xlabel('LOAD%') #Naming x-axis
plt.ylabel('Vol g/Km') #Naming y-axis
plt.legend() #dispalying the lables of graphs
plt.show() #displayin the plot



