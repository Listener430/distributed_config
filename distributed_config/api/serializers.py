from rest_framework import serializers

from config_model.models import DictConfig, DictConfigValueName, ValueName


class ValueNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValueName
        fields = ('name',)

class DictConfigSerializerReadOnly(serializers.ModelSerializer):
    value_names = ValueNameSerializer(required=True, many = True)

    class Meta:
        model = DictConfig
        exclude = ("id",) 

class DictConfigSerializerWriteOnly(serializers.ModelSerializer):
    value_names = ValueNameSerializer(many=True)

    class Meta:
        model = DictConfig
        exclude = ("id", "version", "in_use_indicator")


    def create(self, validated_data):
        value_names = validated_data.pop('value_names')
        dict_config = DictConfig.objects.create(**validated_data)
        for value_name in value_names:
            current_value_name, status = ValueName.objects.get_or_create(
                **value_name)
            DictConfigValueName.objects.create(
                value_name=current_value_name, system_name=dict_config)
        n = DictConfig.objects.filter(system_name=dict_config.system_name).count()
        DictConfig.objects.filter(id=dict_config.id).update(version = n, in_use_indicator = "active")
        DictConfig.objects.exclude(id=dict_config.id).update(in_use_indicator = "inactive") 
         
        return dict_config
