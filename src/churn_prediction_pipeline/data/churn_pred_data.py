from typing import Optional
from enum import Enum
from pydantic import BaseModel

# Define the Enums
class ContractEnum(str, Enum):
    month_to_month = 'Month-to-month'
    one_year = 'One year'
    two_year = 'Two year'

class PhoneServiceEnum(str, Enum):
    yes = 'Yes'
    no = 'No'

# Define the Pydantic BaseModel
class churn_pred_data(BaseModel):
    customerID: str
    TotalCharges: Optional[float] = None
    Contract: ContractEnum
    PhoneService: Optional[PhoneServiceEnum]= None
    tenure: Optional[int] = None

# Function to convert Pydantic model to dictionary
def pydantic_to_dict(model: churn_pred_data) -> dict:
    return model.dict()

# Function to convert dictionary back to Pydantic model
def dict_to_pydantic(data: dict) -> churn_pred_data:
    return churn_pred_data(**data)


# # Convert Pydantic model to dictionary
# churn_pred_dict = pydantic_to_dict(pydantic_churn_pred)
# print("Dictionary:", churn_pred_dict)

# # Convert dictionary back to Pydantic model
# new_pydantic_churn_pred = dict_to_pydantic(churn_pred_dict)
# print("Pydantic Model:", new_pydantic_churn_pred)