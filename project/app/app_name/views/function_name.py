from . import *


class FunctionName(APIView):

    @staticmethod
    def get(request):
        value = 1
        return Response(data=value, status=status.HTTP_200_OK)
