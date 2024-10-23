from artists import *

if __name__ == "__main__":
    f = open("data.txt", "a+") # create new file if not exists

    token = get_token()

    while True:
        print(
            "\nPress the following options:\n0. Exit\n1. Artist"
        )

        option = int(input())
        if (option == 1):
            
            print("Type the name of the artist: ")
            name = input()
            result = search_for_artist(name, token)
            artist_id = result["id"]
            f.write(f"Artist: {name}\n")

            print("\nPress the following:\n0.Exit\n1.Songs.\n2.Albuns.")
            inner_option_2 = input()

            if (inner_option_2 == "1"):
                songs = get_songs_by_artists(artist_id, token)
                for idx, song in enumerate(songs):
                    print(f"{idx + 1} : {song['name']}")
                    f.write(f" * {song['name']}\n")
                f.write("\n")

            elif (inner_option_2 == "2"):
                albums = get_albuns_by_artists(artist_id, token)
                for idx, album in enumerate(albums):
                    print(f"{idx + 1} : {album['name']}")
                    f.write(f" * {album['name']}\n")
                f.write("\n")

            else: break
        else: break
    
    f.close()