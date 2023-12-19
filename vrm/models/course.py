'''
    Course related tables
'''

from django.db import models
from utils.models import Ay
from vrm.models.center import Center
from utils.choicess import *
from django.core.validators import MaxValueValidator, MinValueValidator
from utils.models import Language
from django.conf import settings
from accounts.models import User
 

class Course(models.Model):
    board = models.CharField(max_length=128,choices=BOARD_CHOICESS, null=True, blank=True)
    subject = models.CharField(max_length=128, null=True, blank=True,db_index=True)
    grade = models.IntegerField(default=1, validators=[MaxValueValidator(settings.MAX_GRADE), MinValueValidator(settings.MIN_GRADE)])
    description = models.TextField(max_length=2048, null=True, blank=True)
    picture = models.FileField(upload_to='static/uploads/images/course', null=True, blank=True)
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.DO_NOTHING)
    availabilityType = models.CharField(max_length=50, choices=(('1', 'Web1.0 Only'), ('2', 'Mobile App only'),('3', 'All Platforms')), default="3")
    status = models.IntegerField(choices=((1,'Active'), (2,'Inactive')), default=1)

    def __str__(self):
        return "%s-%s-%s" % (self.board, self.grade, self.subject)


class Topic(models.Model):
    title = models.CharField(max_length=512)
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    num_sessions = models.IntegerField(default=1)
    status = models.IntegerField(choices=((1,'Active'), (2,'Inactive')), default=1)
    
    def __str__(self):
        return self.title


class SubTopic(models.Model):
    name = models.CharField(max_length=1024, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    status = models.IntegerField(choices=((1,'Active'), (2,'Inactive')), default=1)

    def __str__(self):
        return self.name
    


    
    

class Offering(models.Model):
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.DO_NOTHING)
    center = models.ForeignKey(Center, null=True, blank=True, on_delete=models.DO_NOTHING)
    ay =  models.ForeignKey(Ay, null=True, blank=True, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    topic = models.ManyToManyField(Topic, blank=True)
    status = models.IntegerField(choices=((1, 'pending'),(2, 'running'),(3, 'completed')), default=1)
    student = models.ManyToManyField(User, related_name='enrolled_students')
    teacher = models.ForeignKey(User, null=True, blank=True, related_name='current_teacher', on_delete=models.DO_NOTHING)
    batch = models.IntegerField(null=True, blank=True)
    program = models.IntegerField(choices=((0, 'None'),(1,'Digital Classroom'),(2,'LFH'),(3,'Worksheets'), (4,'Alumni'),(5,'Digital School')), default=0)
    
    @property
    def started_sessions(self):
        return Session.objects.filter(offering=self, status='started')

    @property
    def pending_sessions(self):
        return Session.objects.filter(offering=self, status='pending')

    def __str__(self):
        return '%s-%s' %(self.course, self.ay)

    

class Session(models.Model):
    
    STATUS_CHOICESS = ((1,'waiting'), (2,'scheduled'), (3,'completed'), (4,'rescheduled'),(5,'started'),(6,'cancelled'), (7,'Offline'))
    
    CANCLE_REASON_CHOICESS = ((1, 'Internet Down School'), (2, 'Power Cut School'), (3, 'Unscheduled leave School'), (4, 'Internet Down Teacher'),
     (5,'Power Cut Teacher'),(6,'Last Minute Dropout Teacher'), (7,'Communication Issue'), (8,'Teacher yet to be backfilled'), (9,'Others'))
    
    
    offering = models.ForeignKey(Offering, on_delete=models.CASCADE)
    topic = models.ManyToManyField(Topic, blank=True)
    subtopic = models.ForeignKey(SubTopic, null=True, blank=True, on_delete=models.CASCADE)
    
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    teacher = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    status = models.IntegerField(choices=STATUS_CHOICESS, default=1)
    video = models.CharField(max_length=1024, null=True, blank=True)
    comment = models.TextField(max_length=2048, null=True, blank=True)
    cancel_reason = models.IntegerField(choices=CANCLE_REASON_CHOICESS, null=True, blank=True)
    ts_link = models.CharField(max_length=1024, blank=True)
    
    used_lesson_plan = models.BooleanField(default=True)

    def __str__(self):
        return '%s-%s :%s' %(self.start_date, self.end_date, self.teacher)
