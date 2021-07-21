from mydata.models import Gun, Bullet, TestResult, Velocity
from rest_framework import serializers

class VelocitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Velocity
        fields =  ['pk', 'shotnumber', 'velocity', 'date_added']


class TestResultSerializer(serializers.ModelSerializer):
    velocity = VelocitySerializer(many=True)

    class Meta:
        model = TestResult
        fields = ['pk', 'charge', 'moa', 'date_added', 'velocity']

    def update(self, instance, validated_data):
        velocities_data = validated_data.pop('velocity')
        velocities = (instance.velocity).all()
        velocities = list(velocities)

        instance.charge = validated_data.get('charge', instance.charge)
        instance.moa = validated_data.get('moa', instance.moa)
        instance.save()

        for velocity_data in velocities_data:
            velocity = velocities.pop(0)
            velocity.velocity = velocity_data.get('velocity', velocity.velocity)
            velocity.save()

        return instance

    def create(self, validated_data):
        velocities_data = validated_data.pop('velocity')
        result = TestResult.objects.create(bullet=self.context['bullet'], **validated_data)
        for velocity_data in velocities_data:
            Velocity.objects.create(result=result, **velocity_data)
        return result


class BulletSerializer(serializers.ModelSerializer):
    results = TestResultSerializer(many=True)

    class Meta:
        model = Bullet
        fields = ['pk', 'bullet', 'powder', 'primer', 'coal', 'landTotal', 'landOffset', 'date_added', 'results']


class GunSerializer(serializers.ModelSerializer):
    bullets = BulletSerializer(many=True)

    class Meta:
        model = Gun
        fields = ['pk', 'gun', 'date_added', 'owner', 'bullets']