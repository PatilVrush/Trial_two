import numpy as np
from util_data_sim import *
expected_map = np.array([['B','C','C','AB','NC','P','P','T'],['B','C','C','AB','NC','P','P','T'],['B','C','C','AB','NC','P','P','T'],['B','C','C','AB','NC','P','P','T'],['B','C','C','AB','NC','P','P','T']]) #will take as raw_input from user in admin panel ..

#one-time-conversion required to map camera-frame-coordinates to real world.
grid = np.array([[0,100,200,300,400,500,600,700,800],[0,100,200,300,400,500]])

print('If you you want to test case where:\n')
print ('Expected map and vending map matches then enter 0\n')
print('Expected map and vending map does not match but only for P and C are exchanged then enter 1\n')
print('Expected map and vending map matches where some items have been picked then enter 2\n') 
print('Expected map and vending map does not match (position mis-match) then enter 3\n') 
print('Expected map and vending map does not match (unlisted sku appears in shelf) then enter 4\n')
user_selection=input()

items_list,items_xtopleft, items_ybottomleft = data_simulator(user_selection)


col,row = expected_map.shape

## Find unique skus from the expected map:
expected_skus = np.unique(expected_map) #Basically we want only these skus in the shelf
current_skus = np.unique(items_list)
expected_skus_l= list(expected_skus)
current_skus_l=list(current_skus)

expected_skus_l.sort()
current_skus_l.sort()

if expected_skus_l != current_skus_l:
   print('Some Anomaly, Comparing with the map') 
   sku_anomaly = 1
else:
   print('Okay we atleast have expected skus in shelf,lets check their places now\n')
   sku_anomaly = 0

current_map = np.empty((col,row),dtype = object)
for item in range(0,len(items_list)):
    for j in range(0,row): 
        for k in range(0,col):
            if (grid[0][j]< items_xtopleft[item] < grid[0][j+1]) and (grid[1][k] < items_ybottomleft[item] < grid[1][k+1]):
                current_map[(k,j)]=items_list[item]

print('Expected map is:\n')
print(expected_map)
print('\n')
print('Vending machine map is:\n')
print(current_map)

pos_anomaly = 0

for j in range(0,row):
    for k in range(0,col):
        if (current_map[k][j] != None): ### Need to add your restrictions here #basically coke and pepsi position change is accceptable but other are not
            if ((current_map[k][j] != expected_map[k][j]) and ((current_map[k][j]!='P' and current_map[k][j]!='C') or (current_map[k][j]!='C' and current_map[k][j]!='P'))):
                pos_anomaly = 1
            elif ((current_map[k][j] != expected_map[k][j]) and ((current_map[k][j]=='P' and current_map[k][j]=='C') or (current_map[k][j]=='C' and current_map[k][j]=='P'))):
                continue
        else:
            continue
      
if (pos_anomaly == 0 and sku_anomaly ==0):
   print('\nWohoo..All Good\n')
else:
   print('\nOops some anomaly... please check respective flags\n')

  


##############  Notes  ####################

# Question is what movement is allowed??? 
# What will you do in vertical stack like cuppa maggie? how to map? check 
# One more option convert map to some values based on sku numbering and compare--easier but confusing
