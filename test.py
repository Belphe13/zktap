# check access and log actions?

import time

from catalog.models import Door, DoorRequest
from accounts.models import User

starttime=time.time()
while True:
    input_bool = 'True' # assume take external input later

    input_door = Door.objects.get(door_name='Instructional Clean Room') # take door_public_key
    input_name = User.objects.get(username='lyang57') # user_public_key

    input_access = DoorRequest.objects.get(door = input_door, user = input_name)

    unlock = input_access.status
    print(input_access.status)

    if input_bool == 'True' and unlock == 'approved':
        print("You got in!")
    else:
        print("Nay")
    time.sleep(1)