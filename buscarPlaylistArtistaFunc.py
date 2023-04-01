def playlists_por_artista(artista, db):

    playlists = db['playlists']
    musicas = db['musicas']

    musicas_do_artista = [m['nome'] for m in musicas if m['artista'] == artista]

    playlists_do_artista = []
    for playlist in playlists:
        if set(musicas_do_artista).intersection(set(playlist['musicas'])):
            playlists_do_artista.append(playlist)

    return playlists_do_artista