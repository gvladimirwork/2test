from haystack import indexes
from homepage.models import Item



class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(use_template=True, document=True)
    name = indexes.CharField(model_attr='name')
    comment = indexes.CharField(model_attr='comment')
    price = indexes.CharField(model_attr='price')

    def get_model(self):
        return Item

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

