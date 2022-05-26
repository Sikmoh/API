# -*- coding: utf-8 -*-

# -------------------------------------------------
#  External Imports
# -------------------------------------------------
import connexion

# -------------------------------------------------
#  Python Imports
# -------------------------------------------------


# -------------------------------------------------
#  Module Imports
# -------------------------------------------------
from errors.v1 import handlers as error_handlers

# -------------------------------------------------
#  Setup
# -------------------------------------------------
# Setup the connexion app - for swagger self documenting API routes
app = connexion.FlaskApp(__name__)
app.add_api('openapi.yaml',
            strict_validation=True,
            arguments={'title': 'Sikirus Random facts Project'})
app.app.register_blueprint(error_handlers.error_handlers)


# -------------------------------------------------
#  Kick off
# -------------------------------------------------

def startup():
    """
       Method to fire any startup config stuff up
   :return:
   """
    pass


if __name__ == '__main__':
    startup()
    app.run(host="127.0.0.1", port=5003)
