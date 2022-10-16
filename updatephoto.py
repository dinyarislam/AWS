import json
import boto3
from boto3.dynamodb.conditions import Key, Attr  
import time
import datetime

REGION="us-east-1"
dynamodb = boto3.resource('dynamodb',region_name=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    photoID=event['body-json']['photoID']
    username=event['body-json']['username']
    title=event['body-json']['title']
    description=event['body-json']['description']
    tags=event['body-json']['tags']
    uploadedFileURL=event['body-json']['uploadedFileURL']

    tableItems = table.scan(
        FilterExpression=Attr('PhotoID').eq(str(photoID))
    )

    items = tableItems['Items']

    response=table.update_item(                      
        Key={'PhotoID': str(photoID),'CreationTime': photoID},
        UpdateExpression="set Title=:t, Description=:d, Tags:=g",
                ExpressionAttributeValues={
                    ':t': title,
                    'd' : description,
                    'g'  : tags
                },
                ReturnValues="UPDATED_NEW"
    )
                
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
    
    
    
