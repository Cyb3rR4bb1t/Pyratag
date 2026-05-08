from audio.tag import Tag
from mutagen.mp3 import MP3
from mutagen.id3._specs import PictureType, ID3TimeStamp
from mutagen.id3._frames import (AENC, APIC, ASPI, BUF, CHAP, CNT, COM, COMM, COMR, CRA,
    CRM, CTOC, ENCR, EQU2, ETC, ETCO, GEO, GEOB, GP1, GRID, GRP1, IPL, IPLS,
    LINK, LNK, MCDI, MCI, MLL, MLLT, MVI, MVIN, MVN, MVNM, OWNE, PCNT, PCST,
    PIC, POP, POPM, POSS, PRIV, RBUF, REV, RVA, RVA2, RVAD, RVRB, SEEK, SIGN,
    SLT, STC, SYLT, SYTC, TAL, TALB, TBP, TBPM, TCAT, TCM, TCMP, TCO, TCOM,
    TCON, TCOP, TCP, TCR, TDA, TDAT, TDEN, TDES, TDLY, TDOR, TDRC, TDRL, TDTG,
    TDY, TEN, TENC, TEXT, TFLT, TFT, TGID, TIM, TIME, TIPL, TIT1, TIT2, TIT3,
    TKE, TKEY, TKWD, TLA, TLAN, TLE, TLEN, TMCL, TMED, TMOO, TMT, TOA, TOAL,
    TOF, TOFN, TOL, TOLY, TOPE, TOR, TORY, TOT, TOWN, TP1, TP2, TP3, TP4, TPA,
    TPB, TPE1, TPE2, TPE3, TPE4, TPOS, TPRO, TPUB, TRC, TRCK, TRD, TRDA, TRK,
    TRSN, TRSO, TS2, TSA, TSC, TSI, TSIZ, TSO2, TSOA, TSOC, TSOP, TSOT, TSP,
    TSRC, TSS, TSSE, TSST, TST, TT1, TT2, TT3, TXT, TXX, TXXX, TYE, TYER, UFI,
    UFID, ULT, USER, USLT, WAF, WAR, WAS, WCM, WCOM, WCOP, WCP, WFED, WOAF,
    WOAR, WOAS, WORS, WPAY, WPB, WPUB, WXX, WXXX)
from datetime import datetime

def mp3_create_text_tags(name, value_object) -> list[Tag]:
    if 'text' not in value_object:
        raise
    return [Tag(name, v) for v in value_object['text']]

def mp3_create_binary_tags(name, value_object) -> list[Tag]:
    if 'data' not in value_object:
        raise
    return [ Tag(name, bytes(value_object['data'])) ]

def mp3_create_integer_range_first_item_tags(name, value_object) -> list[Tag]:
    if 'text' not in value_object:
        raise
    tags: list[Tag] = []
    for v in value_object['text']:
        numbers = v.split('/')
        if not (1 <= len(numbers) <= 2):
            continue
        tags.append( Tag(name, int(numbers[0])) )
    return tags

def mp3_create_integer_range_second_item_tags(name, value_object) -> list[Tag]:
    if 'text' not in value_object:
        raise
    tags: list[Tag] = []
    for v in value_object['text']:
        numbers = v.split('/')
        if len(numbers) != 2:
            continue
        tags.append( Tag(name, int(numbers[1])) )
    return tags

def mp3_tag_to_picture(value_object) -> list[Tag]:
    picture_type: PictureType = value_object['type']
    if picture_type == PictureType.COVER_FRONT:
        return mp3_create_binary_tags('cover_front', value_object)
    if picture_type == PictureType.COVER_BACK:
        return mp3_create_binary_tags('cover_back', value_object)
    return mp3_create_binary_tags(f'APIC({picture_type.value})', value_object)

def mp3_tag_to_title(value_object) -> list[Tag]:
    return mp3_create_text_tags('title', value_object)

def mp3_tag_to_artist(value_object) -> list[Tag]:
    return mp3_create_text_tags('artist', value_object)

def mp3_tag_to_album(value_object) -> list[Tag]:
    return mp3_create_text_tags('album', value_object)

def mp3_tag_to_album_artist(value_object) -> list[Tag]:
    return mp3_create_text_tags('album_artist', value_object)

def mp3_tag_to_genre(value_object) -> list[Tag]:
    return mp3_create_text_tags('genre', value_object)

def mp3_tag_to_year(value_object) -> list[Tag]:
    if 'text' not in value_object:
        raise
    tags = []
    for v in value_object['text']:
        time_stamp: ID3TimeStamp = v
        tags.append( Tag('year', datetime.strptime(time_stamp.text, "%Y-%m-%d").year) )
    return tags

def mp3_tag_to_track_num(value_object) -> list[Tag]:
    return mp3_create_integer_range_first_item_tags('track_num', value_object)

def mp3_tag_to_track_total(value_object) -> list[Tag]:
    return mp3_create_integer_range_second_item_tags('track_total', value_object)

def mp3_tag_to_disk_num(value_object) -> list[Tag]:
    return mp3_create_integer_range_first_item_tags('disk_num', value_object)

def mp3_tag_to_disk_total(value_object) -> list[Tag]:
    return mp3_create_integer_range_second_item_tags('disk_total', value_object)

def mp3_tag_to_normalized_tag(key, value_object) -> list[Tag]:
    if 'text' in value_object:
        if type(value_object['text']) == str:
            return [Tag(key, value_object['text'])]
        return mp3_create_text_tags(key, value_object)
    if 'data' in value_object:
        return mp3_create_binary_tags(key, value_object)
    return []

def mp3_convert_tag(mp3_tag:tuple) -> list[Tag]:
    if type(mp3_tag[0]) != str:
        raise
    key = mp3_tag[0]
    data = mp3_tag[1].__dict__
    match mp3_tag[1]:
        case APIC(): return mp3_tag_to_picture(data)
        case TIT2(): return mp3_tag_to_title(data)
        case TPE1(): return mp3_tag_to_artist(data)
        case TALB(): return mp3_tag_to_album(data)
        case TPE2(): return mp3_tag_to_album_artist(data)
        case TCON(): return mp3_tag_to_genre(data)
        case TDRC(): return mp3_tag_to_year(data)
        case TRCK(): return mp3_tag_to_track_num(data) + mp3_tag_to_track_total(data)
        case TPOS(): return mp3_tag_to_disk_num(data) + mp3_tag_to_disk_total(data)
        case _: return mp3_tag_to_normalized_tag(key, data)

def mp3_convert_tags(mp3: MP3) -> list[Tag]:
    res = list[Tag]()
    for mp3_tag in mp3.items():
        tags = mp3_convert_tag(mp3_tag)
        if tags == None:
            print(f"invalid {mp3_tag[0]}")
            continue
        res = res + tags
    return res
