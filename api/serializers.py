from rest_framework import serializers
from shop.models import Product, ProductFeature
from account.models import ShopUser
from orders.models import Order



class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = ("name","value")




class ProductSerializer(serializers.ModelSerializer):
    #اتریبیوت  منی یعنی اینکه ما چندین فیچر و ویژگی داریم به همین دلیل مقدار آن را برابر با ترو قرار دادیم
    #اتریبیوت ریدآنلی بعنی  این سریالایز تنها قابلیت خواندن را دارد و نمیتوان آن را ویرایش کرد
    features=ProductFeatureSerializer(many=True,read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'new_price', 'features']



class ShopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = ('id', 'phone', 'first_name', 'last_name', 'address', 'is_staff', 'date_joined', 'is_active')





class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = ('phone', 'first_name', 'last_name', 'address', 'password')
        #  کد قسمت پایین برای این است  زمانی که ما ریکویست را از طریق ای پی ای میفرستیم پسوورد کاربر قابل مشاهده نباشد و پسوورد ان سکرت بماند
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = ShopUser(phone=validated_data['phone'], first_name=validated_data['first_name'],
                        last_name=validated_data['last_name'], address=validated_data['address'])
        user.set_password(validated_data['password'])
        user.save()
        return user





class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'