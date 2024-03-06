import numpy as np
import pandas as pd
String_series=pd.Series(["Deva",21,"Vinod",24,"Nikhila",16,"Sunthosh",14,"Pramod",17,"Vihitha",19],name="Details")
print(String_series)
Newcount=String_series.count()
print("The count is:",Newcount)
#Add of two lists
Newlist1=pd.Series([10,20,30,"Chandu",60,66],index=[1,3,5,7,9,6])
Newlist2=pd.Series([20,30,40,50,60,80],index=[1,3,5,6,8,0])
Deva=Newlist1+Newlist2
print("The newlist is:\n",Deva )
new=Deva.count()
print("The count is:\n",new)
