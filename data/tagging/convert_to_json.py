import sqlite3
import csv
import unicodedata
import json
class TaggingDbConn:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)

    def get_data(self, table, limit = 10):
        query = (
            'SELECT * '
            'FROM {0} '.format(table)
        )
        if limit is not None:
            query +=  'LIMIT {0}'.format(limit)
        x = self.conn.execute(query).fetchall()
        return x


TaggingDb = TaggingDbConn('leduythuccs.github.io/data/tagging/tagging.db')
def convert_to_json():
    #shortlink, tag, discord_id
    tagged = TaggingDb.get_data('tagged', limit=None)
    problems = {}
    user_tagged = {}
    for p, tag, discord_id in tagged:
        if p not in problems:
            problems[p] = {}
        discord_id = str(discord_id)
        if discord_id not in problems[p]:
            problems[p][discord_id] = {'tags': [], 'comments': []}
        problems[p][discord_id]['tags'].append(tag)
        
        if discord_id not in user_tagged:
            user_tagged[discord_id] = set()
        user_tagged[discord_id].add(p)

    commented = TaggingDb.get_data('commented', limit=None)
    for p, comment, discord_id in commented:
        if p not in problems:
            problems[p] = {}
        discord_id = str(discord_id)
        if discord_id not in problems[p]:
            problems[p][discord_id] = {'tags': [], 'comments': []}
        problems[p][discord_id]['comments'].append(comment)
        
        if discord_id not in user_tagged:
            user_tagged[discord_id] = set()
        user_tagged[discord_id].add(p)
    for x in user_tagged:
        user_tagged[x] = list(user_tagged[x])
    
    cnt = {}
    for p in problems:
        for discord_id in problems[p]:
            discord_id = str(discord_id)
            if discord_id not in cnt:
                cnt[discord_id] = 0
            cnt[discord_id] += 1
    rank_info = []
    for discord_id, cnt_t in cnt.items():
        rank_info.append((cnt_t, str(discord_id)))
    rank_info.sort(reverse=True)
    tmp = {}
    for x in rank_info:
        tmp[x[1]] = x[0]
    rank_info = tmp


    tags_table = TaggingDb.get_data('tag_info', limit=None)

    tags_info = []
    for id, tag in tags_table:
        tags_info.append(tag)

    user_table = TaggingDb.get_data('user', limit=None)

    handle_info = {}
    for id, handle, junk in user_table:
        handle_info[str(id)] = handle
    f = open('leduythuccs.github.io/data/tagging/rank_text.txt', 'w')
    for x in rank_info:
        f.write(f"{x} {rank_info[x]}\n")
    for x in rank_info:
        print(f"<@{x}>", end=' ')
    f.close()
    rank_info = unicodedata.normalize('NFC', json.dumps(rank_info).replace("\'", "\\\'")).replace('\"', '\\\"').replace('\\u001d', '')
    handle_info = unicodedata.normalize('NFC', json.dumps(handle_info).replace("\'", "\\\'")).replace('\"', '\\\"').replace('\\u001d', '')
    tags_info = unicodedata.normalize('NFC', json.dumps(tags_info).replace("\'", "\\\'")).replace('\"', '\\\"').replace('\\u001d', '')
    problems_info = unicodedata.normalize('NFC', json.dumps(problems).replace("\'", "\\\'")).replace('\"', '\\\"').replace('\\u001d', '')
    users_info = unicodedata.normalize('NFC', json.dumps(user_tagged).replace("\'", "\\\'")).replace('\"', '\\\"').replace('\\u001d', '')
    open('leduythuccs.github.io/data/tagging/rank_info.json', 'w', encoding='utf-8').write(f"rank_info_json = \'{rank_info}\';")
    open('leduythuccs.github.io/data/tagging/handle_info.json', 'w', encoding='utf-8').write(f"handle_info_json = \'{handle_info}\';")
    open('leduythuccs.github.io/data/tagging/tags_info.json', 'w', encoding='utf-8').write(f"tags_info_json = \'{tags_info}\';")
    open('leduythuccs.github.io/data/tagging/problems_info.json', 'w', encoding='utf-8').write(f"problems_info_json = \'{problems_info}\';")
    open('leduythuccs.github.io/data/tagging/users_info.json', 'w', encoding='utf-8').write(f"users_info_json = \'{users_info}\';")
convert_to_json()
