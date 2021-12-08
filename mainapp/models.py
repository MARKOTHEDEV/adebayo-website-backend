from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager



class UserManager(BaseUserManager):
    "this is what will manage the user"

    def create_user(self,email,password=None):
        "this is a custom function used to create my custom user"

        if password is None:
            raise ValueError("You Need To enter A Valid Password")

        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password):
        # function create a normal user and convert it to a Super User
        user = self.create_user(email,password)
        
        user.is_staff = True
        user.is_superuser=True
        user.save()

        return user

class User(PermissionsMixin,AbstractBaseUser):
    'This is Our Custom User The Whole Project will Use'

    email =      models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]
    # now i want to link the custom UserManager to Help me manage this my custom user
    objects =UserManager()

    def __str__(self):
        "String Rep of THe user"
        return f'{self.email}'





class SkitTable(models.Model):
    "this Hols all the skit link to the youtube .. pictures heading .."
    heading_picture = models.ImageField(upload_to='skitPhotos/')
    youtube_link = models.TextField()
    heading_text = models.CharField(max_length=400)
    

    def __str__(self):
        return f'{self.id})  {self.heading_text}'


class ResourcesTable(models.Model):
    heading_text = models.CharField(max_length=400)
    blog_link = models.TextField()
    heading_picture = models.ImageField(upload_to='resources/')

    def __str__(self):
        return self.heading_text

class Event(models.Model):
    event_name = models.CharField(max_length=300)
    event_photo =models.ImageField(upload_to='event_pictures/')
    form_message = models.TextField()
    email_message_confirm = models.TextField()
    is_how_can_help = models.BooleanField(default=False)
    def __str__(self):
        return self.event_name


class peopleEnrollfor(models.Model):
    "many people will enroll for one Event"
    event = models.ForeignKey(Event,on_delete=models.SET_NULL,null=True)
    email= models.EmailField()
    phone_number= models.CharField(max_length=90,default="NiL")
    name = models.CharField(max_length=300)

    def __str__(self):
        return f'Enroll for {self.event or "Event Deleted Already"}'  

class Quotes(models.Model):
    quote = models.TextField()

    def __str__(self):
        return f' Quoute number {self.id}'

class Testimonial(models.Model):
    text = models.TextField()
    person_image = models.ImageField(upload_to='testimonal_image/')
    person_name= models.CharField(max_length=200)

    def __str__(self):
        return f'Testimnials from ..{self.person_name}'