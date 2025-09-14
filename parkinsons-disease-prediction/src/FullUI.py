#CREATING UI
import pandas as pd
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk,Image
import tkinter.font as font
import numpy as np
from pandas import DataFrame as df
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


window = tk.Tk()
window.title("Parkinsons Disease Prediction")
window.attributes('-fullscreen', True) 
window.configure(background='cyan')


bg = PhotoImage(file ="assets/b2.png")
label1 = Label( window, image = bg)
label1.place(x = 0, y = 0,relwidth=1,relheight=1)



message = tk.Label(window, text="Parkinsons Disease Prediction" ,bg="#B93B8F"  ,fg="white"  ,width=25  ,height=1,font=('times', 30, 'italic bold')) 

message.place(x=400, y=20)

#row1
l1 = tk.Label(window, text="MDVP:F0 (Hz)",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l1.place(x=60, y=100)

t1 = tk.Entry(window,width=10,bd=5 ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t1.place(x=280, y=100)

l2 = tk.Label(window, text="MDVP:Fhi (Hz)",width=15 ,fg="white"  ,bg="#B93B8F"    ,height=1 ,font=('times', 15, ' bold ')) 
l2.place(x=60, y=170)

t2 = tk.Entry(window,width=10,bd=5 ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t2.place(x=280, y=170)

l3 = tk.Label(window, text="MDVP:Flo (Hz)",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l3.place(x=60, y=240)

t3 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t3.place(x=280, y=240)

l4 = tk.Label(window, text="MDVP:Jitter(%)",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l4.place(x=60, y=310)

t4 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t4.place(x=280, y=310)

l5 = tk.Label(window, text="MDVP:Jitter(Abs)",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l5.place(x=60, y=380)

t5 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t5.place(x=280, y=380)

l6 = tk.Label(window, text="MDVP:RAP",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l6.place(x=60, y=450)

t6 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t6.place(x=280, y=450)

l7 = tk.Label(window, text="MDVP:PPQ",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l7.place(x=60, y=520)

t7 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t7.place(x=280, y=520)

l8 = tk.Label(window, text="Jitter:DDP",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l8.place(x=60, y=590)

t8 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t8.place(x=280, y=590)

l9 = tk.Label(window, text="MDVP:Shimmer",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l9.place(x=60, y=660)

t9 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t9.place(x=280, y=660)

l10 = tk.Label(window, text="MDVP:Shimmer(dB)",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l10.place(x=60, y=730)

t10 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t10.place(x=280, y=730)


#ROW2

l11 = tk.Label(window, text="Shimmer:APQ3",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l11.place(x=450, y=100)

t11 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t11.place(x=670, y=100)

l12 = tk.Label(window, text="Shimmer:APQ5",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l12.place(x=450, y=170)

t12 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t12.place(x=670, y=170)

l13 = tk.Label(window, text="MDVP:APQ",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l13.place(x=450, y=240)

t13 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t13.place(x=670, y=240)

l14 = tk.Label(window, text="Shimmer:DDA",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l14.place(x=450, y=310)

t14 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t14.place(x=670, y=310)

l15 = tk.Label(window, text="NHR",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l15.place(x=450, y=380)

t15 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t15.place(x=670, y=380)

l16 = tk.Label(window, text="HNR",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l16.place(x=450, y=450)

t16 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t16.place(x=670, y=450)

l17 = tk.Label(window, text="RPDE",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l17.place(x=450, y=520)

t17 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t17.place(x=670, y=520)

l18 = tk.Label(window, text="DFA",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l18.place(x=450, y=590)

t18 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t18.place(x=670, y=590)

l19 = tk.Label(window, text="spread1",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l19.place(x=450, y=660)

t19 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t19.place(x=670, y=660)

l20 = tk.Label(window, text="Spread2",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l20.place(x=450, y=730)

t20 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t20.place(x=670, y=730)


#ROW3

l21 = tk.Label(window, text="D2",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l21.place(x=840, y=100)

t21 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t21.place(x=1060, y=100)

l22 = tk.Label(window, text="PPE",width=15  ,height=1  ,fg="white"  ,bg="#B93B8F" ,font=('times', 15, ' bold ') ) 
l22.place(x=840, y=170)

t22 = tk.Entry(window,width=10,bd=5  ,bg="grey" ,fg="WHITE",font=('times', 15, ' bold '))
t22.place(x=1060, y=170)

#RESULTS

def submit():
    
    l=[]
    l.append(float(t1.get()))
    l.append(float(t2.get()))
    l.append(float(t3.get()))
    l.append(float(t4.get()))
    l.append(float(t5.get()))
    l.append(float(t6.get()))
    l.append(float(t7.get()))
    l.append(float(t8.get()))
    l.append(float(t9.get()))
    l.append(float(t10.get()))
    l.append(float(t11.get()))
    l.append(float(t12.get()))
    l.append(float(t13.get()))
    l.append(float(t14.get()))
    l.append(float(t15.get()))
    l.append(float(t16.get()))
    l.append(float(t17.get()))
    l.append(float(t18.get()))
    l.append(float(t19.get()))
    l.append(float(t20.get()))
    l.append(float(t21.get()))
    l.append(float(t22.get()))

    
    #MACHINE LEARNING MAIN CODE


    a=pd.read_csv('parkinsons.csv')
    lna=['MDVP:Fo(Hz)','MDVP:Fhi(Hz)','MDVP:Flo(Hz)','MDVP:Jitter(%)','MDVP:Jitter(Abs)','MDVP:RAP','MDVP:PPQ','Jitter:DDP','MDVP:Shimmer','MDVP:Shimmer(dB)','Shimmer:APQ3','Shimmer:APQ5','MDVP:APQ','Shimmer:DDA','NHR','HNR','RPDE','DFA','spread1','spread2','D2','PPE']
    #lit=[214.289,260.277,77.973,0.00567,0.00003,0.00295,0.00317,0.00885,0.01884,0.19,0.01026,0.01161,0.01373,0.03078,0.04398,21.209,0.462803,0.664357,-5.724056,0.190667,2.555477,0.148569]
    a=a.drop(['name'],axis=1)
    z= df([l],columns=lna)
    a=a.append(z,ignore_index = True)
    features=a.drop(['status'],axis=1)
    labels=a['status']
    scaler=MinMaxScaler((-1,1))
    x=scaler.fit_transform(features)
    y=labels
    x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=5)

    
    tt=x[-1]
    k=[]
    for i in range(22):
        k.append(tt[i])
    arr=np.array([k])

    
    #XGBOOST
    from xgboost import XGBRFClassifier
    model2=XGBRFClassifier()
    model2.fit(x_train,y_train)
    res1=model2.predict(arr)
    str=""
        
    if res1==[1]:
        str="YES"
    else:
        str="NO"

    result1.set(str)



    #SVM
    
    from sklearn import svm
    clf = svm.SVC(kernel='rbf')
    clf.fit(x_train, y_train)
    res2=clf.predict(arr)
    str2=""
        
    if res2==[1]:
        str2="YES"
    else:
        str2="NO"

    result2.set(str2)


    #EXTRATREE

    from sklearn.ensemble import ExtraTreesClassifier
    m1 = svm.SVC(kernel='rbf')
    m1.fit(x_train, y_train)
    res3=m1.predict(arr)
    str3=""
        
    if res3==[1]:
        str3="YES"
    else:
        str3="NO"

    result3.set(str3)

    

def exit():
        window.destroy()

sub=tk.Button(window,text="Submit",fg="white",bg="Green",width=5,height=1,font=("times",20,"bold"),command=submit)
sub.place(x=900,y=240)

result1=tk.StringVar()
result2=tk.StringVar()
result3=tk.StringVar()

xgbl=tk.Label(window, text="XGBoost",width=15  ,height=1  ,fg="white"  ,bg="orange" ,font=('times', 15, ' bold ') ) 
xgbl.place(x=840, y=310)

xgbr = tk.Entry(window,width=10,bd=5  ,bg="grey" , textvariable=result1 ,fg="WHITE",font=('times', 15, ' bold '))
xgbr.place(x=1060, y=310)

svml=tk.Label(window, text="SVM",width=15  ,height=1  ,fg="white"  ,bg="orange" ,font=('times', 15, ' bold ') ) 
svml.place(x=840, y=380)

svmr = tk.Entry(window,width=10,bd=5  ,bg="grey" , textvariable=result2 ,fg="WHITE",font=('times', 15, ' bold '))
svmr.place(x=1060, y=380)

extl=tk.Label(window, text="ExtraTree",width=15  ,height=1  ,fg="white"  ,bg="orange" ,font=('times', 15, ' bold ') ) 
extl.place(x=840, y=450)

extr = tk.Entry(window,width=10,bd=5  ,bg="grey" , textvariable=result3 ,fg="WHITE",font=('times', 15, ' bold '))
extr.place(x=1060, y=450)

ex=tk.Button(window,text="Exit",fg="white",bg="black",width=5,height=1,font=("times",20,"bold"),command=exit)
ex.place(x=1000,y=20)


window.mainloop()
