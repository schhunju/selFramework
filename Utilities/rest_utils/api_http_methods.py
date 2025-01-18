import requests
from requests import Response
from requests.auth import HTTPBasicAuth



class ApiHttpMethods:
    @staticmethod
    def post(base_url, endpoint, data, headers=None):
        """
        This function sends a POST request to a specified endpoint with provided data and headers, and logs
        the request and response.

        :param base_url: The base URL of the API endpoint that the request will be sent to
        :param endpoint: The specific endpoint of the API that we want to send a POST request to. It is a
        string that is appended to the base URL to form the complete URL for the API endpoint
        :param data: The data parameter is the payload to be sent in the request body. It can be a
        dictionary, list of tuples, bytes, or file-like object
        :param headers: The headers parameter is an optional dictionary that contains HTTP headers to be
        sent with the request. These headers provide additional information about the request, such as the
        content type of the data being sent or authentication credentials. If no headers are provided, the
        request will be sent with default headers
        :return: a response object from the `requests.post()` method.
        """
        url = f"{base_url}/{endpoint}"
        return requests.post(url, data=data, headers=headers)

    @staticmethod
    def post_basic_auth(base_url, endpoint, data, username, password, headers=None):
        """
        The function `post_basic_auth` sends a POST request to a specified endpoint with basic
        authentication using a username and password.

        :param base_url: The base URL is the main URL of the API or website you are making the request to.
        It is the starting point for constructing the complete URL for the request
        :param endpoint: The `endpoint` parameter is a string that represents the specific endpoint or route
        of the API that you want to send a POST request to. It is appended to the `base_url` to form the
        complete URL for the request
        :param data: The `data` parameter is the payload or body of the HTTP request. It contains the data
        that you want to send to the server. It can be in various formats such as JSON, XML, or form data
        :param username: The `username` parameter is the username used for basic authentication. It is
        typically a string that represents the username of the user making the request
        :param password: The `password` parameter is the password used for basic authentication. It is used
        to authenticate the user along with the `username` parameter
        :param headers: The `headers` parameter is an optional argument that allows you to pass additional
        headers to the HTTP request. Headers are used to provide additional information about the request,
        such as the content type or authentication credentials. If you don't need to pass any additional
        headers, you can omit this parameter or pass `
        :return: the response object from the POST request made using the requests library.
        """
        url = f"{base_url}/{endpoint}"
        return requests.post(url, data=data, headers=headers, auth=HTTPBasicAuth(username, password))

    @staticmethod
    def post_for_files(base_url, endpoint, files, headers=None) -> Response:
        """
        This function sends a POST request to a specified endpoint with provided data and headers, and logs
        the request and response.

        :param base_url: The base URL of the API endpoint that the request will be sent to
        :param endpoint: The specific endpoint of the API that we want to send a POST request to. It is a
        string that is appended to the base URL to form the complete URL for the API endpoint
        :param files: The data parameter is the payload to be sent in the request body. It can be a
        dictionary, list of tuples, bytes, or file-like object
        :param headers: The headers parameter is an optional dictionary that contains HTTP headers to be
        sent with the request. These headers provide additional information about the request, such as the
        content type of the data being sent or authentication credentials. If no headers are provided, the
        request will be sent with default headers
        :return: a response object from the `requests.post()` method.
        """
        url = f"{base_url}/{endpoint}"
        return requests.post(url, files=files, headers=headers)

    @staticmethod
    def post_for_graphql(base_url, endpoint, data, headers=None):
        """
        This function sends a POST request to a GraphQL endpoint with specified data and headers, and logs
        the request and response.

        :param base_url: The base URL of the API endpoint that the request will be sent to
        :param endpoint: The endpoint parameter is a string that represents the specific API endpoint that
        the request is being sent to. It is typically a URL path that comes after the base URL
        :param data: The data parameter is a JSON object that contains the data to be sent in the request
        body. It will be serialized to JSON format and sent as the request payload
        :param headers: The headers parameter is a dictionary containing the HTTP headers to be sent with
        the request. These headers typically include information such as the content type of the request,
        authentication tokens, and user agent information. If no headers are required, the parameter can be
        set to None
        :return: The function `post_for_graphql` returns a response object obtained from sending a POST
        request to a specified endpoint with the provided data and headers.
        """
        url = f"{base_url}/{endpoint}"
        return requests.post(url, headers=headers, json=data)

    @staticmethod
    def get(base_url, endpoint, headers=None, params=None) -> Response:
        """
        This is a Python function that sends a GET request to a specified endpoint with optional headers and
        parameters, logs the request and response, and returns the response.

        :param base_url: The base URL of the API endpoint that we want to access. It is the common part of
        the URL that remains the same for all API requests
        :param endpoint: The endpoint is a specific URL that is appended to the base URL to access a
        particular resource or functionality provided by the API. It is the part of the URL that comes after
        the domain name and any subdirectories. For example, if the base URL is "https://api.example.com"
        and the
        :param headers: The headers parameter is a dictionary containing HTTP headers to be sent with the
        request. These headers provide additional information about the request, such as the user agent,
        content type, and authentication credentials
        :param params: The `params` parameter is a dictionary of query string parameters to include in the
        GET request. These parameters are appended to the URL after a question mark (?) and separated by
        ampersands (&). For example, if `params` is `{'q': 'python', 'page': 2}`,
        :return: a response object obtained from making a GET request to a specified endpoint with optional
        headers and parameters.
        """
        url = f"{base_url}/{endpoint}"
        return requests.get(url, headers=headers, params=params)

    @staticmethod
    def put(base_url, endpoint, data):
        """
        The function sends a PUT request to a specified endpoint with provided data and logs the request and
        response.

        :param base_url: The base URL of the API endpoint that the PUT request will be sent to
        :param endpoint: The endpoint is a specific URL that is appended to the base URL to access a
        particular resource or functionality of an API. It is the part of the URL that comes after the
        domain name or IP address
        :param data: The data parameter is the payload that will be sent in the body of the PUT request. It
        should be a JSON object
        :return: the response object obtained from making a PUT request to the specified endpoint with the
        provided data and headers.
        """
        url = f"{base_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}
        return requests.put(url, json=data, headers=headers)

    @staticmethod
    def patch(base_url, endpoint, json=None, headers=None):
        """
        This function sends a PATCH request to a specified endpoint with provided data and headers, and logs
        the request and response.

        :param base_url: The base URL of the API endpoint that the request will be sent to
        :param endpoint: The specific endpoint of the API that we want to send a PATCH request to. It is a
        string that is appended to the base URL to form the complete URL for the API endpoint
        :param data: The data parameter is the payload to be sent in the request body. It can be a
        dictionary, list of tuples, bytes, or file-like object
        :param headers: The headers parameter is an optional dictionary that contains HTTP headers to be
        sent with the request. These headers provide additional information about the request, such as the
        content type of the data being sent or authentication credentials. If no headers are provided, the
        request will be sent with default headers
        :return: a response object from the `requests.patch()` method.
        """
        url = f"{base_url}/{endpoint}"
        # # Log the request details
        # logger.info("Sending PATCH request to %s", url)
        # logger.info("Headers: %s", json.dumps(headers, indent=4))
        # logger.info("Body: %s", json.dumps(data, indent=4) if data else "None")
        return requests.patch(url, json=json, headers=headers)

    @staticmethod
    def delete(base_url, endpoint, headers):
        """
        The function sends a DELETE request to a specified endpoint and logs the request and response
        information.

        :param base_url: The base URL of the API endpoint that we want to send a DELETE request to. It is
        the starting part of the URL that remains constant for all requests to that API. For example,
        "https://api.example.com"
        :param endpoint: The endpoint is a specific URL that is used to access a particular resource or
        functionality on a web server. It is the part of the URL that comes after the base URL and any path
        parameters. For example, if the base URL is "https://api.example.com" and the endpoint is "/users
        :param headers: A dictionary of HTTP headers
        :return: the response object obtained from making a DELETE request to the specified endpoint on the
        given base URL.
        """
        url = f"{base_url}/{endpoint}"
        return requests.delete(url, headers=headers)