import Flask

# run a function to get the three values from register; call them email, pw1, pw2

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
pet_users = dynamodb.Table('petflix_users')
if pw1 == pw2:
    # That's secure, right?
    pet_users.put_item({"email": email, "password": hash(pw1)})
else:
    # Throw an error, tell the user "passwords don't match"
