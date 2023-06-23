""" data for tests """
from song.models import Accords, Authors, Genres, SongGenres, SongLikes, Songs
from user.models import Users


class DataForTests:

    models_in_order = [
        Users,
        Genres,
        Authors,
        Accords,
        SongGenres,
        SongLikes,
        Songs
    ]

    data = {

        Users.__name__: [
            {
                'username': 'user1',
                # 'first_name': 'User1FirstName',
                # 'last_name': 'User1LastName',
                'email': 'user1@email.com',
                'password': 'Passuser1',
                'password2': 'Passuser1',
            },  {
                'username': 'user2',
                # 'first_name': 'User2FirstName',
                # 'last_name': 'User2LastName',
                'email': 'user2@email.com',
                'password': 'Pass//user2',
                'password2': 'Pass//user2',
            },  {
                'username': 'user3',
                # 'first_name': 'User3FirstName',
                # 'last_name': 'User3LastName',
                'email': 'user3@email.com',
                'password': 'Pass.user3',
                'password2': 'Pass.user3',
            },
        ],

        Genres.__name__: [
            {
                'name': 'Rock',
                'description': 'This genre encompasses various subgenres such as classic rock, hard rock, alternative rock, punk rock, and progressive rock. Guitar-driven bands and iconic guitar solos are a defining characteristic of rock music'
            },
            {
                'name': 'Blues',
                'description': 'Originating from African-American communities in the United States, blues music heavily relies on the guitar. It often features soulful playing, bending of notes, and expressive solos'
            },
            {
                'name': 'Jazz',
                'description': 'Jazz music incorporates improvisation and complex harmonies. The guitar plays a significant role in jazz, both as a rhythm instrument and for soloing. Subgenres like gypsy jazz and smooth jazz also have distinct guitar styles'
            },
            {
                'name': 'Country',
                'description': 'Country music often features acoustic and electric guitars, including fingerpicking and twangy guitar sounds. It encompasses subgenres like traditional country, country rock, and outlaw country'
            },
            {
                'name': 'Metal',
                'description': 'Known for its heavy sound, aggressive riffs, and fast guitar playing, metal music is characterized by distorted guitars and intricate solos. Subgenres like thrash metal, heavy metal, and power metal are all guitar-driven'
            },
        ],

        Authors.__name__: [
            {
                'name': 'Johnny Cash',
                'link': 'https://en.wikipedia.org/wiki/Johnny_Cash'
            },
            {
                'name': 'The Beatles',
                'link': 'https://sh.wikipedia.org/wiki/The_Beatles'
            },
            {
                'name': 'Чёрный Обелиск',
                'link': 'https://ru.wikipedia.org/wiki/%D0%A7%D1%91%D1%80%D0%BD%D1%8B%D0%B9_%D0%9E%D0%B1%D0%B5%D0%BB%D0%B8%D1%81%D0%BA_(%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%B0)'
            },
        ],

        Accords.__name__: [
            {
                'name': 'A major',
                'short_name': 'A',
                'link': 'https://www.audiolisted.com/wp-content/uploads/2018/04/A-Major-Chord-Open-Finger-Numbers.jpg.webp'
            },
            {
                'name': 'E9',
                'short_name': 'E9',
                'link': 'https://www.audiolisted.com/wp-content/uploads/2018/04/E-9-Chord-7th-Fret-5th-String-Root-1.jpg.webp'
            },
            {
                'name': 'E minor',
                'short_name': 'Em',
                'link': 'https://www.audiolisted.com/wp-content/uploads/2018/04/E-Minor-Chord-Open-Finger-Numbers.jpg.webp'
            },
            {
                'name': 'G major',
                'short_name': 'G',
                'link': 'https://www.audiolisted.com/wp-content/uploads/2018/04/G-Major-Chord-Open-Finger-Numbers.jpg.webp'
            },
        ],

    }

    @staticmethod
    def fill(models: list, stop_on_model=None):
        """ fill db by data in order """

        def fill_model(model):
            try:
                for data_dict in DataForTests.data[model.__name__]:
                    new_row = model.objects.create(**data_dict)
                    new_row.save()
            except Exception as exc:
                raise Exception(
                    f'Failed to fill with test data model: {model.__name__}') from exc

        if stop_on_model:
            models = DataForTests.models_in_order

        model = None

        for model in models:
            fill_model(model)
            if not stop_on_model is None and model.__name__ == stop_on_model.__name__:
                break
        return DataForTests.data[model.__name__]

    # @staticmethod
    # def get_data_for_model(model):
    #     return DataForTests.data[model.__name__]
