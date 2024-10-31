from dataclasses import dataclass, asdict
from typing import Dict, Optional


@dataclass
class User:
    """Represents an user with information details.

    Args:
        name (str): The name of the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        address (Optional[str]): The user's address (default is None).
        phone (Optional[str]): The user's phone number (default is None).
        website (Optional[str]): The user's website (default is None).
        company (Optional[str]): The company of the user (default is None).
        id (Optional[int]): The user ID (default is None).
    """

    name: str
    username: str
    email: str
    adress: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    company: Optional[str] = None
    id: Optional[int] = None

    def to_json(self) -> Dict:
        """Converts the user instance to a JSON dictionary.

        Returns:
            Dict: A dictionary representation of the user instance.
        """
        return asdict(self)


@dataclass
class Post:
    """Represents a post with information details.

    Args:
        title (str): The title of the post.
        body (str): The body of the post.
        id (Optional[int]): The ID of the post.
        userId (Optional[int]): The ID of the user to whom the post belongs.
    """

    title: str
    body: str
    id: Optional[int] = None
    userId: Optional[int] = None

    def to_json(self) -> Dict:
        """Converts the post instance to a JSON dictionary.

        Returns:
            Dict: A dictionary representation of the post instance.
        """
        return asdict(self)


@dataclass
class Comment:
    """Represents a comment with information details.

    Args:
        name (str): The name of the user who made the comment.
        email (str): The email of the user who made the comment.
        body (str): The body of the comment.
        id (Optional[int]): The ID of the comment.
        postId (Optional[int]): The ID of the post to which the comment belongs.
    """

    name: str
    email: str
    body: str
    id: Optional[int] = None
    postId: Optional[int] = None

    def to_json(self) -> Dict:
        """Converts the comment instance to a JSON dictionary.

        Returns:
            Dict: A dictionary representation of the comment instance.
        """
        return asdict(self)
