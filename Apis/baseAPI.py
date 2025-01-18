from Utilities.rest_utils.api_http_methods import ApiHttpMethods


class BaseAPI:
    def __init__(self, end_point):
        self.api_http_methods = ApiHttpMethods()
        self.end_point = f'{end_point}'