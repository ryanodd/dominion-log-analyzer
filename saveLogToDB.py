from logAnalyzer.logParser.logParserUtils import getGameIdFromLog
import uuid
import datetime
import boto3


def saveLogToDB(log):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('DominionLogs')

    id = getGameIdFromLog(log)
    if id is None:
        return

    response = table.update_item(
        Key={
            'id': id
        },
        UpdateExpression="set gameLog=:l, modifiedAt=:t",
        ExpressionAttributeValues={
            ':l': log,
            ':t': datetime.datetime.now().isoformat()
        },
        ReturnValues="UPDATED_NEW"
    )

    print("SAVE LOG TO DB RESPONSE:")
    print(response)


def saveErrorToDB(errorMessage):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('DominionErrors')

    response = table.update_item(
        Key={
            'id': str(uuid.uuid4()),
            'modifiedAt': datetime.datetime.now().isoformat()
        },
        UpdateExpression="set errorMessage=:e",
        ExpressionAttributeValues={
            ':e': errorMessage
        },
        ReturnValues="UPDATED_NEW"
    )

    print("SAVE ERROR TO DB RESPONSE:")
    print(response)
