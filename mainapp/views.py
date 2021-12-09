from django.shortcuts import render
from rest_framework.decorators import api_view
from . import models
from utils.reponse_helper import Success_response,CustomError
from django.core.mail import send_mail
from django.conf import settings


@api_view(['GET'])
def get_all_events(request,pk=None):
    "get all events"
    # the reason am doing this is becuse i want access the image url from aws 
    eventData = []
    eventUrl= ''
    for event in models.Event.objects.all():
        try:eventUrl = event.event_photo.url
        except:eventUrl =''
        
        eventData.append(
           { "id":event.id,"event_name":event.event_name,
           'event_photo':eventUrl,'form_message':event.form_message,
           "is_how_can_help":event.is_how_can_help
           
           
           }
        )


    return Success_response(data=eventData)
    # .values('id','event_name',)


@api_view(['POST'])
def registerForEvent(request,eventID=None):
    if eventID is None:
        raise CustomError("Pick an event To Register For")

    if not models.Event.objects.filter(id=eventID).exists():
        "if it doesnt exits complain"
        return CustomError("This Event Does't Exits or Has Been Erased")

    email =''
    name = ''
    phone_number = ''
    try:
        email = request.data['email']
        name = request.data['name']
        phone_number = request.data['phone_number']
    except:
        raise CustomError("Please Check Fields Email and Name are needed")

    event = models.Event.objects.get(id=eventID)
    register  = models.peopleEnrollfor.objects.create(event=event,email=email,name=name,phone_number=phone_number)
    register.save()

        
    # try:
    #     send_mail(
    #         f'Hi {name} You Registered For {event.event_name}',
    #         event.email_message_confirm,
    #         settings.EMAIL_HOST_USER,
    #         [email],
    #         fail_silently=False,
    #     )
    # except:
    #     raise CustomError('Try again there Seem to Be a Network issue')
    return Success_response()

@api_view(['GET'])
def get_testimonials(request,pk=None):
    formated_data = []
    testimonials = models.Testimonial.objects.all()
    imageUrl =''
    for testimonial in testimonials:
        try:imageUrl=testimonial.person_image.url
        except:imageUrl=""
        formated_data.append({
            "text":testimonial.text,
            "person_image":imageUrl,
            "person_name":testimonial.person_name
        })
    
    return Success_response(data=formated_data)


@api_view(['GET'])
def get_allQuotes(request,pk=None):
    QUote = models.Quotes.objects.all().first().values('id','quote')

    return Success_response(data=QUote)

@api_view(['GET'])

def get_all_resourcesTable(request,pk=None):
    

    all_resources = models.ResourcesTable.objects.all()
    formated_data = []
    imageUrl = ''
    for recource in all_resources:
        try:imageUrl = recource.heading_picture.url
        except:imageUrl=""
        formated_data.append({
            'blog_link':recource.blog_link,"heading_text":recource.heading_text,
            "heading_picture":imageUrl})
        
    return Success_response(data=formated_data)


@api_view(['GET'])
def get_all_skits(request,pk=None):
    formated_data = []

    all_skit = models.SkitTable.objects.all()
    imageUrl =''
    for eachSkit in all_skit:
        try:imageUrl=eachSkit.heading_picture.url
        except:imageUrl = ""

        formated_data.append({'heading_picture':imageUrl,"youtube_link":eachSkit.youtube_link,"heading_text":eachSkit.heading_text})

    return Success_response(data=formated_data)


@api_view(['POST'])
def save_contact_us(requst):


    email =''
    name = ''
    phone_number = ''
    message= ''
    try:
        email = request.data['email']
        name = request.data['name']
        phone_number = request.data['phone_number']
        message = ''
    except:
        raise CustomError("Please Check Fields Email and Name are needed")


    contact_us = models.Contact.objects.create(email=email,name=name,phone_number=phone_number,message=message)

    contact_us.save()
    return Success_response()
