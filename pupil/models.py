from django.db import models


class Pupil(models.Model):
    NURSERY_ONE = 'N1'
    NURSERY_TWO = 'N2'
    NURSERY_THREE = 'N3'
    PRIMARY_ONE = 'P1'
    PRIMARY_TWO = 'P2'
    PRIMARY_THREE = 'P3'
    PRIMARY_FOUR = 'P4'
    PRIMARY_FIVE = 'P5'
    PRIMARY_SIX = 'P6'
    CLASS_CHOICES = (
        (NURSERY_ONE, 'Nursery One'),
        (NURSERY_TWO, 'Nursery Two'),
        (NURSERY_THREE, 'Nursery Three'),
        (PRIMARY_ONE, 'Primary One'),
        (PRIMARY_TWO, 'Primary Two'),
        (PRIMARY_THREE, 'Primary Three'),
        (PRIMARY_FOUR, 'Primary Four'),
        (PRIMARY_FIVE, 'Primary Five'),
        (PRIMARY_SIX, 'Primary Six'),)
    full_name = models.CharField(max_length=100)
    pupil_class = models.CharField(
        'Class', max_length=2, choices=CLASS_CHOICES)
    image = models.ImageField(upload_to='application')
    date_of_birth = models.DateField()
    date_of_registration = models.DateField(blank=True, null=True)
    parent_name = models.CharField(max_length=100)
    contact_number = models.CharField(
        max_length=13, blank=True, null=True)
    email = models.EmailField(blank=True)
    home_address = models.CharField(
        max_length=50, blank=True, null=True)
    student_number = models.CharField(
        max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Caution(models.Model):
    pupil = models.ForeignKey(
        Pupil, on_delete=models.CASCADE)
    date_of_caution = models.DateField()
    reason = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Caution: {self.pupil}"
