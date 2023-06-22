#OOPS 

import pandas as pd
import numpy as np

class refer:
    
    def __init__(self,filePath):
        codes="G:\GitClone\Project at GIT\Tuberclosis Risk\TB-Risk\Reference\State_UT_Code.csv"
        self.file=filePath
        
        df=pd.read_csv(filePath)
        df.set_index("S.No.")
        df["Code"]=[i for i in range(0,(len(df["State_UT"])))]
        
        codefile=pd.read_csv(codes)
        codes=list(codefile.code)
        sutmain=list(codefile.State_UT)

        for i in range(0,len(df["State_UT"])):
            for j in range(0,len(codefile.State_UT)):
                if str(df["State_UT"][i])[0:3] in str(codefile["State_UT"][j][:5]):
                    df["Code"][i]=codefile["code"][j]
                    break
        path=filePath
        
        df.to_csv(path_or_buf=filePath)
        print( "🟢 File Has Been Updated Successfully")
    
# refer("G:\GitClone\Project at GIT\Tuberclosis Risk\TB-Risk\HIV_Cases\HIV_Data_MOD.csv")

