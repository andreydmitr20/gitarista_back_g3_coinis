""" data for tests """
from song.models import Accords, Authors, Genres, SongGenres, SongLikes, Songs
from user.models import Users


class DataForTests:
    models_in_order = [
        Users,
        Genres,
        Authors,
        Accords,
        Songs,
        SongGenres,
        SongLikes,

    ]

    model_by_fieldname = {
        'user_id': Users,
        'author_id': Authors,
        'song_id': Songs,
        'genre_id': Genres,
        'accord_id': Accords,
    }

    data = {

        Users.__name__: [
            {
                'username': 'user1',
                # 'first_name': 'User1FirstName',
                # 'last_name': 'User1LastName',
                'email': 'user1@email.com',
                'password': 'Passuser1',
                # 'password2': 'Passuser1',
            },  {
                'username': 'user2',
                # 'first_name': 'User2FirstName',
                # 'last_name': 'User2LastName',
                'email': 'user2@email.com',
                'password': 'Pass//user2',
                # 'password2': 'Pass//user2',
            },  {
                'username': 'user3',
                # 'first_name': 'User3FirstName',
                # 'last_name': 'User3LastName',
                'email': 'user3@email.com',
                'password': 'Pass.user3',
                # 'password2': 'Pass.user3',
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

        Songs.__name__: [
            {
                'user_id': 3,
                'author_id': 2,
                'title': 'Zapisano je u vremenu',
                'link': 'http://www.pesmarica.rs/Akordi/12796/Nedeljko-Baji%C4%87-Baja--Zapisano-je-u-vremenu',


                'text_with_accords':
                """ 
                Em ---------Am ---Em 
                Zapisano je u vremenu
                C----------D- -----Em 
                kakva je to ljubav bila
                C---------D- --------
                (kamo srece za nas dvoje
                G ----E -Am ---D- --G  (Em  2x)
                kad bi se nekom ponovila) 2x

                Zapisano je u vremenu
                da se secam, da se secas
                (rekla si mi: ''Volecu te doveka.'',
                B ja tebi: ''Nemoj da me cekas!'') 2x

                Ref. 2x
                D- -------------------Em -----------
                Zazmuri, broj do sto, to bice dovoljno
                ---D- ---------------Em -----------
                da probam nekako, da odem bezbolno
                ---D- -------------Em -----------
                ja necu voleti, posle tebe, ni u snu - 
                C--------D- ------Em 
                zapisano je u vremenu

                Zapisano je u vremenu
                da smo mnogo jaki bili
                (B gde bi nam bio kraj
                jos da smo se za ljubav borili)2x

                Zapisano je u vremenu
                plakala si, i ja s' tobom
                (i na kraju, kad si rekla: ''Volim te.'',
                teska srca rekao sam: ''Zbogom'') 2x
                """
            },
            {
                'user_id': 1,
                'author_id': 2,
                'title': 'Da si tu',
                'link': 'http://www.pesmarica.rs/Akordi/12791/Aco-Pejovi%C4%87--Da-si-tu',


                'text_with_accords':
                """ 
                Em                       D
                Iako znam da ljubav nema pravila
                Em                       D
                taj osjecaj krivice imam danima
                G 
                za grube reci sto su pale
                D
                za ruke koje nisu znale
                Am                       Hm
                da zadrze te tu na mojim vratima

                Em                         D
                Proveravam telefon svoj iz navike
                Em                           D
                za propusteni poziv tvoj bih dao sve
                G 
                zar nije vredna ljubav moja
                D
                ni poruke sa tvoga broja
                Am                        Hm
                zar mora Bog u crno da me zavije
                Hm
                Da mi je

                Ref.
                G 
                Da si tu bar noci ove
                D
                da si tu, jedino moje
                Am                   Em      (D)
                da si tu da oci dusu odmore

                G 
                Da si tu bar ovog' trena
                D
                bila bi za sva vremena
                C            D                 Em
                da si tu, pa makar i bio tvoja sena 
                """
            },
            {
                'user_id': 1,
                'author_id': 2,
                'title': 'Za ljiljanu',
                'link': 'http://www.pesmarica.rs/Akordi/12781/Toma-Zdravkovi%C4%87--Za-ljiljanu',


                'text_with_accords':
                """ 
                                Em
                Ne kosite rosnu travu
                Am
                ne lomite mladu granu
                D
                Ostavite cvetna polja
                G
                ostavite cvetna polja
                H7                  Em
                nek cvetaju za Ljiljanu
                (2x)


                Ref.
                C                  Am
                Ljubavi su mnoge bile
                D                    G
                kao vatra mladost planu
                Am           Em
                sve sto osta od zivota
                D                  G
                ja bi dao za Ljiljanu
                Am            Em
                sve sto osta od zivota
                D         H7       Em
                ja bi dao za Ljiljanu


                Ne pevajte pesme njene
                ne dirajte staru ranu
                pet godina ja negujem
                pet godina ja jos cuvam
                jednu ruzu za Ljiljanu

                Pet godina ja jos cuvam
                pet godina ja negujem
                jednu ruzu za Ljiljanu

                Ref.

                Ostvaricu snove svoje
                kada hladne kise stanu

                Kad s'prolecem ozelene
                cvetna polja za Ljiljanu
                cvetna polja za Ljiljanu
                (2x)

                Ref.

                Ja bi dao za Ljiljanu
                za Ljiljanu, za Ljiljanu
                """
            },
        ],

        SongGenres.__name__: [
            {
                'song_id': 1,
                'genre_id': 5
            },
            {
                'song_id': 1,
                'genre_id': 2
            },
            {
                'song_id': 3,
                'genre_id': 4
            },
            {
                'song_id': 3,
                'genre_id': 5
            },
            {
                'song_id': 3,
                'genre_id': 2
            },
        ],

        SongLikes.__name__: [
            {
                'song_id': 1,
                'user_id': 3
            },
            {
                'song_id': 1,
                'user_id': 2
            },
            {
                'song_id': 2,
                'user_id': 2
            },

        ],

    }
