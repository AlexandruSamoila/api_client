from app.api_client import ApiClient
from app.data import User, Post, Comment


class Menu:
    """
    A console menu to interact with the application.

    It allows users to perform actions like listing information about users, posts, comments,
    and creating, updating or deleting posts.

    Args:
        api_client(ApiClient): An instance of the ApiClient used to make API requests.
    """

    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    def run(self) -> None:
        """
        Starts the console menu loop. Based on the user's choice, it performes the desired action
        and display the result. It continues to run until the user chooses the option to exit.
        """
        while True:
            print("\n=====================================")
            print("Choose the action from the following:")
            print("1. View all users")
            print("2. View user details")
            print("3. View post details")
            print("4. View comments details")
            print("5. Create a new post")
            print("6. Update an existing post")
            print("7. Delete a post")
            print("8. Create a new user")
            print("9. Add a comment to a post")
            print("0. Exit")
            print("=====================================\n")
            choice = input("Enter your choice: ")

            if choice == "1":
                response = self.api_client.get_all_users()
                if "error" not in response:
                    print("All users:")
                print(response)

            elif choice == "2":
                user_id_str = input("Enter user id: ")
                response = self.api_client.get_user(user_id_str)
                if "error" not in response:
                    print("User details:")
                print(response)

            elif choice == "3":
                post_id_str = input("Enter post id: ")
                response = self.api_client.get_posts(post_id_str)
                if "error" not in response:
                    print("User posts:")
                print(response)

            elif choice == "4":
                comment_id_str = input("Enter comment id: ")
                response = self.api_client.get_comments(comment_id_str)
                if "error" not in response:
                    print(f"Comments from the post {comment_id_str}:")
                print(response)

            elif choice == "5":
                user_id_int = int(input("Enter user id: "))
                post_title = input("Enter post title: ")
                post_body = input("Enter post body: ")
                post = Post(userId=user_id_int, title=post_title, body=post_body)
                response = self.api_client.create_post(post.to_json())
                if "error" not in response:
                    print("Post created:")
                print(response)

            elif choice == "6":
                post_id_str = input("Enter post id: ")
                post_title = input("Enter post title: ")
                post_body = input("Enter post body: ")
                post = Post(title=post_title, body=post_body)
                response = self.api_client.update_post(post_id_str, post.to_json())
                if "error" not in response:
                    print("Post updated:")
                print(response)

            elif choice == "7":
                post_id_str = input("Enter post id to be deleted: ")
                response = self.api_client.delete_post(post_id_str)
                print(response["message"])

            elif choice == "8":
                user_name = input("Enter the name: ")
                user_username = input("Enter the username: ")
                user_email = input("Enter the email: ")
                user = User(name=user_name, username=user_username, email=user_email)
                response = self.api_client.create_user(user.to_json())
                if "error" not in response:
                    print("User created:")
                print(response)

            elif choice == "9":
                post_id_int = int(input("Enter post id: "))
                comment_name = input("Enter the name: ")
                comment_email = input("Enter the email: ")
                comment_body = input("Enter the comment body: ")
                comment = Comment(
                    postId=post_id_int,
                    name=comment_name,
                    email=comment_email,
                    body=comment_body,
                )
                response = self.api_client.create_comment(comment.to_json())
                if "error" not in response:
                    print("Comment created:")
                print(response)

            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")
