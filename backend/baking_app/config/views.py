from rest_framework.views import APIView
from rest_framework.response import Response

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