
from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=20,)

    def __str__(self):
        return self.title


class Candidate(models.Model):
    COURSES = [("BIT", "Information Technology"),
               ("LLB", "LAW"),
               ("M", "Medicine"),
               ("SWASWA", "SOCIAL WORKS"),
               ]
    GENDER_OPTIONS = [
        ("M", "Male"),
        ("F", "Female"),

    ]
    name = models.CharField(max_length=50)
    address = models.CharField(
        max_length=10, null=True, blank=True, default="N/A")
    gender = models.CharField(max_length=10, choices=GENDER_OPTIONS)
    email = models.EmailField(default=None)
    course = models.CharField(max_length=20, choices=COURSES)
    contact = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.position)


class Voter(models.Model):
    COURSES = [("BIT", "Information Technology"),
               ("LLB", "LAW"),
               ("M", "Medicine"),
               ("SWASWA", "SOCIAL WORKS"),
               ("BCOM", "Bachelor In Commerce")
               ]
    GENDER_OPTIONS = [
        ("M", "Male"),
        ("F", "Female"),

    ]
    reg_no = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    gender = models.CharField(max_length=10, choices=GENDER_OPTIONS)
    address = models.CharField(max_length=30)
    course = models.CharField(max_length=20, choices=COURSES)
    email = models.EmailField(default=None)
    contact = models.CharField(max_length=15)
    birth_date = models.DateField(auto_now=False)

    def __str__(self):
        return self.reg_no


class Vote(models.Model):

    voter_id = models.ForeignKey(Voter, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE)
    candidated_voted = models.ForeignKey(Candidate, on_delete=models.CASCADE)
