from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, IntField, EmbeddedDocumentField, EmbeddedDocument


class AnotherTest(EmbeddedDocument):
    name = StringField()


class Teste(Document):
    name = StringField(unique=True)
    some_value = EmbeddedDocumentField(AnotherTest)