from django.db import models
from sys_management.models import Instructor
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

STATUS = (
    (0, "DRAFT"),
    (1, "PUBLISH")
)
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)

class Course(models.Model):
    DIFFICULTY_CHOICES = (
        ('BEGINNNER', 'Beginnner'),
        ('INTERMIDIATE', 'Intermidiate'),
        ('HARD','Hard')
    )

    title = models.CharField(max_length=300, db_index=True)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, related_name='my_courses')
    duration = models.CharField(max_length=128)
    difficulty = models.CharField(max_length=30, choices=DIFFICULTY_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='courses')
    status = models.SmallIntegerField(choices=STATUS, default=0)
    def __str__(self): return self.title
class Enrollment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='enrolled_in')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_users')
    enrollment_date = models.DateField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'course'], name='unique_user_course_enrollment')
        ]
class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=300, db_index=True)
    description = models.TextField()
    index = models.PositiveIntegerField()
    status = models.SmallIntegerField(choices=STATUS, default=0)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course', 'index'], name='unique_course_module_index')
        ]
    def __str__(self): return self.title
class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=300, db_index=True)
    content = RichTextUploadingField()
    index = models.PositiveIntegerField()
    status = models.SmallIntegerField(choices=STATUS, default=0)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['module', 'index'], name='unique_module_lesson_index')
        ]
    def __str__(self): return self.title
class Wishlist(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="my_wishlist")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="in_wishlist")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "course"], name="unique_user_course_in_wishlist")
        ]
class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="my_cart")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="in_cart")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "course"], name="unique_user_course_in_cart")
        ]
class Rating(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "course"], name="unique_user_course_rating")
        ] 
