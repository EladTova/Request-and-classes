import requests

# Sending a request to the specified url and saving the data.
res = requests.get('https://jsonplaceholder.typicode.com/users')

# MyUser class definition
class MyUser:

    # Constructor
    def __init__(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email

    # Print function
    def __str__(self):
        return f'MyUser({self.id}, {self.name}, {self.username}, {self.email})'

if __name__ == '__main__':

    # Transfer the dictionary to json.
    urlUsersDictionary = res.json()

    # Requesting from the client to enter his name
    userNameInput = input('Please enter your name:')

    doesUserExistsFlag = False

    # The loop will go over all the users in the url users dictionary and will
    # compare each user's name to the client input. In case of a match the
    # program will print a suitable message + user properties.
    for user in urlUsersDictionary:
        # Creating a MyUser object using the MyUser class constructor
        MyUserObj = MyUser(user['id'], user['name'], user['username'],
                           user['email'])
        # Names comparison
        if MyUserObj.name == userNameInput:
            print('User found:')
            print(MyUserObj)
            doesUserExistsFlag = True
            break

    # In case the given input has not been found
    if not doesUserExistsFlag:
        print('user not found')
