from rest_framework import serializers

from . models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        

class BlogSerializer(serializers.ModelSerializer):
    #de esta forma se forman los comentarios anidados en el blog
    #se instancia la clase CommentSerializer en la clase BlogSerializer
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
        
        
        