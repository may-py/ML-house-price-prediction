import sys, os
import pandas as pd
from src.logger import logger
from src.utils import load_object



class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join('artifacts','model.pkl')
            preprocessor_path = os.path.join('artifacts','proprocessor.pkl')
            print('Before loading')
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print('After loading')
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
            
        except Exception as e:
            raise e
        

class CustomData:
# 'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'
    def __init__(self,    
        CRIM   :    float,
        ZN     :    float,
        INDUS  :    float,
        CHAS   :    int  ,
        NOX    :    float,
        RM     :    float,
        AGE    :    float,
        DIS    :    float,
        RAD    :    int  ,
        TAX    :    int  ,
        PTRATIO:    float,
        B      :    float,
        LSTAT  :    float,
        ):

        self.CRIM   = CRIM
        self.ZN     = ZN
        self.INDUS  = INDUS
        self.CHAS   = CHAS
        self.NOX    = NOX
        self.RM     = RM
        self.AGE    = AGE
        self.DIS    = DIS
        self.RAD    = RAD
        self.TAX    = TAX
        self.PTRATIO= PTRATIO
        self.B      = B
        self.LSTAT  = LSTAT
        
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                'CRIM':[self.CRIM],
                'ZN':[self.ZN],
                'INDUS':[self.INDUS],
                'CHAS':[self.CHAS],
                'NOX':[self.NOX],
                'RM':[self.RM],
                'AGE':[self.AGE],
                'DIS':[self.DIS],
                'RAD':[self.RAD],
                'TAX':[self.TAX],
                'PTRATIO':[self.PTRATIO],
                'B':[self.B],
                'LSTAT':[self.LSTAT],
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise e

