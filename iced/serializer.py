from rest_framework import serializers
from .models import KonnectProfile

class KonnectSerializer(serializers.ModelSerializer):
	class Meta:
		model=KonnectProfile
		fields=('name','county','specialisation')