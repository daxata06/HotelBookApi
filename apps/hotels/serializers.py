from rest_framework import serializers
from .models import Country, City, Hotel


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False)

    class Meta:
        model = City
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    location = CitySerializer(many=False)

    def create(self, validated_data):
        if (
            Country.objects.filter(
                name=validated_data["location"]["country"]["name"]
            ).exists()
            is False
        ):
            Country.objects.create(name=validated_data["location"]["country"]["name"])
        if (
            City.objects.filter(name=validated_data["location"]["name"]).exists()
            is False
        ):
            City.objects.create(
                name=validated_data["location"]["name"],
                country=Country.objects.filter(
                    name=validated_data["location"]["country"]["name"]
                ).first(),
            )
        validated_data["location"] = City.objects.filter(
            **validated_data["location"]
        ).first()

        try:
            return Hotel.objects.create(**validated_data)
        except:  # noqa
            raise serializers.ValidationError(
                "Hotel you are trying to add already exists"
            )

    class Meta:
        model = Hotel
        fields = "__all__"
