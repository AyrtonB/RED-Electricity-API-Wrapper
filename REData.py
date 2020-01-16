"""
Imports
"""
import pandas as pd
import numpy as np

import requests
import inspect
import operator
import itertools
from functools import reduce

from API_structure import *


"""
Wrapper
""" 
class REData:
    ## Calling the API  
    def check_errs(self, r_json):
        if 'errors' in r_json.keys():
            for err in r_json['errors']:
                err_title = err['title']
                err_detail = err['detail']

                raise ValueError(f'{err_title}\n{err_detail}\n')
                
    def make_request(self, start_date, end_date, time_trunc, geo_trunc=None, geo_limit=None, geo_ids=None):
        *_, params = inspect.getargvalues(inspect.currentframe())
        r = requests.get(self.url, params=params)

        return r
    
    
    ## JSON Parsing
    col_2_s = staticmethod(lambda col: pd.DataFrame(col['attributes']['values']).set_index('datetime')['value'])
    
    def get_from_dict(self, data_dict, map_list):
        return reduce(operator.getitem, map_list, data_dict)

    def json_2_nested_lists(self, obj_in, route):
        if len(route) == 0:
            yield obj_in

        elif isinstance(obj_in, list):
            for item in obj_in:
                obj_out = self.json_2_nested_lists(item, route)
                yield from obj_out

        else:
            obj_out = self.get_from_dict(obj_in, route[0])
            yield from self.json_2_nested_lists(obj_out, route[1:])

    def json_2_df(self, r_json):
        nested_lists = self.json_2_nested_lists(r_json, self.JSON_route)
        cols_flatlist = list(itertools.chain(*nested_lists))

        df = pd.DataFrame()

        for col in cols_flatlist:
            s_data = self.col_2_s(col)
            s_data.name = col['type']

            df[s_data.name] = s_data

        df.index = pd.to_datetime(df.index)

        return df
            
    
    ## User Functions
    def update_stream(self, category, widget):
        assert (category, widget) in list(JSON_routes.keys()), f'The widget \'{widget}\' is not allowed for category \'{category}\''

        self.JSON_route = JSON_routes[(category, widget)]
        self.url = f'https://apidatos.ree.es/en/datos/{category}/{widget}'
      
    def query_REData(self, *args, **kwargs):
        r = self.make_request(*args, **kwargs)
        
        r_json = r.json()
        self.check_errs(r_json)
        
        df = self.json_2_df(r_json)
        
        return df
    
    
    ## Initialisation
    def __init__(self, category, widget):
        self.update_stream(category, widget)
        self.JSON_route = JSON_routes[(category, widget)]
        
    
