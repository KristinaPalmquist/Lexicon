Create an Azure Functions app, where you run event-driven code in a serverless environment. Build a web API, respond to database changes, process live event streams, and implement many more scenarios—in the cloud, in a wide variety of languages. Plus, you can connect your functions to other services without having to write extra code.
az storage account create \
  --name kikislexfuncapp \
  --resource-group kikislexfuncapp_group \
  --location northeurope \
  --sku Standard_LRS

az functionapp create \
  --resource-group kikislexfuncapp_group \
  --consumption-plan-location northeurope \
  --runtime python \
  --runtime-version 3.13 \
  --functions-version 4 \
  --name kikislexfuncapp \
  --storage-account kikislexfuncapp \
  --os-type linux


Local endpoint: http://localhost:7071/api/HttpExample