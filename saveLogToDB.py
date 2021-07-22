from logAnalyzer.logParser.logParserUtils import getGameIdFromLog
from pprint import pprint
import boto3


def saveLogToDB(log):
    # , endpoint_url="http://localhost:8000")
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('DominionLogs')

    id = getGameIdFromLog(log)
    if id is None:
        return

    response = table.update_item(
        Key={
            'id': id
        },
        UpdateExpression="set gameLog=:l",
        ExpressionAttributeValues={
            ':l': log,
        },
        ReturnValues="UPDATED_NEW"
    )

    print("SAVE TO DB RESPONSE:")
    print(response)
