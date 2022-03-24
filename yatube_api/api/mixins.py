from rest_framework import mixins, viewsets


class BaseViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    pass
