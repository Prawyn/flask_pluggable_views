import os

from flask import Flask

from views import UserView

#App Config
app= Flask(__name__)

# ********************** NOT WORKING ****************************
# from error_handlers import auth_error
# from error_handlers import *
# ***************************************************************

#URLs
app.add_url_rule('/users', view_func=UserView.as_view('user_view'), methods=['GET'])

# ********************** NOT WORKING ****************************
# from error_handlers import auth_error
# ***************************************************************

# ********************** WORKING ****************************
from error_handlers import *
# ***************************************************************

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port=5050)

