from django.db.models import QuerySet


class TaskQuerySet(QuerySet):


    def detail(self, **filters):

        qs = self.prefetch_related('tag_list').select_related('user')

        return qs.filter(**filters)