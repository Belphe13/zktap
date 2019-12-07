# check access and log actions?

import time, serial
from random import random
from catalog.models import Door, DoorRequest, Input
from accounts.models import User

# serial port
ser = serial.Serial('/dev/tty.usbmodem14203')

starttime=time.time()
while True:

    inputs = ser.readline()
    input_bool = inputs.rstrip(b'\r\n').split(b';')[1].decode('utf8')
    input_user_public_key=inputs.rstrip(b'\r\n').split(b';')[0].decode('utf8')

#    if input_bool == 'true':
#        print("User verfied")
#    if input_bool == 'false':
#        print("Access denied")
#    print(input_user_public_key)
    input_user = None
    print('got public key:', input_user_public_key)
    try:
        user_tag = User.objects.get(user_public_key=input_user_public_key) # take door_public_key
        print('found user:', user_tag.username)

    except:
        print('User Not Found')
        print('Rejected')


    # if input_user.user_public_key == input_user_public_key:
    if user_tag:
        access = user_tag.doors.all()
        door_pubs = [door.door_public_key for door in access]


        door = Door.objects.get(door_name='EWS Computer Lab')
        door_pub = door.door_public_key

        if door_pub in door_pubs:
            print('Verified')
        else:
            print('Rejected')
    # input_access = DoorRequest.objects.get(door = input_door, user = 'user')

    # unlock = input_access.status
    # print(input_access.status)

#    if input_bool == 'True' and unlock == 'approved':
#        print("You got in!")
#    else:
#        print("Nay")
    time.sleep(1)
