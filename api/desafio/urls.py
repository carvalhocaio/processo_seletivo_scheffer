from rest_framework import routers
from .views import FazendaViewSet, AlgodoeiraViewSet, MovimentoViewSet, EstoqueViewSet

route = routers.DefaultRouter(trailing_slash=True)
route.register('fazendas', FazendaViewSet)
route.register('algodoeira', AlgodoeiraViewSet)
route.register('movimentos', MovimentoViewSet)
route.register('estoques', EstoqueViewSet)

urlpatterns = route.urls
