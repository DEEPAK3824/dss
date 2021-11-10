from rest_framework import serializers
from rest_framework import Topics, Folders,Documents

class dssSerializers(Serializers.ModelSerializer):
    class Meta:
        model=Documents
        fields=('Documents')
        model = Folders
        fields = ('Folders')
        model = Topics
        fields = ('Topics')
    fields- '__all__'