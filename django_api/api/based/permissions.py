from django.core.cache import cache
from django.conf import settings

from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from based.exceptions.CodeDataException import CodeDataException


class ManyToSeedUser(IsAuthenticated):

    def has_permission(self, request, view):
        res = super().has_permission(request, view)

        if not res:
            return res

        key = f'user_{request.user.id}_seed'
        if request.user.username == 'bot':
            if request.GET.get('tg_id'):
                key = key + '_' + str(request.GET.get('tg_id'))
            elif request.data.get('telegram_id'):
                key = key + '_' + str(request.data.get('telegram_id'))
            else:
                return True
        count_seed = cache.get(key, 0)
        if count_seed > settings.COUNT_SEED:
            raise CodeDataException("too many seed", status.HTTP_429_TOO_MANY_REQUESTS)
        else:
            count_seed += 1
            cache.set(key, count_seed, 60)

            return True
