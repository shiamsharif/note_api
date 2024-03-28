from rest_framework.viewsets import ModelViewSet

from Note.models import Note
from Note.serializers import NoteSerializer

class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    