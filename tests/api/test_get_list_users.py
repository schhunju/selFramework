from Apis.api_get_list_users import APIGetListUsers
from Pages.Basepage import BasePage


class TestGetListUsers(BasePage):

    def test_get_list_users(self, api_url):
        self.api_get_list_users = APIGetListUsers()
        self.api_get_list_users.set_end_point(f'api/users?page=2')
        response = self.api_get_list_users.get_list_users(api_url)
        print(response.json())
        assert response.status_code == 200