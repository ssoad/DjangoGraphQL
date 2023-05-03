import core.ingredients.schema
import core.recipes.schema
import graphene

from graphene_django.debug import DjangoDebug


class Query(
    core.ingredients.schema.Query,
    core.recipes.schema.Query,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query)
