from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test Api Vies """
    def get(self,request,format=None):

        """ returns a list of api view features"""
        an_apiview = [
        'Uses Http methods as function(get,post,patch,put,delete)',
        'is similar to a traditional django view',
        'gives you the most control over your application logic',
        'is mapped mannually to Urls'
        ]
        return Response({'message':'hello!','an_apiview':an_apiview})
