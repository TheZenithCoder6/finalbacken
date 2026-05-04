from django.contrib import admin   
from django.urls import path, include
from django.http import HttpResponse  # ✅ Add this import
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from shop.views import ProductViewSet, topartist
from shop.auth_views import RegisterView 
from shop.auth_views import CheckAdminView 

# ✅ Add this function
def home(request):
    return HttpResponse("""
        <html>
            <head><title>Art Gallery API</title></head>
            <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
                <h1>🎨 Art Gallery API</h1>
                <p>API is running on <code>/api/</code></p>
                <p>Admin panel: <a href="/admin/">/admin/</a></p>
                <hr>
                <h3>Available Endpoints:</h3>
                <ul style="display: inline-block; text-align: left;">
                    <li><code>GET /api/products/</code> - Get all products</li>
                    <li><code>POST /api/products/</code> - Add new product</li>
                    <li><code>POST /api/login/</code> - User login</li>
                    <li><code>POST /api/register/</code> - User signup</li>
                    <li><code>GET /api/check-admin/</code> - Check admin status</li>
                    <li><code>GET /api/topartist/</code> - Get top artists</li>
                </ul>
            </body>
        </html>
    """)

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', home),  # ✅ Add this line (root URL)
    path('admin/', admin.site.urls),   
    path('api/', include(router.urls)),
    path('api/topartist/', topartist),
    path('api/check-admin/', CheckAdminView.as_view(), name='check_admin'), 
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
]