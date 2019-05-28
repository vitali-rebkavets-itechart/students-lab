from rest_framework import serializers 
from comments.models import Comment 


class CommentsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Comment 
        fields = ( 
            'id', 
            'text', 
            'mark', 
            'user', 
            'product' 
        )
        