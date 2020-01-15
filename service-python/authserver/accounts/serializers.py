from rest_framework import serializers
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.db.models import Q
from .models import Account
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class AccountSerializer(serializers.ModelSerializer):
    nama_lengkap = serializers.SerializerMethodField('get_nama_lengkap_')
    is_active = serializers.SerializerMethodField('get_status_')

    class Meta:
        model = Account
        fields = ('email', 'nama_lengkap', 'username', 'is_active')

    def get_nama_lengkap_(self, obj):
        return obj.get_full_name()

    def get_status_(self, obj):
        return obj.is_staff()

class AccountLoginSerializer(serializers.HyperlinkedModelSerializer):
    user_obj = None
    token = serializers.CharField(allow_blank=True,read_only=True)
    # ishout = serializers.CharField(allow_blank=True,read_only=True)
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = Account
        fields = ('email','password','token')
        extra_kwargs = {'password': 
                            {'write_only': True},
                            }

    def validate(self, data):
        email = data.get("email", None)
        password = data["password"]
        request = self.context.get('request')
        if not email:
            raise ValidationError("Alamat email harus di isi")

        user = Account.objects.filter(Q(email=email)).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Alamat email yang anda masukkan tidak terdaftar")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Password yang anda masukkan salah")
            payload = jwt_payload_handler(user_obj)
            token = jwt_encode_handler(payload)


        data["token"] = token
        return data