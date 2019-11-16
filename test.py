# check access and log actions

from catalog.models import User

print(User.objects.all())

newuser = User(netid = "newid")
newuser.save()