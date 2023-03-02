# Create tables: users, roles, user_roles, books, book_orders
# Register an account:
# - When password and retype password match:
#    + Check if account is exists -> Show messagebox Account is exists
#    + If not exists: insert new record to table users (status = 1)
#    + insert role_id = 2, user_id (Student) to table user_roles
#    + return to Login Page
# If mismatch, show messagebox: pasword and retype-password must be match
# Login :
# Check:
        # if Admin, show Blank Admin Toplevel
        # if Student, show Blank Student Toplevel