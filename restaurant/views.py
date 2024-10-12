from django.shortcuts import render
from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request, "index.html")


class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
