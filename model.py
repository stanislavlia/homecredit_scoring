import numpy as np
import pydantic
import catboost

"""Expected data for model

Data columns (total 69 columns):
 #   Column                          Non-Null Count  Dtype  
---  ------                          --------------  -----  
 0   SK_ID_CURR              
 1   NAME_CONTRACT_TYPE              48744 non-null  int64  
 2   CODE_GENDER                     48744 non-null  int64  
 3   FLAG_OWN_CAR                    48744 non-null  int64  
 4   AMT_INCOME_TOTAL                48744 non-null  float64
 5   AMT_CREDIT                      48744 non-null  float64
 6   AMT_ANNUITY                     48744 non-null  float64
 7   AMT_GOODS_PRICE                 48744 non-null  float64
 8   NAME_INCOME_TYPE                48744 non-null  int64  
 9   NAME_FAMILY_STATUS              48744 non-null  int64  
 10  REGION_POPULATION_RELATIVE      48744 non-null  float64
 11  DAYS_BIRTH                      48744 non-null  int64  
 12  DAYS_EMPLOYED                   48744 non-null  int64  
 13  DAYS_REGISTRATION               48744 non-null  float64
 14  DAYS_ID_PUBLISH                 48744 non-null  int64  
 15  OWN_CAR_AGE                     48744 non-null  float64
 16  FLAG_WORK_PHONE                 48744 non-null  int64  
 17  FLAG_PHONE                      48744 non-null  int64  
 18  OCCUPATION_TYPE                 48744 non-null  int64  
 19  REGION_RATING_CLIENT_W_CITY     48744 non-null  int64  
 20  WEEKDAY_APPR_PROCESS_START      48744 non-null  int64  
 21  REG_CITY_NOT_LIVE_CITY          48744 non-null  int64  
 22  ORGANIZATION_TYPE               48744 non-null  int64  
 23  EXT_SOURCE_1                    48744 non-null  float64
 24  EXT_SOURCE_2                    48744 non-null  float64
 25  EXT_SOURCE_3                    48744 non-null  float64
 26  DEF_30_CNT_SOCIAL_CIRCLE        48744 non-null  float64
 27  DAYS_LAST_PHONE_CHANGE          48744 non-null  float64
 28  FLAG_DOCUMENT_3                 48744 non-null  int64  
 29  AMT_REQ_CREDIT_BUREAU_QRT       48744 non-null  float64
 30  CREDIT_ACTIVE_mode              48744 non-null  int64  
 31  avg_DAYS_CREDIT                 48744 non-null  float64
 32  avg_DAYS_CREDIT_ENDDATE         48744 non-null  float64
 33  avg_AMT_CREDIT_MAX_OVERDUE      48744 non-null  float64
 34  avg_AMT_CREDIT_SUM              48744 non-null  float64
 35  avg_meanMONTHS_BALANCE          48744 non-null  float64
 36  prev_AMT_ANNUITY                48744 non-null  float64
 37  prev_AMT_DOWN_PAYMENT           48744 non-null  float64
 38  prev_AMT_GOODS_PRICE            48744 non-null  float64
 39  prev_NAME_CONTRACT_STATUS       48744 non-null  int64  
 40  prev_DAYS_DECISION              48744 non-null  float64
 41  prev_NAME_CLIENT_TYPE           48744 non-null  int64  
 42  prev_SELLERPLACE_AREA           48744 non-null  float64
 43  prev_CNT_PAYMENT                48744 non-null  float64
 44  prev_NAME_YIELD_GROUP           48744 non-null  int64  
 45  prev_DAYS_FIRST_DUE             48744 non-null  float64
 46  prev_DAYS_TERMINATION           48744 non-null  float64
 47  prev_NFLAG_INSURED_ON_APPROVAL  48744 non-null  float64
 48  prev_avg_cntinstallment         48744 non-null  float64
 49  prev_avg_cntinstallment_future  48744 non-null  float64
 50  prev_amtcredlimit_avg           48744 non-null  float64
 51  prev_amtpaymentcurr_avg         48744 non-null  float64
 52  prev_amtrecivable_avg           48744 non-null  float64
 53  prev_cntdrawingsatmcurr_avg     48744 non-null  float64
 54  prev_cntdrawingscurr_avg        48744 non-null  float64
 55  LOG_AMT_INCOME                  48744 non-null  float64
 56  LOG_AMT_CREDIT                  48744 non-null  float64
 57  GEOM_AVG_EXT_SOURCES12          48744 non-null  float64
 58  AMT_INCOME_PER_CREDIT           48744 non-null  float64
 59  DAYS_EMPLOYED_PER_CREDIT        48744 non-null  float64
 60  EXT_SOURCE_1_prod_AMT_CREDIT    48744 non-null  float64
 61  EXT_SOURCE_2_prod_AMT_CREDIT    48744 non-null  float64
 62  EXT_SOURCE_3_prod_AMT_CREDIT    48744 non-null  float64
 63  AGE_VS_JOB_EXPERIENCE           48744 non-null  float64
 64  CURR_CONSUMPTION_RATE           48744 non-null  float64
 65  CONSUMPTION_RATIO               48744 non-null  float64
 66  WORKING_TIME_FRACTION           48744 non-null  float64
 67  EDUCATION_TYPE_ORD              48744 non-null  int64  
 68  EDUCATION_TYPE_ORD_EXP          48744 non-null  float64
"""

def compute_hand_crafted_feats(df):
    pass

def compute_golden_feats(df):
    pass




def preprocess_df():
    pass