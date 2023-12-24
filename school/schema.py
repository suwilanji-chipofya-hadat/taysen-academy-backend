import graphene
from itertools import chain
from graphene_django import DjangoObjectType
from .models import (Category, Course, Module, Enrollment, Lesson, Wishlist, Cart, Rating)
from sys_management.schema import InstructorType
from sys_management.models import Instructor
from django.db.models import Q
from utils.recommendations import train_user_to_user_recommendation_model
import pandas as pd
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
class CourseType(DjangoObjectType):
    class Meta:
        model = Course
class ModuleType(DjangoObjectType):
    class Meta:
        model = Module
class EnrollmentType(DjangoObjectType):
    class Meta:
        model = Enrollment
class LessonType(DjangoObjectType):
    class Meta:
        model = Lesson

class WishlistType(DjangoObjectType):
    class Meta:
        model = Wishlist

class CartType(DjangoObjectType):
    class Meta:
        model = Cart

class SearchResultType(graphene.Union):
    class Meta:
        types = (CourseType, InstructorType, CategoryType)
class RatingType(DjangoObjectType):
    class Meta:
        model = Rating
class Query(graphene.ObjectType):

    categories = graphene.List(CategoryType)
    courses = graphene.List(CourseType)
    modules = graphene.List(ModuleType)
    enrollments = graphene.List(EnrollmentType, course_id=graphene.Int())
    lessons = graphene.List(LessonType)
    my_wishlist = graphene.List(WishlistType)
    my_cart = graphene.List(CartType)
    my_courses = graphene.List(EnrollmentType)
    search = graphene.List(SearchResultType, query=graphene.String())
    recommended_courses = graphene.List(CourseType, user_id=graphene.Int())
    course_by_id = graphene.Field(CourseType, id=graphene.Int())
    lesson_by_id = graphene.Field(LessonType, id=graphene.Int())
    def resolve_course_by_id(self, info, id=None):
        if id is None:
            raise Exception("Course id must be set")
        course = Course.objects.get(pk=id)
        if not course:
            raise Exception(f"Course with id {id} not found")
        return course
    def resolve_lesson_by_id(self, info, id=None):
        if id is None:
            raise Exception("Course id must be set")
        lesson = Lesson.objects.get(pk=id)
        if not lesson:
            raise Exception(f"Course with id {id} not found")
        return lesson
    def resolve_recommended_courses(self, info, user_id):
        ratings = Rating.objects.filter(user_id=user_id)
        ratings_df = pd.DataFrame.from_records(ratings.values('user_id', 'course_id', 'rating'))

        recommendation_model = train_user_to_user_recommendation_model(ratings_df)

        user_course_matrix = ratings_df.pivot_table(index='user_id', columns='course_id', values='rating', fill_value=0)

        recommended_courses = []

        # Get courses the user has rated
        user_rated_courses = user_course_matrix.loc[user_id]
        print(user_rated_courses)
        # Iterate over user's rated courses
        for course_id, rating in user_rated_courses.items():
            similar_courses = recommendation_model[course_id].sort_values(ascending=False).head(5).index
            recommended_courses.extend(similar_courses)

        # Remove courses the user has already rated
        print(recommended_courses)
        recommended_courses = set(recommended_courses) - set(user_rated_courses.index)
        
        recommended_courses = Course.objects.filter(id__in=recommended_courses)

        return recommended_courses
    def resolve_categories(self, info):
        return Category.objects.all()
    def resolve_search(self, info, query):
        if query is None or query == "":
            raise Exception("Query string empty")
        courses = Course.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
        instructors = Instructor.objects.filter(Q(user__username__icontains=query))
        categories = Category.objects.filter(Q(name__icontains=query))
        return list(chain(courses, instructors, categories))
    def resolve_courses(self, info):
        return Course.objects.filter(status=1)
    def resolve_modules(self, info):
        return Module.objects.filter(status=1)
    def resolve_enrollments(self, info, course_id=-1):
        if course_id >= 0:
            course = Course.objects.get(id=course_id)
            return Enrollment.objects.filter(course=course)
        return Enrollment.objects.all()
    def resolve_lessons(self, info):
        return Lesson.objects.filter(status=1)
    
    def resolve_my_wishlist(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not logged in")
        wishlist = Wishlist.objects.filter(user=user)
        return wishlist
    def resolve_my_cart(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not logged in")
        cart = Cart.objects.filter(user=user)
        return cart
    def resolve_my_courses(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise Exception("Not logged in")
        courses = Enrollment.objects.filter(user=user)
        return courses