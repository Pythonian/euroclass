from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Subject(models.Model):
    name = models.CharField(max_length=50)
    # teachers - ManyToMany
    # students - ManyToMany
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    CRECHE_ONE = 'C1'
    CRECHE_TWO = 'C2'
    CRECHE_THREE = 'C3'
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
        (CRECHE_ONE, 'Creche One'),
        (CRECHE_TWO, 'Creche Two'),
        (CRECHE_THREE, 'Creche Three'),
        (NURSERY_ONE, 'Nursery One'),
        (NURSERY_TWO, 'Nursery Two'),
        (NURSERY_THREE, 'Nursery Three'),
        (PRIMARY_ONE, 'Primary One'),
        (PRIMARY_TWO, 'Primary Two'),
        (PRIMARY_THREE, 'Primary Three'),
        (PRIMARY_FOUR, 'Primary Four'),
        (PRIMARY_FIVE, 'Primary Five'),
        (PRIMARY_SIX, 'Primary Six'),)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),)
    YES = 'Y'
    NO = 'N'
    YES_NO_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No'),)
    full_name = models.CharField(
        max_length=100, help_text='format: Surname, Firstname Middlename')
    pupil_class = models.CharField(max_length=2, choices=CLASS_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='application')
    date_of_birth = models.DateField()
    child_id_document = models.FileField(upload_to='documents')
    father_name = models.CharField(
        max_length=100, blank=True, null=True)
    mother_name = models.CharField(
        max_length=100, blank=True, null=True)
    father_contact_number = models.CharField(
        max_length=13, blank=True, null=True)
    mother_contact_number = models.CharField(
        max_length=13, blank=True, null=True)
    father_id_document = models.FileField(
        upload_to='documents', blank=True, null=True)
    mother_id_document = models.FileField(
        upload_to='documents', blank=True, null=True)
    email = models.EmailField(blank=True)
    home_address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    special_assitance = models.BooleanField(
        blank=True,
        help_text='Click if the child needs any special assitance')
    areas_of_assistance = models.CharField(
        max_length=200, blank=True)

    sibling_name_1 = models.CharField(
        max_length=100, blank=True, null=True)
    dob_sibling_1 = models.DateField(blank=True, null=True)
    gender_sibling_1 = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    category_sibling_1 = models.CharField(
        max_length=50, blank=True, null=True)
    sibling_class_1 = models.CharField(
        max_length=2, choices=CLASS_CHOICES, blank=True, null=True)

    sibling_name_2 = models.CharField(
        max_length=100, blank=True, null=True)
    dob_sibling_2 = models.DateField(blank=True, null=True)
    gender_sibling_2 = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    category_sibling_2 = models.CharField(
        max_length=50, blank=True, null=True)
    sibling_class_2 = models.CharField(
        max_length=2, choices=CLASS_CHOICES, blank=True, null=True)

    sibling_name_3 = models.CharField(
        max_length=100, blank=True, null=True)
    dob_sibling_3 = models.DateField(blank=True, null=True)
    gender_sibling_3 = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    category_sibling_3 = models.CharField(
        max_length=50, blank=True, null=True)
    sibling_class_3 = models.CharField(
        max_length=2, choices=CLASS_CHOICES, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class SchoolManagement(models.Model):
    ROLE_CHOICES = (
        ('L', 'Leadership Team'),
        ('T', 'Teachers'),
        ('A', 'Teaching Assistants'),
        ('O', 'Office Staff'),
        ('S', 'Support Staff'))
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    title = models.CharField(
        max_length=25, blank=True,
        help_text='E.g: Principal, Senior Teacher')
    image = models.ImageField(upload_to='management')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'School Management'
        verbose_name = 'School Management'

    def __str__(self):
        return self.full_name


class PTAManagement(models.Model):
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='management')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'PTA Management'
        verbose_name_plural = 'PTA Management'

    def __str__(self):
        return self.full_name


class PTAMeetingResolution(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'PTA Meeting Resolution'
        verbose_name_plural = 'PTA Meeting Resolutions'

    def __str__(self):
        return self.title


class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=150)
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Frequently Asked Question'
        verbose_name_plural = 'Frequently Asked Questions'

    def __str__(self):
        return self.question


class Picture(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='picture')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption


class Tuition(models.Model):
    NURSERY_SCHOOL = 'NS'
    PRIMARY_SCHOOL = 'PS'
    SCHOOL_TYPE_CHOICES = (
        (NURSERY_SCHOOL, 'Nursery School'),
        (PRIMARY_SCHOOL, 'Primary School'))
    tuition_info = models.CharField(
        max_length=50, help_text='3-month Terms')
    first_term_period = models.CharField(
        max_length=100, help_text='Eg. January-March')
    first_term_price = models.IntegerField()
    second_term_period = models.CharField(
        max_length=100, help_text='Eg. May-July')
    second_term_price = models.IntegerField()
    third_term_period = models.CharField(
        max_length=100, help_text='Eg. September-November')
    third_term_price = models.IntegerField()

    def __str__(self):
        return self.tuition_info

    @property
    def term_total(self):
        return self.first_term_price + self.second_term_price + self.third_term_price


class SchoolContactInfo(models.Model):
    # Add unique=True?
    short_information = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='logo')
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'School Contact Information'
        verbose_name_plural = 'School Contact Information'

    def __str__(self):
        return "School Contact Information"

    def save(self, *args, **kwargs):
        if not self.pk and SchoolContactInfo.objects.exists():
            raise ValidationError(
                'There can only be one SchoolContactInfo instance.')
        return super().save(*args, **kwargs)


class About(models.Model):
    welcome_note = models.TextField()
    welcome_note_image = models.ImageField(upload_to='about')
    history = RichTextUploadingField()
    history_title = models.CharField(max_length=20)
    history_image = models.ImageField(upload_to='about')
    admission_information = RichTextField()
    admission_information_image = models.ImageField(upload_to='about')

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return "About School"
