from django.contrib import admin
from .models import (Category, Course, Module, Lesson, Enrollment, Cart, Wishlist, Rating)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating')
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "course")
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("user", "course")
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'difficulty', 'category', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'index', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrollment_date')
    search_fields = ('user', 'course')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('module', 'title', 'index', 'status')
    list_filter = ('status',)
    summernote_fields = ('content',)
    search_fields = ('title', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Rating, RatingAdmin)