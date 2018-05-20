from rest_framework import serializers
from taggit_serializer.serializers import (
    TagListSerializerField, TaggitSerializer
)

from bookmarks.models import Bookmark


class BookmarkSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    def validate_title(self, value):
        qs = Bookmark.objects.filter(title=value)
        if self.instance is None:
            # create scenario.
            if qs.count() > 0:
                raise serializers.ValidationError('Title already exists.')
        else:
            # update scenario.
            if qs.exclude(pk=self.instance.id).count() > 0:
                raise serializers.ValidationError('Title already exists.')
        return value

    def validate_link(self, value):
        qs = Bookmark.objects.filter(link=value, user=self.context['request'].user)
        if self.instance is None:
            # create scenario.
            if qs.count() > 0:
                raise serializers.ValidationError('Link already exists.')
        else:
            # update scenario.
            if qs.exclude(pk=self.instance.id).count() > 0:
                raise serializers.ValidationError('Link already exists.')
        return value

    class Meta:
        model = Bookmark
        fields = [
            'id', 'title', 'link', 'tags'
        ]
