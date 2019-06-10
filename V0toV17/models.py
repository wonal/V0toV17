from django.db import models
from django.core import serializers

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateTimeField()

    def __str__(self):
        return "{},{},{},{}".format(self.id, self.first_name, self.last_name, self.dob)

    class Meta:
        unique_together = [['first_name', 'last_name', 'dob']]

    def natural_key(self):
        return (self.first_name, self.last_name, self.dob)

class UsersManager(models.Model):
    def get_by_natural_key(self, first_name, last_name, dob):
        return self.get(first_name=first_name, last_name=last_name, dob=dob)

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    notes = models.CharField(max_length=200)

    def __str__(self):
        return "{},{},{}".format(self.session_id, self.date, self.notes)

    def natural_key(self):
        return (self.date, self.notes)

class SessionManager(models.Model):
    def get_by_natural_key(self, date, notes):
        return self.get(date=date, notes=notes)

class Techniques(models.Model):
    technique_id = models.AutoField(primary_key=True)
    technique = models.CharField(max_length=20)

    def __str__(self):
        return "{},{}".format(self.technique_id, self.technique)

    class Meta:
        unique_together = [['technique_id', 'technique']]

    def natural_key(self):
        return (self.technique_id, self.technique)

class TechniquesManager(models.Model):
    def get_by_natural_key(self, technique_id, technique):
        return self.get(technique_id=technique_id, technique=technique)

class Session_Techniques(models.Model):
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    technique_id = models.ForeignKey(Techniques, on_delete=models.CASCADE)

    def __str__(self):
        return "{},{}".format(self.session_id, self.technique_id)

class Climbs(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    v_grade = models.IntegerField(default=0)
    num_success = models.IntegerField(default=0)
    num_attempts = models.IntegerField(default=0)

    def __str__(self):
        return "{},{},V{}, success: {}, attempt: {}".format(self.user_id, self.session_id, self.v_grade, self.num_success, self.num_attempts)
