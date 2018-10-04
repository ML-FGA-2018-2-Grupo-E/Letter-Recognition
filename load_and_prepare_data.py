from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

def load_and_prepare_data(file_path=None):
    data = 'data_set/letter-recognition.data'
    if(file_path):
        data = file_path
    else:
        pass
    columns = ['lettr','x-box','y-box','width','high','onpix','x-bar','y-bar','x2bar','y2bar','xybar','x2ybr','xy2br','x-ege','xegvy','y-ege','yegvx']
    df = pd.read_csv(data, names = columns)
    df.shape

    #Enumera letras de 0(A) até 25(Z)
    df_num = df.iloc[:, :16].values
    labelencoder_df = LabelEncoder()
    df_num[:, 0] = labelencoder_df.fit_transform(df_num[:, 0])

    train=df_num[:16000, :]
    test=df_num[16000:, :]

    y_train = train[:, 0]
    x_train = train[:, 1:]
    
    y_test = test[:, 0]
    x_test = test[:, 1:]
    
    return y_train, x_train, y_test, x_test