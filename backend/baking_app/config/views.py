from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Config
from .serializers import ConfigSerializer

class ListApps(APIView):
    """
    View to list all apps in the system.

    """
    
    def get(self, request, format=None):
        """
        Return a list of all apps.
        """
        apps = ["Catelog", "Production", "Purchasing", "Recipes", "Sales"]
        return Response(apps)
    
class Company(APIView):
    """
    View to get the company name
    """

    def get(self, request, format=None):
        company_config = Config.objects.filter(item__in=["company_name", "company_tag_line"])
        serializer = ConfigSerializer(company_config, many=True)
                
        return Response(serializer.data)