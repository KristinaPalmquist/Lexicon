import azure.functions as func
import json
import logging

app = func.FunctionApp()

@app.route(route="httppost", auth_level=func.AuthLevel.ANONYMOUS, methods=["POST"])
def httppost(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP POST trigger function processed a request.')

    try:
        # Get JSON data from request body
        req_body = req.get_json()
        
        if req_body:
            logging.info(f'Received {len(req_body)} student records')
            
            # Process the student data (you can add your logic here)
            response_data = {
                "message": f"Successfully received {len(req_body)} student records",
                "students": req_body
            }
            
            return func.HttpResponse(
                json.dumps(response_data),
                status_code=200,
                headers={"Content-Type": "application/json"}
            )
        else:
            return func.HttpResponse(
                "No data received in request body",
                status_code=400
            )
            
    except Exception as e:
        logging.error(f'Error processing request: {str(e)}')
        return func.HttpResponse(
            f"Error processing request: {str(e)}",
            status_code=500
        )