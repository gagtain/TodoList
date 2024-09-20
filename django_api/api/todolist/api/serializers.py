from rest_framework import serializers

from todolist.models import Task, Tag


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class TagRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class TaskRetrieveSerializer(serializers.ModelSerializer):
    tag_list = TagRetrieveSerializer(many=True)
    dead_line_time = serializers.DateTimeField(format="%Y-%m-%d:%H:%M")
    created = serializers.DateTimeField(format="%Y-%m-%d:%H:%M")

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'tag_list', 'dead_line_time', 'created')


class TaskCreateSerializer(serializers.ModelSerializer):

    tag_list = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Tag.objects.all())
    telegram_id = serializers.CharField(required=False)
    dead_line_time = serializers.DateTimeField(input_formats=["%Y-%m-%d:%H:%M"])

    class Meta:
        model = Task
        fields = ('name', 'description', 'tag_list', 'dead_line_time', 'telegram_id')


    def update(self, instance, validated_data):
        tag_list = validated_data.pop('tag_list', None)

        task = super().update(instance, validated_data)

        if tag_list:
            task.tag_list.crear()
            for tag in tag_list:
                task.tag_list.add(tag)
        return task


    def create(self, validated_data):
        tag_list = validated_data.pop('tag_list')


        task = super().create(validated_data)
        for tag in tag_list:
            task.tag_list.add(tag)
        task.user = self.context['request'].user
        task.save()
        return task