import xml.etree.ElementTree as Xet
import csv

# These filenames should be in root directory
FILES = [
    'Badges.xml',
    'Comments.xml', 
    'PostHistory.xml',
    'PostLinks.xml',
    'Posts.xml',
    'Tags.xml',
    'Users.xml',
    'Votes.xml'
]

# This is the maximum set of keys, some rows do not contain all fields but still need csv order to be consistent. Getting a non-existent key from a row will result in a empty field in csv ',,' maintains order of values
KEYS = [
    ['Class', 'Date', 'Id', 'Name', 'TagBased', 'UserId'],
    ['ContentLicense', 'CreationDate', 'Id', 'PostId', 'Score', 'Text', 'UserDisplayName', 'UserId'],
    ['Comment', 'ContentLicense', 'CreationDate', 'Id', 'PostHistoryTypeId', 'PostId', 'RevisionGUID', 'Text', 'UserDisplayName', 'UserId'],
    ['CreationDate', 'Id', 'LinkTypeId', 'PostId', 'RelatedPostId'],
    ['AcceptedAnswerId', 'AnswerCount', 'Body', 'ClosedDate', 'CommentCount', 'CommunityOwnedDate', 'ContentLicense', 'CreationDate', 'FavoriteCount', 'Id', 'LastActivityDate', 'LastEditDate','LastEditorDisplayName', 'LastEditorUserId', 'OwnerDisplayName', 'OwnerUserId', 'ParentId', 'PostTypeId', 'Score', 'Tags', 'Title', 'ViewCount'],
    ['Count', 'ExcerptPostId', 'Id', 'TagName', 'WikiPostId'],
    ['AboutMe', 'AccountId', 'CreationDate', 'DisplayName', 'DownVotes', 'Id', 'LastAccessDate', 'Location', 'ProfileImageUrl', 'Reputation', 'UpVotes', 'Views', 'WebsiteUrl'],
    ['BountyAmount', 'CreationDate', 'Id', 'PostId', 'UserId', 'VoteTypeId']
]

# Nested quotation marks are not accepted in neo4j so using built in repr function to wrap string in triple quotation marks
def cleanText(text):
    return repr(text)

for i, file in enumerate(FILES):
    print("File ", i)
    xmlparse = Xet.parse(file)
    name = file.split('.')[0]
    csvfile = open(f"csv/{name}.csv",'w',encoding='utf-8')
    csvfile_writer = csv.writer(csvfile)
    for row in xmlparse.findall("row"):
        csv_line = []
        for key in KEYS[i]:
            field = ''
            if key == 'Text':
                field = cleanText(row.get(key))
            else: field = row.get(key)
            csv_line.append(field)
        csvfile_writer.writerow(csv_line)
    csvfile.close()




  