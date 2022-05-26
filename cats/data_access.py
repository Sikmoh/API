# -*- coding: utf-8 -*-

# ------------------------------------------------
#    Python Imports
# ------------------------------------------------

# ------------------------------------------------
#    External Imports
# ------------------------------------------------

# ------------------------------------------------
#     Module Imports
# ------------------------------------------------
from catfacts import Facts


# ------------------------------------------------
#     Abstract fact Data Access Layer
# ------------------------------------------------

class FactDacc(object):
    """
        Abstract Fact Data Access Class
    """

    @staticmethod
    def fact(kwargs: dict):
        """
             Retrieve a random Fact
        :param kwargs:
        :return: The fact data
        """

        random = Facts()
        # Build and request the URL by adding the animal_type and amount
        random.request_data_sync('/facts/random', kwargs['animal_type'], kwargs['amount'])
        return random.facts_data

    @staticmethod
    def factid(fact_id, kwargs):
        """
             Retrieve a random Fact
        :param kwargs:
        :param fact_id:

        :return: The fact data
        """
        random = Facts()
        # Build and request the URL by adding the category and subcategory
        random.request_data_sync('/facts/' + fact_id, kwargs['animal_type'])
        return random.facts_data

    @staticmethod
    def facts(kwargs: dict):
        """
             Retrieve StarWars Films


        :return: The facts data
        """
        # import pdb;
        # pdb.set_trace()
        random = Facts()
        random.request_data_async('/facts/random', kwargs['animal_type'], kwargs['amount'])
        return random.facts_data, len(random.facts_data)
