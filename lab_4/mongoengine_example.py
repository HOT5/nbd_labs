
from mongoengine import *


class VideoGame(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    released = BooleanField(required=True)

    @queryset_manager
    def released_games(clazz, queryset):
        return queryset.filter(released=True)


if __name__ == '__main__':
    mongo_client = connect(db='ikol5DB', host='localhost', port=27017)

    gtaV = VideoGame(title='GTA V',
                     content='Is a 2013 action-adventure game developed by Rockstar North and published by Rockstar Games.',
                     author='Rockstar Games',
                     released=True)
    gtaVI = VideoGame(title='GTA VI',
                      content='Unknown',
                      author='Rockstar Games',
                      released=False)

    gtaV.save()
    gtaVI.save()
    print(f'Author before change {gtaV.author}')
    gtaV.author = 'Rockstar'
    gtaV.save()
    print(f'Author after change {gtaV.author}')
    video_games = VideoGame.objects
    print(f'Collection contains: {len(video_games)} documents')
    print(f'Collection contains games that is released : {len(VideoGame.released_games())} documents')