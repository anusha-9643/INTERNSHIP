# Problem: Permission Checker
# You want a function dashboard() but only admin should access it.
# What to do
# Create a decorator called admin_only
# Decorator behavior
# if username == "admin" → allow function execution
# else → print "Access Denied"
# Apply decorator
# Use it on:
# dashboard()
# Test
# Call dashboard using:
# admin → works
# other user → blocked

def admin_only(fun):
    def wrapper(username):
         if username == "admin":
              fun(username)
         else:
              print("Access Denied")
    return wrapper

@admin_only
def dashboard(username):
     print("Welcome to dashboard")

username = "admin"
dashboard(username)


