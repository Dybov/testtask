from flask import Blueprint


bp = Blueprint(
     'datapoint',
     __name__,
     url_prefix='/datapoint',
     template_folder='templates',
     static_folder='static',
)

# Dict with ID ranges: 
# 1st source: ID 1-10,31-40;
# 2nd source: ID 11-20,41-50;
# 3d source: ID 21-30,51-60;
datarange = {
    1: (1, 10, 31, 40),
    2: (11, 20, 41, 50),
    3: (21, 30, 51, 60),
}

import datapoint.views
