import csv
from rest_framework.decorators import api_view

from django.http import HttpResponse
from product.models import Product
from django.db.models import Q
from rest_framework.views import APIView
from product.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status


def importData(request):

    permission_classes = []

    a = 0
    with open("cleanData.csv", "r", encoding="utf8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(a)
            Product.objects.create(
                Name=row["Name"],
                Brand=row["Brand"],
                Slug=row["Slug"],
                Sell=row["Sell"],
                Star=row["Star"],
                Pack=row["Pack"],
                Price=row["Price"],
                Image=row["Img"],
                Category=row["Category"],
                InternalMemory=row["InternalMemory"],
                Ram=row["RAM"],
                Screen=row["Screen"],
                Networks=row["CommunicationNetworks"],
                PictureRes=row["PictureRes"],
                InStockColor=row["InStockColor"],
                Waranti=row["Waranti"],
                InStock=row["Instock"],
                Count=row["Count"],
                ProductId=row["Productid"],
                Description=row["Description"],
                DisplayType=row["Displaytype"],
                Refreshrate=row["Maximumrefreshrate"],
                Resolation=row["Resolution"],
                Pixeldensity=row["Pixeldensity"],
                AspectRatio=row["Aspecratio"],
                Screentobodyratio=row["Screentobodyratio"],
                HDR=row["HDR"],
                Maximumbrightness=row["Maximumbrightness"],
                OtherDisplay=row["Otherdisplay"],
                SpeakerType=row["Speakertype"],
                Jack=row["Jak3.5"],
                AudioFeatures=row["Audiofeatures"],
                ModelNumbers=row["Modelnumbers"],
                PriceRelease=row["Pricerelease"],
                Announced=row["Announced"],
                Supplystatus=row["Supplystatus"],
                Releasedate=row["Releasedate"],
                SAR=row["SAR"],
                SAREU=row["SAR EU"],
                Os=row["OS"],
                OsInRelease=row["Osinrelease"],
                Descriptionos=row["Descriptionos"],
                Dimensions=row["Dimensions"],
                Weight=row["weight"],
                Backmaterial=row["Backmaterial"],
                Frontmaterial=row["Frontmaterial"],
                Framematerial=row["Framematerial"],
                Colors=row["Colors"],
                Chipmodel=row["Chipmodel"],
                Chipprocess=row["Chipprocess"],
                Numbercores=row["Numbercores"],
                Coredetails=row["Coredetails"],
                GPU=row["GPU"],
                Specificationschip=row["Specificationschip"],
                Storageram=row["Storageram"],
                Rams=row["Rams"],
                Storages=row["Storages"],
                Storagetype=row["Storagetype"],
                Microsd=row["Microsd"],
                Typemicrosd=row["Typemicrosd"],
                Rearcameraconfiguration=row["Rearcameraconfiguration"],
                Maincamera=row["Maincamera"],
                Descriptionmaincamera=row["Descriptionmaincamera"],
                Secondcamera=row["Secondcamera"],
                Descriptionsecondcamera=row["Descriptionsecondcamera"],
                Thirdcamera=row["Thirdcamera"],
                Descriptionthirdcamera=row["Descriptionthirdcamera"],
                Maximumvideores=row["Maximumvideores"],
                Resoltionvideo=row["Resoltionvideo"],
                Filmingdescription=row["Descriptionmaincamera"],
                Frontmaincamera=row["Frontmaincamera"],
                Frontdescriptionmaincamera=row["Frontdescriptionmaincamera"],
                Maximumfrontvideores=row["Maximumfrontvideores"],
                Resoltionfrontvideo=row["Resoltionfrontvideo"],
                Descriptionvideofront=row["Descriptionvideofront"],
                Batterycapacity=row["Batterycapacity"],
                Batterycapacityclass=row["Batterycapacityclass"],
                Batterytype=row["Batterytype"],
                ReplaceableBattery=row["Replaceable battery"],
                Maxchargingpower=row["Maxchargingpower"],
                Fastchargesupport=row["Fastchargesupport"],
                Wirelesscharge=row["Wirelesscharge"],
                Maxwirelesschargingpower=row["Maxwirelesschargingpower"],
                Batteryfeatures=row["Batteryfeatures"],
                Timeforcharging=row["Timeforcharging"],
                Connectionport=row["Connectionport"],
                Otgsupport=row["Otgsupport"],
                Sensors=row["Sensors"],
                Sensorstype=row["Sensorstype"],
                WiFi=row["WiFi"],
                Desciptionwifi=row["Desciptionwifi"],
                Bluetooth=row["Bluetooth"],
                Bluetoothdescription=row["Bluetoothdescription"],
                Communicationtechnology=row["Communicationtechnology"],
                support5g=row["support5g"],
                Simcard=row["Simcard"],
                Gps=row["Gps"],
            )
            a = a + 1
    return HttpResponse("Data insert is Succesful")


class LatestProductsList(APIView):

    permission_classes = []

    def get(self, request, format=None):
        products = Product.objects.all()[:7]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryProduct(APIView):

    permission_classes = []

    def get(self, request, category):
        products = Product.objects.filter(Q(Brand=category))[:7]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SellProduct(APIView):

    permission_classes = []

    def get(self, request):
        products = Product.objects.all()[:7]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductSlug(APIView):

    permission_classes = []

    def get(self, request, product_slug):
        products = Product.objects.get(Slug=product_slug)
        serializer = ProductSerializer(products)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BestSell(APIView):

    permission_classes = []

    def get(self, request):
        products = Product.objects.all()[2:7]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllProduct(APIView):

    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import (
    ProductSerializer,
)  # Assuming ProductSerializer is defined elsewhere
from .models import Product  # Assuming Product model is defined elsewhere


class ProductsFilter(APIView):
    permission_classes = []

    def post(self, request):
        filters = {}

        try:
            in_stock = request.data.get("inStock", None)
            brand = request.data.get("brand", None)
            ram = request.data.get("ram", None)
            internal = request.data.get("internal", None)
            price_min = request.data.get("min", None)
            price_max = request.data.get("max", None)
        except KeyError:
            return Response(
                {"error": "Missing required filter parameters"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if in_stock is not None:
            filters["InStock"] = in_stock
        if brand is not None:
            filters["Brand"] = brand
        if ram is not None:
            filters["Ram"] = ram
        if internal is not None:
            filters["InternalMemory"] = internal
        if price_min is not None and price_max is not None:
            filters["Price__range"] = (price_min, price_max)

        if not filters:
            return Response(
                {"message": "No filters provided"}, status=status.HTTP_200_OK
            )

        q_object = Q(**filters)
        products = Product.objects.filter(q_object)

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class Search(APIView):

    permission_classes = []

    def get(self, request):

        r = request.GET

        if "Category" in r:
            category = r["Category"]
            products = Product.objects.filter(Category=category)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

        if "Brand" in r:
            brand = r["Brand"]
            products = Product.objects.filter(Brand=brand)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

        if "query" in r:
            query = r["query"]
            products = Product.objects.filter(Name__icontains=query)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)
