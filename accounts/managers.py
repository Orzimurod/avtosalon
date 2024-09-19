from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self,phone_number,password=None,**extra_fields):
        if not phone_number:
            raise ValueError('Users must havean phone_number address')
        user = self.model(phone_number=phone_number,**extra_fields,password=make_password(password))
        user.save(using = self._db)

        return user
    

    def create_superuser(self,phone_number,password):
        user = self.create_user(phone_number,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    


