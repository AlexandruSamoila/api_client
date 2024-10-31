import requests_mock
import pytest
from app.api_client import ApiClient
from typing import Dict

adapter = requests_mock.Adapter()


@pytest.fixture
def api_client():
    """Fixture to create an instance of the API client."""
    return ApiClient(url_adress="https://jsonplaceholder.typicode.com")


@pytest.mark.get
@pytest.mark.parametrize(
    "user_id, user_data, status_code",
    [
        (
            "2",
            {
                "id": 2,
                "name": "Ervin Howell",
                "username": "Antonette",
                "email": "Shanna@melissa.tv",
                "address": {
                    "street": "Victor Plains",
                    "suite": "Suite 879",
                    "city": "Wisokyburgh",
                    "zipcode": "90566-7771",
                    "geo": {"lat": "-43.9509", "lng": "-34.4618"},
                },
                "phone": "010-692-6593 x09125",
                "website": "anastasia.net",
                "company": {
                    "name": "Deckow-Crist",
                    "catchPhrase": "Proactive didactic contingency",
                    "bs": "synergize scalable supply-chains",
                },
            },
            200,
        ),
        (
            "11",
            {
                "error": f"Failed to fetch data for user 11.",
                "status_code": 404,
                "reason": None,
            },
            404,
        ),
    ],
)
def test_get_user(
    user_id: str, user_data: Dict, status_code: int, api_client: ApiClient
):
    """Test the `get_user` method of the ApiClient for a success and a failure scenario.

    Args:
        user_id (str): The id of the user.
        user_data (Dict): The mock data to simulate the server response.
        status_code (int): The status code of the response.
        api_client (ApiClient): An instance of the ApiClient to test.
    """
    url = "https://jsonplaceholder.typicode.com/users/" + user_id
    with requests_mock.Mocker() as mock:
        mock.get(url, json=user_data, status_code=status_code)
        response = api_client.get_user(user_id)
        assert response == user_data


@pytest.mark.get
@pytest.mark.parametrize(
    "post_id, post_data, status_code",
    [
        (
            "3",
            {
                "userId": 1,
                "id": 3,
                "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
                "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut",
            },
            200,
        ),
        (
            "111",
            {"error": f"Failed to fetch post 111.", "status_code": 404, "reason": None},
            404,
        ),
    ],
)
def test_get_posts(
    post_id: str, post_data: Dict, status_code: int, api_client: ApiClient
):
    """Test the `get_posts` method of the ApiClient for a success and a failure scenario.

    Args:
        post_id (str): The id of the post.
        post_data (Dict): The mock data to simulate the server response.
        status_code (int): The status code of the response.
        api_client (ApiClient): An instance of the ApiClient to test.
    """
    url = "https://jsonplaceholder.typicode.com/posts/" + post_id
    with requests_mock.Mocker() as mock:
        mock.get(url, json=post_data, status_code=status_code)
        response = api_client.get_posts(post_id)
        assert response == post_data


@pytest.mark.get
@pytest.mark.parametrize(
    "comment_id, comment_data, status_code",
    [
        (
            "5",
            {
                "postId": 1,
                "id": 5,
                "name": "vero eaque aliquid doloribus et culpa",
                "email": "Hayden@althea.biz",
                "body": "harum non quasi et ratione\ntempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et",
            },
            200,
        ),
        (
            "505",
            {
                "error": f"Failed to fetch comment 505.",
                "status_code": 404,
                "reason": None,
            },
            404,
        ),
    ],
)
def test_get_comments(
    comment_id: str, comment_data: Dict, status_code: int, api_client: ApiClient
):
    """Test the `get_comments` method of the ApiClient for a success and a failure scenario.

    Args:
        comment_id (str): The id of the comment.
        comment_data (Dict): The mock data to simulate the server response.
        status_code (int): The status code of the response.
        api_client (ApiClient): An instance of the ApiClient to test.
    """
    url = "https://jsonplaceholder.typicode.com/comments/" + comment_id
    with requests_mock.Mocker() as mock:
        mock.get(url, json=comment_data, status_code=status_code)
        response = api_client.get_comments(comment_id)
        assert response == comment_data


