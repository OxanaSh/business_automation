import random
from decimal import Decimal

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt import authentication

from .models import Apparel, TypeOfApparel, ColourOfApparel, SizeOfApparel, Warehouse, Pack
from .serializers import ApparelSerializer, TypeOfApparelSerializer, ColourOfApparelSerializer, SizeOfApparelSerializer, \
    WarehouseSerializer, PackSerializer
from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import LoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken


class PackView(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            pack = get_object_or_404(Pack, pk=pk)
            serializer = PackSerializer(pack)
            return Response(serializer.data)
        except Apparel.DoesNotExist:
            raise Http404

    def get(self, request):
        packs = Pack.objects.all()
        serializer = PackSerializer(packs, many=True)
        return Response(serializer.data)

    def post(self, request):
        #print(request.data)
        sizes = request.data.getlist('sizes[]')
        #apparel = ApparelSerializer(data=request.data)

        is_rand_int_unique = False
        rand_int = None

        while not is_rand_int_unique:
            rand_int = random.randint(100000000000, 999999999999)
            if Pack.objects.filter(barcode=rand_int).exists() or Apparel.objects.filter(barcode=rand_int).exists():
                is_rand_int_unique = False
            else:
                is_rand_int_unique = True


        new_pack = Pack()
        new_pack.price = Decimal(request.data.getlist('apparel.pack.price')[0])
        new_pack.barcode = rand_int
        new_pack.save()

        apparel = Apparel(
            code_name = request.data.getlist('apparel.code_name')[0],
            colour = ColourOfApparel(request.data.getlist('apparel.colour')[0]),
            size = SizeOfApparel(request.data.getlist('apparel.size')[0]),
            price = Decimal(request.data.getlist('apparel.price')[0]),
            warehouse = Warehouse(request.data.getlist('apparel.warehouse')[0]),
            brand = request.data.getlist('apparel.brand')[0],
            type = TypeOfApparel(request.data.getlist('apparel.type')[0]),
        )
        apparel.pack = new_pack

        try:
            for size in sizes:
                apparel.size = SizeOfApparel(size)
                apparel.pk = None

                is_rand_int_unique = False
                while not is_rand_int_unique:
                    rand_int = random.randint(100000000000, 999999999999)
                    if Pack.objects.filter(barcode=rand_int).exists() or Apparel.objects.filter(
                            barcode=rand_int).exists():
                        is_rand_int_unique = False
                    else:
                        is_rand_int_unique = True

                apparel.barcode = rand_int
                apparel.save()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except:
            return Response({"status": "success"}, status=status.HTTP_200_OK)

class AllApparelList(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        apparels = Apparel.objects.all()
        serializer = ApparelSerializer(apparels, many=True)
        return Response(serializer.data)

class ApparelView(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ApparelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
        apparel = Apparel.objects.get(pk=pk)
        serializer = ApparelSerializer(apparel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            apparel = get_object_or_404(Apparel, pk=pk)
            serializer = ApparelSerializer(apparel)
            return Response(serializer.data)
        except Apparel.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        try:
            apparel = Apparel.objects.get(pk=pk)
            apparel.delete()
            return Response({"status": "success"}, status=status.HTTP_204_NO_CONTENT)
        except Apparel.DoesNotExist:
            raise Http404


class TypeList(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        types = TypeOfApparel.objects.all()
        serializer = TypeOfApparelSerializer(types, many=True)
        return Response(serializer.data)

class WarehouseList(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        warehouses = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouses, many=True)
        return Response(serializer.data)


class ColourList(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        colours = ColourOfApparel.objects.all()
        serializer = ColourOfApparelSerializer(colours, many=True)
        return Response(serializer.data)


class SizeList(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        sizes = SizeOfApparel.objects.all()
        serializer = SizeOfApparelSerializer(sizes, many=True)
        return Response(serializer.data)


class ApparelType(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, type_slug, apparel_slug):
        try:
            return Apparel.objects.filter(type__slug=type_slug).get(slug=apparel_slug)
        except Apparel.DoesNotExist:
            raise Http404

    def get(self, request, type_slug, apparel_slug, format=None):
        apparel = self.get_object(type_slug, apparel_slug)
        serializer = ApparelSerializer(apparel)
        return Response(serializer.data)


class GetApparelByBarcode(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def post(self, request, barcode):
        apparel = Apparel.objects.get(barcode=barcode)
        serializer = ApparelSerializer(apparel)
        return Response(serializer.data)

class GetPackByBarcode(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def post(self, request, barcode):
        pack = Pack.objects.get(barcode=barcode)
        serializer = PackSerializer(pack)
        return Response(serializer.data)



#@api_view(['POST'])
#def get_apparel_by_barcode(barcode):
#    apparel = Apparel.objects.get(barcode=barcode)
#    serializer = ApparelSerializer(apparel)
#    return Response(serializer.data)

#@api_view(['POST'])
#def get_pack_by_barcode(request, barcode):
#    print(barcode)
#    pack = Pack.objects.get(barcode=barcode)
#    serializer = ApparelSerializer(pack)
#    return Response(serializer.data)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    })
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            except user.DoesNotExist:
                return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)