import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
COMPLETION_MODEL_NAME = "gpt-3.5-turbo-instruct"

# Database Configuration
DATABASE_PATH = "chroma/"

# Templates
TEMPLATE_GENERATE_FEATURES = """
You are a piece of software that is helping a Housing Chatbot that
is supporting users in New York City.

Your job is to take a query from an user and generate a list of what the user 
requires in the house or neighborhood, call that list user's requirements. 

Here is a housing query asked by the customer, it is delimited by triple backticks:
```{query_user}```

Please be accurate, don't assume anything that wasn't mentioned by the user.
"""

TEMPLATE_COMPARISON = """
You are a piece of software that is helping a Real State Chatbot that
is supporting users in New York City.

Your job is to take a look at two things: 
1. A list of user's requirements
2. A house description found in the database

You need to traverse the user's requirements list and assign every 
item to one of the following groups:

1. The similarities list, if the item is present in the house description
found in the database.
2. The not similarities list otherwise.

There is no need to invent new items for the user's requirements list, just assign every 
item to one of the output lists.
If all requirement items get assigned to one of the output lists, then add None to the empty list, 
do not use "House" as a default value for an empty list.

The criteria for assigning items to the lists depends on whether the item has a  
categorical or numerical variables:

- For categorical variables you have to be very specific. For instance, if the house is 
located one boroughs like Manhattan and the user requires it to be in The Bronx then that item 
should go to the not similarities list, boroughs should equally match in order to go to the similarities list.
If user requires the house to be in a safe neighborhood and there is no mention of that in the description, 
then that item should go to the not similarities list.

- For numerical values we have two cases:
    - If the price that the user can pay is equal or lower than the one found in the description, 
    then that item should go to the similarities list, if it's higher it has to go to the not
    similarities list.

    - For variables like the number of bathrooms, bedrooms, or size of the house, it is ok to put in 
    the similarities list if the value found in the database is equal or higher than the user requires it
    If the value found in the database is smaller, then it should go to the not similarities list.

Here is the list of user's requirements, it is delimited by triple backticks:
```{user_list_requirements}```

And here is the output found in the database, it is delimited by triple backticks:
```{output_database}```
""" 