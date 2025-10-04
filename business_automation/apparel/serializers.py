from rest_framework import serializers
from .models import Apparel, TypeOfApparel, ColourOfApparel, SizeOfApparel, Warehouse, Pack




class ApparelSerializer(serializers.ModelSerializer):
    #pack = PackSerializer(many=True)

    class Meta:
        model = Apparel
        fields = (
            "id",
            "code_name",
            "price",
            "type",
            "colour",
            "size",
            "warehouse",
            "barcode",
            "brand",
            "date_added",
            "date_sold",
            #"pack"
        )

class PackSerializer(serializers.ModelSerializer):
    apparels = ApparelSerializer(many=True)

    class Meta:
        model = Pack
        fields = (
            "id",
            "barcode",
            "date_added",
            "date_sold",
            "price",
            "apparels"
        )

class TypeOfApparelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfApparel
        fields = (
            "id",
            "name"
        )


class ColourOfApparelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColourOfApparel
        fields = (
            "id",
            "name"
        )

class SizeOfApparelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeOfApparel
        fields = (
            "id",
            "name"
        )

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = (
            "id",
            "name"
        )

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()