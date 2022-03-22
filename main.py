import xml.etree.ElementTree as Xet
import csv

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

for i, file in enumerate(FILES):
    xmlparse = Xet.parse(file)
    name = file.split('.')[0]
    csvfile = open(f"csv/{name}.csv",'w',encoding='utf-8')
    csvfile_writer = csv.writer(csvfile)
    for row in xmlparse.findall("row"):
        csv_line = []
        for key in KEYS[i]:
            csv_line.append(row.get(key))
        csvfile_writer.writerow(csv_line)
    csvfile.close()

  