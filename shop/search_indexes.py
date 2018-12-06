from haystack import indexes
from .models import Product


class Search(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    description = indexes.CharField(model_attr='description', null=True)
    available = indexes.BooleanField(model_attr='available')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(available=True)
