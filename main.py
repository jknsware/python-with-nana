from user import User
from post import Post

app_user_one = User("jason@jknsware.com", "Jason Ware", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "James Bond", "supersecret", "Agent")
app_user_two.get_user_info()

new_post = Post("On a secret mission today" , app_user_two.name)
new_post.get_post_info()