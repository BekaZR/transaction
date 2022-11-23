from rest_framework import serializers, exceptions

from mainapp.models import User,Payment


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ("id", "username", "password", "balance")
        read_only_fields = ("balance", )
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("id", "payor", "payee", "amount", "created_at")
        read_only_fields = ("created_at", )
    
    def create(self, validated_data):
        payor = validated_data.get("payor", None)
        payee = validated_data.get("payee", None)
        amount = validated_data.get("amount", None)
        
        if payor.balance < amount:
            raise exceptions.ValidationError(
                {"Value error": "There are not enough funds on your balance"}
            )
        payor.balance -= amount
        payor.save()
        
        payee.balance += amount
        payee.save()
            
        payment = Payment.objects.create(**validated_data)
        return payment
        