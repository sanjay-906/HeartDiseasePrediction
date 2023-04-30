# Write your code here :-)
import numpy as np
import pickle
import sklearn
import streamlit as sl



pickle_1=open("D:/New folder/model_lr.sav","rb")
model1=pickle.load(pickle_1)

pickle_2=open("D:/New folder/model_svc.sav","rb")
model2=pickle.load(pickle_2)

pickle_3=open("D:/New folder/model_xgb.sav","rb")
model3=pickle.load(pickle_3)

def compute(input_values):

    pred_array=np.asarray(input_values).reshape(1,-1)
    predictions=model3.predict(pred_array)
    if(predictions[0]==1):
        return "Presence of Heart Disease "
    else:
        return "Absence of Heart Disease"



def main():

    sl.title('Heart Disease Prediction')
    Age = sl.number_input("Age: ",min_value=1, max_value=100, value=1, step=1)
    Sex_dropdown = sl.selectbox('Sex:',('Male','Female'))
    if Sex_dropdown =='Male':
        Sex =0
    if Sex_dropdown == 'Female':
        Sex =1
    #--------------------------------------------------------------------------
    ChestPainT= sl.selectbox('ChestPainType:',('ASY','ATA','NAP','TA'))
    if ChestPainT =='ASY':
        ChestPainType = 1
    if ChestPainT == 'ATA':
        ChestPainType = 2
    if ChestPainT == 'NAP':
        ChestPainType = 3
    if ChestPainT == 'TA':
        ChestPainType = 4
    #--------------------------------------------------------------------------
    RestingBP = sl.number_input("RestingBP: ",min_value=80, max_value=200, value=80, step=1)
    Cholestrol = sl.number_input("Cholestrol: ",min_value=0, max_value=800, value=0, step=1)

    FBS= sl.selectbox('FastingBS:',('0','1'))
    if FBS =='0':
        FastingBS =0
    if FBS =='1':
        FastingBS =1

    #---------------------------------------------------------------------------
    RECG=sl.selectbox('RestingECG:',('Normal','ST','LVH'))
    if RECG =='Normal':
        RestingECG = 1
    if RECG == 'ST':
        RestingECG = 2
    if RECG == 'LVH':
        RestingECG = 3
    #--------------------------------------------------------------------------
    MaxHR = sl.number_input("MaxHR: ",min_value=60, max_value=200, value=60, step=1)
    #--------------------------------------------------------------------------
    EA= sl.selectbox('ExerciseAngina:',('Yes','No'))
    if EA =='No':
        ExerciseAngina =0
    if EA =='Yes':
        ExerciseAngina =1
    #--------------------------------------------------------------------------
    Oldpeak = sl.number_input("Oldpeak: ")


    ST=sl.selectbox('ST_Slope:',('Flat','Up','Down'))
    if ST =='Flat':
        ST_Slope = 1
    if ST == 'Up':
        ST_Slope = 2
    if ST == 'Down':
        ST_Slope = 3
    #--------------------------------------------------------------------------







    patient=''
    if sl.button("Evaluate"):
        patient= compute([Sex, ChestPainType,FastingBS,RestingECG,ExerciseAngina,ST_Slope, Age,
        RestingBP, Cholestrol, MaxHR , Oldpeak ])

    sl.success(patient)



if __name__ == '__main__':
    main()
