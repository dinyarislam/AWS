import json
import boto3  
import time
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

REGION="us-east-1"
dynamodb = boto3.resource('dynamodb',region_name=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    photoID=event['body-json']['photoID']

    
    tableItems = table.scan(
        FilterExpression=Attr('PhotoID').eq(str(photoID))
    )
    items = tableItems['Items'][0]['URL']

    filename = (items.split('/'))[-1]
    table.delete_item(
        Key={
            'PhotoID': str(photoID),
            'CreationTime': photoID
        }
    )

    return {
        "statusCode": 200,
        "body": filename,
    }
    
    
    
