from rest_framework import serializers
from notes.models import Notes

class NotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = '__all__'

    def validate_title(self, value):
        if len(value) > 100:
            return serializers.ValidationError("Max title length is 100 characters")
        return value    


class NoteDetailSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Notes
        fields = '__all__'

    def get_slug(self, obj):
        return obj.slug

   