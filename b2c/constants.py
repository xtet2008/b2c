# -*- coding: utf8 -*-


class TargetType:
    (ALBUM,
     ARTIST,
     SONG) = range(1, 4)

    CN = {
        ALBUM: 'album',
        ARTIST: 'artist',
        SONG: 'song',
    }


class Source:
    OFFICIAL = 'official'
    UGC = 'ugc'

    CN = {
        OFFICIAL: 'official',
        UGC: 'ugc',
    }


class Difficulty:
    (EASY,
     ADVANCE,
     ORIGINAL) = range(1, 4)

    CN = {
        EASY: 'easy',
        ADVANCE: 'advance',
        ORIGINAL: 'original',
    }


class Currency:
    (CNY,
     USD) = range(1, 3)

    CN = {
        CNY: 'CNY',
        USD: 'USD',
    }


class PopMusicType:
    (MELODY,
     PLAY_SING) = range(1, 3)

    CN = {
        MELODY: 'melody',
        PLAY_SING: 'play & sing',
    }


class PianoType:
    KEY_61 = 0
    KEY_88 = 1

    CN = {
        KEY_61: '61 key',
        KEY_88: '88 key',
    }


class Gender:
    (FEMALE,
     MALE,
     UNKNOWN) = range(3)

    CN = {
        FEMALE: 'female',
        MALE: 'male',
        UNKNOWN: 'unknown',
    }


class ResourceType:
    (XML,
     KARA,
     VIDEO,
     RUSH,
     PNG,
     ) = range(1, 6)

    CN = {
        XML: 'xml',
        PNG: 'png',
        RUSH: 'rush',
        KARA: 'kara',
        VIDEO: 'video',
    }

    MAP = {v: k for k, v in CN.items()}


class VisitType:
    (
        SCORE,
        ALBUM,
        VIDEO,  # 收藏区分视频
    ) = range(1, 4)

    CN = {
        SCORE: 'score',
        ALBUM: 'album',
    }


class PurchaseType:
    (
        XML,
    ) = range(1)

    CN = {
        XML: 'xml',
    }


class CategoryType:
    ALBUM_LEVEL_TYPE = 1
    VIDEO_LEVEL_TYPE = 2


class Region:
    CN_ONLINE = 1
    US_ONLINE = 1
    CN_OFFLINE = 0
    US_OFFLINE = 0
    ONLINE = 1
    OFFLINE = 0


class RegionStrategy:
    CN = "cn"
    US = "us"


class CopyRight:
    CN_COPYRIGHT = ["华纳", "太和"]
    OVERSEA_COPYRIGHT = ["Hal Leonard", "Alfred Music", "hoffman", "HDPiano"]


class UserGroup:
    CHINA_GROUP = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    OVERSEA_GROUP = [10, 11, 12, 13, 14]


class UserStrategyMapping:
    USER_STRATEGY = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 2, 11: 2, 12: 2, 13: 2, 14: 2}


class HeaderXPad:
    (Mobile, Pad) = range(0, 2)


class DeleteSeq:
    (DELETED,
     NORMAL) = range(0, 2)


class CollectType:
    (SCORE,
     ALBUM,
     TUTOR) = range(1, 4)


class TutorialGene:
    (SCORE,
     ALBUM) = range(1, 3)


class VersionUpdate:
    (NO, ADVICE, FORCE) = range(0, 3)


class BannerType:
    (OUTLINK,
     ALBUM,
     SCORE,
     KARA,
     VIDEO,
     RUSH,
     BEGINLIST,
     BEGINDETAIL,
     LAB,
     ) = range(-1, 8)


levels = {u"新手": 1, u"初级": 2, u"中级": 3, u"高级": 4, u"挑战": 5}

BEAT_RATE = "恭喜你刷新纪录，击败了全国{}%的人～"
BEAT_RATE_NO_HIGHEST = "你击败了全国{}%的人~"

# redis key
ALBUM_HITS_KEY = 'album_hits:{}'  # 曲集点击量
SCORE_HITS_KEY = 'score_hits:{}'  # 曲谱点击量
USER_KEY = 'user:{}'  # 用户
