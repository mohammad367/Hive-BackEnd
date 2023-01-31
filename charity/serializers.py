from rest_framework import serializers
from charity.models import Advertisement , DonatorDonate

class AdvertisementSerializer(serializers.ModelSerializer):
    '''getting list of advertimsements and creating post new advertisement'''
    serializer_class = AdvertisementSerializer
    def get(self,request):
        '''retreive a list of ads'''
        if request.method == "GET":
            ads = Advertisement.objects.get(pk = id)
            serializer = AdvertisementSerializer(ads, many=True)
            return Response(serializer.data)
        def post(self,request):
            '''creating a new ad with provided data'''
            serializer = AdvertisementSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    
# description
# raiser
# amount
# collected_amount
# ...

class DonatorDonateSerializer(serializers.ModelSerializer):
    serializer_class = DonatorDonateSerializer
    def get(self,request):
        
        if request.method == "GET":
            donator = DonatorDonate.objects.get(pk = id)
            serializer = DonatorDonateSerializer(donator, many=True)
            return Response(serializer.data)
        def post(self,request):
            
            donator = DonatorDonateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)