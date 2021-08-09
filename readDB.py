import os
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DominionLogs')

response = table.scan()
data = response['Items']

while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items'])

for item in data:
    filename = 'logs/' + item['id'] + '.txt'
    if not (os.path.exists(filename)):
        file = open(filename, 'w')
        file.write(item['gameLog'])
        file.close()
