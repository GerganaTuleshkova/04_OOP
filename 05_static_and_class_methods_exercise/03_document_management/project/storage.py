from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document: Document):
        if document in self.documents:
            return
        self.documents.append(document)

    def find_category_by_id(self, category_id):
        for category_obj in self.categories:
            if category_obj.id == category_id:
                return category_obj

    def edit_category(self, category_id: int, new_name:str):
        if not self.find_category_by_id(category_id):
            return
        category = self.find_category_by_id(category_id)
        category.name = new_name

    def find_topic_by_id(self, topic_id):
        for topic_obj in self.topics:
            if topic_obj.id == topic_id:
                return topic_obj

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        if not self.find_topic_by_id(topic_id):
            return
        topic = self.find_topic_by_id(topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def get_document(self, document_id):
        for document_obj in self.documents:
            if document_obj.id == document_id:
                return document_obj

    def edit_document(self, document_id: int, new_file_name: str):
        if not self.get_document(document_id):
            return
        document = self.get_document(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        if not self.find_category_by_id(category_id):
            return
        category = self.find_category_by_id(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        if not self.find_topic_by_id(topic_id):
            return
        topic = self.find_topic_by_id(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        if not self.get_document(document_id):
            return
        document = self.get_document(document_id)
        self.documents.remove(document)

    def __repr__(self):
        return "\n".join([str(d) for d in self.documents])
