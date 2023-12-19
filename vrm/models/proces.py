from accounts.models import User
from django.db import models


class Role(models.Model):
    
    ROLE_TYPE_CHOICESS = ((1,'Internal'), (2,'External'))
    
    name = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=1024, null=True, blank=True)
    type = models.IntegerField(choices=ROLE_TYPE_CHOICESS)
    
    def __str__(self):
        return self.name
    


class RolePreference(models.Model):
    
    ROLE_STATUS_CHOICESS = ((1,'New'), (2,'Active'), (3, 'Inactive'), (4, 'Others'), (5,'Dormant'))
    ROLE_OUTCOME_CHOICESS = ((1,'Not Started'), (2,'Inprocess'), (3,'Recommended'), (4,'Recommended for Alternate Role'), (5,'Not Eligible'))
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    status = models.IntegerField(choices=ROLE_STATUS_CHOICESS, default=1)
    role_outcome = models.IntegerField(choices=ROLE_OUTCOME_CHOICESS, default=1)
    recommended_on = models.DateTimeField(null=True, blank=True)
    notes = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return "%s-%s" % (self.user.id, self.role.name)

        
        
class RoleStep(models.Model):
    
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    stepname = models.CharField(max_length = 50, blank=True, null=True)
    description = models.CharField(max_length = 1024, blank=True, null=True)
    weightage = models.IntegerField( default = 0)
    order = models.IntegerField( default = 0 )
    repeatable = models.BooleanField(default=False)
    
    def __str__(self):
        return "%s-%s" % (self.role.name, self.stepname)
    
    
    
class SelectionDiscussionSlot(models.Model):
    
    SLOT_CHOICESS = ((1, 'Not Booked'),(2, 'Booked'))
    OUTCOME_CHOICESS = ((1, 'Scheduled'),(2, 'Assigned'),(3, 'Completed'), (4, 'Cancelled'))
    
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(Role, null=True, blank=True, default=None, on_delete=models.CASCADE)
    panel = models.ForeignKey(User, null=True, blank=True, related_name="panel_member", on_delete=models.DO_NOTHING)
    booked_date = models.DateTimeField(null=True,blank=True)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=SLOT_CHOICESS, default=1)
    outcome = models.IntegerField(choices=OUTCOME_CHOICESS, default=1)


    def __str__(self):
        return "%s-%s :%s" % (self.start_time, self.role.name, self.status)