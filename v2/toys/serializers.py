from rest_framework import serializers
from toys.models import Toy

# Taking advantage of model serializers

class ToySerializer(serializers.ModelSerializer):

    class Meta:
        model = Toy
        # specifies a tuple of string whose values indicate the field names that we want to 
        # include in the serialization.
        fields = (
            'id',
            'name',
            'description',
            'release_date',
            'toy_category',
            'was_included_in_home')
        # The new version of the ToySerializer class doesn't need to override either the create 
        # or update methods because the generic behavior provided by the ModelSerializer class 
        # will be enough in this case. The ModelSerializer superclass provides implementations 
        # for both methods. 
