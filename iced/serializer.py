from rest_framework import serializers
from .models import KonnectDetails

class KonnectSerializer(serializers.ModelSerializer):
	class Meta:
		model=KonnectDetails
		fields=('name','county','specialisation')