from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateTimeField()

    def __str__(self):
        return "{},{},{},{}".format(self.id, self.first_name, self.last_name, self.dob)

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    notes = models.CharField(max_length=200)

    def __str__(self):
        return "{},{},{}".format(self.session_id, self.date, self.notes)

class Techniques(models.Model):
    technique_id = models.AutoField(primary_key=True)
    technique = models.CharField(max_length=20)

    def __str__(self):
        return "{},{}".format(self.technique_id, self.technique)

class Session_Techniques(models.Model):
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    technique_id = models.ForeignKey(Techniques, on_delete=models.CASCADE)

    def __str__(self):
        return "{},{}".format(self.session_id, self.technique_id)

class Climbs(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    v_grade = models.IntegerField(default=0)
    num_success = models.IntegerField(default=0)
    num_attempts = models.IntegerField(default=0)

    def __str__(self):
        return "{},{},V{}, success: {}, attempt: {}".format(self.user_id, self.session_id, self.v_grade, self.num_success, self.num_attempts)