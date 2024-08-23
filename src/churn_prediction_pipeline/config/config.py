import pathlib
import os
import churn_prediction_pipeline

PACKAGE_ROOT = pathlib.Path(churn_prediction_pipeline.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT,"datasets")

MODEL_NAME = 'churn_model.pickle'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,'trained_model')

schema = {
    'columns': ['customerID', 'tenure', 'PhoneService', 'Contract', 'TotalCharges']
}

result_columns = ['TotalCharges','Month-to-month','One year','Two year','PhoneService','tenure']
output_columns = ['customerID', 'tenure', 'PhoneService', 'Contract', 'TotalCharges','prediction']

pre_processing_columns = ['customerID','TotalCharges','Contract','PhoneService','tenure']


headers = 'customerID,tenure,PhoneService,Contract,TotalCharges,prediction'