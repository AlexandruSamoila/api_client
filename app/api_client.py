import requests
from typing import Dict


class ApiClient:
    """
    Client to interact with the JSONPlaceholder API. It includes methods to get, create, update and delete data
    from the JSONPlaceholder API.

    Args:
        url_adress (str): The base URL for the JSONPlaceholder API.
    """

    def __init__(self, url_adress) -> None:
        self.url = url_adress

    def get_posts(self, post_id: str) -> Dict:
        """Get a post based on the post ID.

        Args:
            post_id (str): The ID of the post to retrieve.

        Returns:
            Dict: Dictionary containing the post data if the post is found, otherwise an error message
        """
        response = requests.get(self.url + "/posts/" + post_id)
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"Failed to fetch post {post_id}.",
                "status_code": response.status_code,
                "reason": response.reason,
            }

    def get_comments(self, comment_id: str) -> Dict:
        """Get a comment based on the comment ID.

        Args:
            comment_id (str): The ID of the comment to retrieve.

        Returns:
            Dict: Dictionary containing the comment data if the comment is found, otherwise an error message
        """
        response = requests.get(self.url + "/comments/" + comment_id)
        if response.status_code == 200:
            print(response.status_code)
            return response.json()
        else:
            return {
                "error": f"Failed to fetch comment {comment_id}.",
                "status_code": response.status_code,
                "reason": response.reason,
            }

    def get_user(self, user_id: str) -> Dict:
        """Get a user based on the user ID.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            Dict: Dictionary containing the user data if the user is found, otherwise an error message
        """
        response = requests.get(self.url + "/users/" + user_id)
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"Failed to fetch data for user {user_id}.",
                "status_code": response.status_code,
                "reason": response.reason,
            }

    def get_all_users(self) -> Dict:
        """Get all the users.

        Returns:
            Dict: Dictionary containing the data of all users if the request is successful, otherwise an error message
        """
        response = requests.get(self.url + "/users")
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": "Failed to fetch data for all users.",
                "status_code": response.status_code,
                "reason": response.reason,
            }

    def create_post(self, data: Dict) -> Dict:
        """Create a new post using the provided data.

        Args:
            data (Dict): The post data to be created.

        Returns:
            Dict: Dictionary containing the created post data if the request is successful,
              otherwise an error message
        """
        response = requests.post(self.url + "/posts", data)
        if response.status_code == 201:
            return response.json()
        else:
            return {
                "error": "Failed to create post.",
                "status_code": response.status_code,
                "reason": response.reason,
            }

    def update_post(self, post_id: str, data: Dict) -> Dict:
        """Update a post based on a post ID using the provided data.

        Args:
            post_id (str): The ID of the post to be updated.
            data (Dict): Dictionary containing the new data to update the post.

        Returns:
            Dict: Dictionary containing the updated post data if the request is successful,
              otherwise an error message
        """
        response = requests.put(self.url + "/posts/" + post_id, data)
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": "Failed to update post.",
                "status_code": response.status_code,
                "reason": response.reason,
            }

    def delete_post(self, post_id: str) -> Dict:
        """Delete a post based on the post ID.

        Args:
            post_id (str): The ID of the post to be deleted.

        Returns:
            Dict: Dictionary containing a success message if the request is successful, otherwise an error message
        """
        response = requests.delete(self.url + "/posts/" + post_id)
        if response.status_code == 200:
            return {"message": f"Post {post_id} deleted successfully."}
        else:
            return {
                "error": f"Failed to delete post {post_id}.",
                "status_code": response.status_code,
                "reason": response.reason,
            }

    def create_user(self, data: Dict) -> Dict:
        """Create a new user using the provided data.

        Args:
            data (Dict): The user data to be created.

        Returns:
            Dict: Dictionary containing the created user data if the request is successful,
              otherwise an error message
        """
        response = requests.post(self.url + "/users", data)
        if response.status_code == 201:
            return response.json()
        else:
            return {
                "error": "Failed to create user.",
                "status_code": response.status_code,
                "reason": response.reason,
            }

    def create_comment(self, data: Dict) -> Dict:
        """Create a new comment using the provided data.

        Args:
            data (Dict): The comment data to be created.

        Returns:
            Dict: Dictionary containing the created comment data if the request is successful,
              otherwise an error message
        """
        response = requests.post(self.url + "/comments", data)
        if response.status_code == 201:
            return response.json()
        else:
            return {
                "error": "Failed to create comment.",
                "status_code": response.status_code,
                "reason": response.reason,
            }
