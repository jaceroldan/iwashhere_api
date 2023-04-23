import ast

from django.views import View
from django.http import HttpResponse

import pandas as pd

from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import CustomerSerializer, OrderSerializer

from api.models import Customer, Order

class CustomerViewSet(viewsets.ModelViewSet):
    """
    /api/customers/
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """
    /api/orders/
    """

    queryset = Order.objects.all() 
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return Response()


class DarienRecommenderView(View):
    def get(self, request):
        categories = ['Fiction', 'Comics & Graphic Novels', 'Comedy', 'Biography & Autobiography', 'Cooking']
        authors = ['Neal Stephenson', 'Bill Watterson', 'Harpo Marx', 'John Perkins']

        book_data = pd.read_csv('./api/fixtures/books_data.csv')

        # Ensure that the response has an image
        book_data = book_data[book_data['image'].isna() == False]

        # Ensure that the response has a category
        book_data = book_data[book_data['categories'].isna() == False]

        # Ensure that the response has an author
        book_data = book_data[book_data['authors'].isna() == False]

        book_data['first_category'] = book_data['categories'].apply(lambda x: ast.literal_eval(x)[0])

        book_data['first_author'] = book_data['categories'].apply(lambda x: ast.literal_eval(x)[0])

        # Match categories
        categories_book_data = book_data[book_data['first_category'].isin(categories) == True]

        # Match authors
        authors_book_data = book_data[book_data['first_author'].isin(authors) == True]

        # combined dataset
        filtered_book_data = pd.concat([categories_book_data, authors_book_data])

        sample = filtered_book_data.sample().to_json()
        return HttpResponse(sample)