@pytest.mark.create
@pytest.mark.parametrize(
    "post_data, status_code, expected_result",
    [
        (
            {"title": "title", "body": "body", "userId": "5", "id": 101},
            201,
            {"title": "title", "body": "body", "userId": "5", "id": 101},
        ),
        (
            {"title": "title", "body": "body", "userId": "99", "id": 101},
            404,
            {"error": "Failed to create post.", "status_code": 404, "reason": None},
        ),
    ],
)
def test_create_post(
    post_data: Dict, status_code: int, api_client: ApiClient, expected_result: Dict
):
    """Test the `create_post` method of the ApiClient for a success and a failure scenario.

    Args:
        post_data (Dict): The mock data to simulate the server response.
        status_code (int): The status code of the response.
        api_client (ApiClient): An instance of the ApiClient to test.
        expected_result (Dict): The expected response of the API.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    with requests_mock.Mocker() as mock:
        mock.post(url, json=post_data, status_code=status_code)
        response = api_client.create_post(post_data)
        assert response == expected_result


@pytest.mark.create
@pytest.mark.parametrize(
    "user_data, status_code, expected_result",
    [
        (
            {"name": "name", "username": "username", "email": "email", "id": 11},
            201,
            {"name": "name", "username": "username", "email": "email", "id": 11},
        ),
        (
            {"name": "name", "username": "username", "email": "email", "id": 11},
            404,
            {"error": "Failed to create user.", "status_code": 404, "reason": None},
        ),
    ],
)
def test_create_user(
    user_data: Dict, status_code: int, api_client: ApiClient, expected_result: Dict
):
    """Test the `create_user` method of the ApiClient for a success and a failure scenario.

    Args:
        user_data (Dict): The mock data to simulate the server response.
        status_code (int): The status code of the response.
        api_client (ApiClient): An instance of the ApiClient to test.
        expected_result (Dict): The expected response of the API.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    with requests_mock.Mocker() as mock:
        mock.post(url, json=user_data, status_code=status_code)
        response = api_client.create_user(user_data)
        assert response == expected_result


@pytest.mark.create
@pytest.mark.parametrize(
    "comment_data, status_code, expected_result",
    [
        (
            {
                "name": "name",
                "email": "email",
                "body": "body",
                "postId": "1",
                "id": 501,
            },
            201,
            {
                "name": "name",
                "email": "email",
                "body": "body",
                "postId": "1",
                "id": 501,
            },
        ),
        (
            {
                "name": "name",
                "email": "email",
                "body": "body",
                "postId": "999",
                "id": 501,
            },
            404,
            {"error": "Failed to create comment.", "status_code": 404, "reason": None},
        ),
    ],
)
def test_create_comment(
    comment_data: Dict, status_code: int, api_client: ApiClient, expected_result: Dict
):
    """Test the `create_comment` method of the ApiClient for a success and a failure scenario.

    Args:
        comment_data (Dict): The mock data to simulate the server response.
        status_code (int): The status code of the response.
        api_client (ApiClient): An instance of the ApiClient to test.
        expected_result (Dict): The expected response of the API.
    """
    url = "https://jsonplaceholder.typicode.com/comments"
    with requests_mock.Mocker() as mock:
        mock.post(url, json=comment_data, status_code=status_code)
        response = api_client.create_comment(comment_data)
        assert response == expected_result


@pytest.mark.update
@pytest.mark.parametrize(
    "post_id, post_data, status_code, expected_result",
    [
        (
            "15",
            {"title": "title", "body": "body", "id": 15},
            200,
            {"title": "title", "body": "body", "id": 15},
        ),
        (
            "999",
            {"title": "title", "body": "body", "id": 15},
            404,
            {"error": "Failed to update post.", "status_code": 404, "reason": None},
        ),
    ],
)
def test_update_post(
    post_id: str,
    post_data: Dict,
    status_code: int,
    expected_result: Dict,
    api_client: ApiClient,
):
    """Test the `update_post` method of the ApiClient for a success and a failure scenario.

    Args:
        post_id (str): The ID of the post to be updated.
        post_data (Dict): The mock data to simulate the server response.
        status_code (int): The status code of the response.
        api_client (ApiClient): An instance of the ApiClient to test.
        expected_result (Dict): The expected response of the API.
    """
    url = "https://jsonplaceholder.typicode.com/posts/" + post_id
    with requests_mock.Mocker() as mock:
        mock.put(url, json=post_data, status_code=status_code)
        response = api_client.update_post(post_id=post_id, data=post_data)
        assert response == expected_result


@pytest.mark.delete
@pytest.mark.parametrize(
    "post_id, status_code, expected_result",
    [
        ("6", 200, {"message": "Post 6 deleted successfully."}),
        (
            "999",
            404,
            {"error": "Failed to delete post 999.", "status_code": 404, "reason": None},
        ),
    ],
)
def test_delete_post(
    post_id: str, status_code: int, expected_result: Dict, api_client: ApiClient
):
    """Test the `delete_post` method of the ApiClient for a success and a failure scenario.

    Args:
        post_id (str): The ID of the post to be deleted.
        status_code (int): The status code of the response.
        api_client (ApiClient): An instance of the ApiClient to test.
        expected_result (Dict): The expected response of the API.
    """
    url = "https://jsonplaceholder.typicode.com/posts/" + post_id
    with requests_mock.Mocker() as mock:
        mock.delete(url, status_code=status_code)
        response = api_client.delete_post(post_id=post_id)
        assert response == expected_result
