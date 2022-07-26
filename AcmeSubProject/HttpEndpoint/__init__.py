import logging
import uuid
import json
import time
import azure.functions as func


def main(request: func.HttpRequest, module9storagecorndel: func.Out[str]) -> func.HttpResponse:
    logging.info('HTTP trigger function received a request.')
    start = time.time()

    rowKey = str(uuid.uuid4())

    data = {
        "Name": "Output binding message",
        "PartitionKey": "module9storagecorndel",
        "RowKey": rowKey
    }

    req_body = request.get_json()
    subtitle = req_body.get("subtitle")

    end = time.time()
    processingTime = end - start

    module9storagecorndel.set(json.dumps(data))

    return func.HttpResponse(
        f"Processing took {str(processingTime)} seconds. Translation is: {subtitle}. Rowkey: {rowKey}",
        status_code=200
    )