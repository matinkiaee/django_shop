from shop.models import Product
from orders.models import Order
from .serializers import *
from rest_framework import generics
from rest_framework import views
from account.models import ShopUser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets
from rest_framework.decorators import action
from .permissions import IsAdminTabriz, IsBuyer


# Create your views here.
#این فایل ویو یک ویو معمولی نیست که ما یک ریکویست را بگیریم و یک ریسپانس دریافت کنیم  به همین  دلیل ویو هایمان را باکلاس ها مینویسیم
#چون در  "ای پی آی " ما یک ریکویست را از سرور دریافت میکنیم و به کلاینت ریسپانس می دهیم و بلعکس


#مفهوم "سریالایز کردن" یعنی تبدیل یک سری داده های پیچیده به دیکشنری پایتون
#مفهوم "دی سریالایز کردن" یعنی تبدیل دیکشنری های پایتون به یکسری داده های پیچیده
#مفهوم رندر کردن یعنی دیکشنری های پایتون را به فایل جیسون تبدیل میکند
#مفهوم پارس کردن یعنی فایل جیسون را به دیکشنری های پایتون تبدیل میکند




#و لیست ای پی ای ویو هم صرفا برای اینکه بخاهیم لیستی از یک ابجکت را داشته باشیم ازش استفاه می کنیم 
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer



# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer



#ویو ست ها از جنریک ها ارث بری نمی کنند 
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['GET'], url_path="all_discount_products", url_name="all_discount_products",
        permission_classes=[IsAuthenticated])
        # معنی این تابع زیر یعنی محصولات تخفیف دار 
    def discount_products(self, request):
        #       هم یعنی تخفیف off         جی تی مخخف great than 
        products = self.queryset.filter(off__gt=0)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)



class UserListAPIView(views.APIView):
    #اوتنتیکیشن کلاس هم به معنی نوع احراز هویت می باشد که ما میتوانیم نوع ان را مشخص کنیم 
    authentication_classes = [BasicAuthentication]
    #پرمیشن کلاس به معنی سطح دسرسی کاربر میباشد که در این قسمت سطح دسرسی به کسانی تعلق میگیرد که احراز هویت کرده باشند
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = ShopUser.objects.all()
        serializer = ShopUserSerializer(users, many=True)
        return Response(serializer.data)
    


#کریت ای پی ای ویو یک نوع جنریک است که برای ایجاد و ساخت چیزی استفاده می شود و چون کلاس ما رجیستر است و رجیستر هم باید صرفا ابجکتی را ایجاد کند  از این جنریک استفاده می شود
class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = ShopUser.objects.all()
    serializer_class = UserRegistrationSerializer




#و لیست ای پی ای ویو هم صرفا برای اینکه بخاهیم لیستی از یک ابجکت را داشته باشیم ازش استفاه می کنیم 
class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminTabriz]


#و اما رتریو ای پی آی ویو هم زمانی استفاده میشود که ما بخواهیم جزعیات یک ابجکت را دریافت کنیم 
#به منظور دریافت یک آیتم خاص طراحی شده‌اند
class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsBuyer]


