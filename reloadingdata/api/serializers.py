from mydata.models import Gun, Bullet, TestResult, Velocity
from rest_framework import serializers



class VelocitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Velocity
        fields = '__all__'

class TestResultSerializer(serializers.ModelSerializer):
    velocity = VelocitySerializer(many=True)

    class Meta:
        model = TestResult
        fields = ['pk', 'charge', 'moa', 'date_added', 'velocity']


class BulletSerializer(serializers.ModelSerializer):
    results = TestResultSerializer(many=True)

    class Meta:
        model = Bullet
        fields = ['pk', 'bullet', 'powder', 'date_added', 'results']

class GunSerializer(serializers.ModelSerializer):
    bullets = BulletSerializer(many=True)

    class Meta:
        model = Gun
        fields = ['pk', 'gun', 'date_added', 'owner', 'bullets']