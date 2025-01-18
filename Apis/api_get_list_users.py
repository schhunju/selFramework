from Apis.baseAPI import BaseAPI


class APIGetListUsers(BaseAPI):

    def __init__(self, end_point=None):
        super().__init__(end_point)

    # if this function is not created, then we need to pass endpoint directly while calling this class
    # e.g: self.abc=APIGetListUsers('/endpoint/abcd/')
    def set_end_point(self, end_point):
        self.end_point = end_point

    def get_list_users(self, url):
        return self.api_http_methods.get(url, self.end_point)