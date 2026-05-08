from audio.tag import Tag
from mutagen.mp4 import MP4, MP4Cover

def m4a_itunes_convert_tag(m4a_tag) -> list[Tag]:
    if type(m4a_tag[0]) != str:
        raise
    key:str = m4a_tag[0]
    items:list = m4a_tag[1]
    match key:
        case '©nam': return [Tag('title', str(i)) for i in items]
        case '©ART': return [Tag('artist', str(i)) for i in items]
        case '©alb': return [Tag('album', str(i)) for i in items]
        case 'aART': return [Tag('album_artist', str(i)) for i in items]
        case '©gen': return [Tag('genre', str(i)) for i in items]
        case '©day': return [Tag('year', str(i)) for i in items]
        case 'trkn': return [tag for (num, total) in items for tag in (Tag('track_num',int(num)), Tag('track_total', int(total)))]
        case 'disk': return [tag for (num, total) in items for tag in (Tag('disk_num',int(num)), Tag('disk_total', int(total)))]
        case 'covr':
            picture_name = lambda i: 'cover_front' if i==0 else 'cover_back' if i==1 else 'image'
            return [Tag(picture_name(index), bytes(i)) for index, i in enumerate(items)]
        case _:
            if type(m4a_tag[1]) == list:
                return [Tag(key, i) for i in items]
            else:
                return Tag(key, m4a_tag[1])


def m4a_itunes_convert_tags(mp4: MP4) -> list[Tag]:
    res = list[Tag]()
    for m4a_tag in mp4.items():
        tags = m4a_itunes_convert_tag(m4a_tag)
        if tags == None:
            print(f"invalid {m4a_tag[0]}")
            continue
        res = res + tags
    return res
