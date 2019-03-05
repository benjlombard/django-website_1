from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date

# creates a global connection to elastic search
connections.create_connection()


# defines what needs to index in elastic search
class PostsIndex(DocType):
    #author = Text()
    title = Text()
    body = Text()
    publish = Date()

    class Index:
        # name of index. Will be used in search
        name = 'posts-index'