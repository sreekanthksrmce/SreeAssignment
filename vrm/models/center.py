from django.db import models
from utils.models import Ay
from utils.choicess import *
from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class School(models.Model):
    
    MANAGEMENT_CHOICESS = ((1, 'State'), (2, 'Central'), (3, 'Private'))
    SCHOOL_TYPE_CHOICESS = ((1, 'Co-Educational'), (2, 'Boys Only'),(3, 'Girls Only'))
    REGION_CHOICESS = ((1, 'Rural'), (2, 'Urban'))
    BUILDING_CHOICESS = ((1, 'Unknown'), (2, 'Poor'), (3, 'Good'))
    FURNITURE_CHOICESS = ((1, 'Have None'), (2, 'Require More'), (3, 'Poor'), (4, 'Good'))
    
    
    name                    = models.CharField(max_length=256, null=True, blank=True)
    block                   = models.CharField(max_length=256, null=True, blank=True)
    cluster                 = models.CharField(max_length=256, null=True, blank=True)
    village                 = models.CharField(max_length=256, null=True, blank=True)
    region                  = models.IntegerField(choices=REGION_CHOICESS, default=1)
    pincode                 = models.IntegerField(null=True, blank=True)
    contact_details         = models.CharField(max_length=512, null=True, blank=True)
    location_map            = models.CharField(max_length=1024, null=True, blank=True)
    languages               = models.CharField(max_length=100, null = True, blank=True)
    started_on              = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    beo_name                = models.CharField(max_length=256, null=True, blank=True)
    school_number           = models.CharField(max_length=128, null=True, blank=True)
    school_code             = models.BigIntegerField(default=0,db_index=True)
    photo                   = models.FileField(upload_to='static/uploads/images/center', null=True, blank=True)
    min_grade               = models.IntegerField(default=1, validators=[MaxValueValidator(12), MinValueValidator(1)])
    min_grade               = models.IntegerField(default=10, validators=[MaxValueValidator(12), MinValueValidator(1)])
    total_children          = models.IntegerField(null=True, blank=True)
    management_type         = models.IntegerField(choices=MANAGEMENT_CHOICESS, default=1)
    school_type             = models.IntegerField(choices=SCHOOL_TYPE_CHOICESS, default=1)
    
    total_teachers          = models.IntegerField(null=True, blank=True)
    teachers_male           = models.IntegerField(null=True, blank=True)
    teachers_female         = models.IntegerField(null=True, blank=True)
    principal               = models.CharField(max_length=128, null=True, blank=True)
    refer_by                = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    academic_year           = models.ForeignKey(Ay, null=True, blank=True, on_delete=models.DO_NOTHING)
    building_status         = models.IntegerField(choices=BUILDING_CHOICESS, default=1)
    furniture               = models.IntegerField(choices=FURNITURE_CHOICESS, default=1)
    library                 = models.BooleanField(default=False)
    extra_rooms             = models.IntegerField(default=0)
    electricity             = models.BooleanField(default=False)
    internet                = models.BooleanField(default=False)
    playground              = models.BooleanField(default=False)
    books_in_library        = models.IntegerField(default=0) 
    computers_available     = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Center(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    district = models.CharField(max_length=128, null=True, blank=True)
    village = models.CharField(max_length=128, null=True, blank=True)
    language = models.CharField(max_length=128,choices=LANGUAGE_CHOICESS, null=True, blank=True)
    board = models.CharField(max_length=128,choices=BOARD_CHOICESS, null=True, blank=True)
    working_days = models.TextField(null=True, blank=True)
    working_slots = models.TextField(null=True, blank=True)
    
    photo = models.FileField(upload_to='static/uploads/images/center', null=True, blank=True)
    description = models.TextField(max_length=2048, null=True, blank=True)
    class_location = models.CharField(max_length=256, null=True, blank=True)
    grades = models.CharField(max_length=128, null=True, blank=True)
    students_count = models.IntegerField(default=0)
    status = models.CharField(max_length=256,choices=(('Planned', 'Planned'), ('Active', 'Active'), 
                ('Inactive', 'Inactive'),('Closed','Closed'), ('Provisional', 'Provisional')), default="Planned")
    launch_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    skype_id = models.CharField(max_length=256, null=True, blank=True)
    location_map = models.CharField(max_length=1024, null=True, blank=True)
    
    field_coordinator = models.ForeignKey(User, null=True, blank=True, related_name='center_field_coordinator', on_delete=models.DO_NOTHING)
    delivery_coordinator = models.ForeignKey(User, null=True, blank=True, related_name='center_delivery_coordinator', on_delete=models.DO_NOTHING)
    admin = models.ForeignKey(User, null=True, blank=True, related_name='center_admin', on_delete=models.DO_NOTHING)
    assistant = models.ForeignKey(User, null=True, blank=True, related_name='center_assistant', on_delete=models.DO_NOTHING)
    
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.DO_NOTHING)
    program_type = models.IntegerField(null=True, blank=True, choices=((1,'Digital Classroom'), (2,'Digital School'), (3,'Sampoorna')), default=1)
    is_test = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

class Holiday(models.Model):
    day = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    ay = models.ForeignKey(Ay, on_delete=models.CASCADE)
    center = models.ForeignKey(Center, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return  "%s-%s" %(self.day, self.ay)