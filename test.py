# check access and log actions

from catalog.models import Door, DoorRequest
from accounts.models import User

input_bool = 'True' # take external input later

input_door = Door.objects.get(door_name='Senior Design Lab') # take door_public_key
input_name = User.objects.get(username='lyang57') # user_public_key

input_access = DoorRequest.objects.get(door = input_door, user = input_name)

unlock = input_access.status
print(input_access.status)

if input_bool == 'True' and unlock == 'approved':
    print("You got it!")
else:
    print("Nay")
