import graphene
from .models import Instructor
from graphene_django import DjangoObjectType

class InstructorType(DjangoObjectType):
    class Meta:
        model = Instructor

class Query(graphene.ObjectType):

    instructors = graphene.List(InstructorType)
    def resolve_instructors(self, info):
        return Instructor.objects.all()