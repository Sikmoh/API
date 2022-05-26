# -*- coding: utf-8 -*-

# ------------------------------------------------
#    External imports
# ------------------------------------------------

# ------------------------------------------------
#    Python Imports
# ------------------------------------------------

# ------------------------------------------------
#    Module Imports
# ------------------------------------------------
from basehandler import api_response
from auth.core import permission
# ------------------------------------------------
#    facts Data Access layer
# ------------------------------------------------
from cats.data_access import *

from errors.v1.handlers import ApiError


#

# ------------------------------------------------
#          FACT REST FUNCTIONS START HERE
# ------------------------------------------------
def get_fact(**kwargs):
    """
        Fetch a fact
    :return: Fact Entity
    :errors:
        raises an APIError
    """
    permission(kwargs['token_info'], access_role='basic')
    fact = FactDacc.fact(kwargs)
    return api_response({'result': fact})


def get_fact_id(fact_id, **kwargs):
    """
        Fetch a fact
    :return: Fact Entity
    :errors:
        raises an APIError
    """
    # permission(kwargs['token_info'], access_role='basic')
    fact = FactDacc.factid(fact_id, kwargs)
    return api_response(fact)


def get_facts(**kwargs: dict) -> dict:
    """
        Fetch all the facts via pagination. If there is a cursor then fetch the next batch of facts
    :param kwargs: dictionary object containing keyword arguments
    :return: List of fact Entities and total fact count
    :errors:
    """
    # import pdb;
    # pdb.set_trace()
    # permission(kwargs['token_info'], access_role='basic')
    facts = FactDacc.facts(kwargs)
    return api_response({'results': facts})
    # if facts:
    #     return api_response(
    #         facts)
    # else:
    #     raise ApiError('facts-not-found', status_code=404)
