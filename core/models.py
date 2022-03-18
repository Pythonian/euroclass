from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Application(models.Model):
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
    pupil_class = models.CharField(max_length=2, choices=CLASS_CHOICES)
    image = models.ImageField(upload_to='application')
    date_of_birth = models.DateField()
    parent_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=13)
    email = models.EmailField(blank=True)
    home_address = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class SchoolManagement(models.Model):
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='management')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class PTAManagement(models.Model):
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='management')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class PTAMeetingResolution(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FrequentlyAskedQuestion(models.Model):
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FrequentlyAskedQuestionDescription(models.Model):
    faq = models.ForeignKey(FrequentlyAskedQuestion,
                            on_delete=models.CASCADE,
                            related_name='faqs')
    description = models.TextField()


class Gallery(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')
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

    @property
    def term_total(self):
        return self.first_term_price + self.second_term_price + self.third_term_price


class SchoolContactInfo(models.Model):
    short_information = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='logo')
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return "School Contact Information"


class About(models.Model):
    history = RichTextUploadingField()
    mission = RichTextField()
    vision = RichTextField()
    admission_information = RichTextField()

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return "About School"


class Legal(models.Model):
    terms = RichTextField()
    privacy_policy = RichTextField()

    class Meta:
        verbose_name_plural = 'Legal'

    def __str__(self):
        return "Legal Information"
