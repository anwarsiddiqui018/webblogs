users = []
new_user = {
    'last': 'ahmed',
    'first': 'anwar',
    'username': 'anwar241'
}
users.append(new_user)
print(users)
for user_list in users:
    for key, value in new_user.items():
        print(key + ":" + value)