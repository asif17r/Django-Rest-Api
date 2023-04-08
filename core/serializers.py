from rest_framework import serializers
from .models import Breed, Dog


class BreedMaker(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class DogMaker(serializers.ModelSerializer):
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())

    class Meta:
        model = Dog
        fields = '__all__'

    def update(self, instance, validated_data):
        breed_id = validated_data.pop('breed').id
        breed = Breed.objects.get(id=breed_id)
        instance.breed = breed
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.color = validated_data.get('color', instance.color)
        instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
        instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)
        instance.save()
        return instance

    def create(self, validated_data):
        breed_id = validated_data.pop('breed').id
        breed = Breed.objects.get(id=breed_id)
        dog = Dog.objects.create(breed=breed, **validated_data)
        return dog
