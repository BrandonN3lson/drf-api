# from django.http import Http404
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Profile
# from .serializers import ProfileSerializer
# from drf_api.permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

# class ProfileList(APIView):
#     """
#     List all post
#     No Create view (post method), as profile creation handled by django
#     signals
#     """
#     def get(self, request):
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles,
#                                        many=True,
#                                        context={'request': request}
#                                        )
#         return Response(serializer.data)


# class ProfileDetail(APIView):
#     serializer_class = ProfileSerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         try:
#             profile = Profile.objects.get(pk=pk)
#             self.check_object_permissions(self.request, profile)
#             return profile
#         except Profile.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(
#                                        profile,
#                                        context={'request': request})
#         return Response(serializer.data)

#     def put(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile,
#                                        data=request.data,
#                                        context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST
#                         )
