# Import relevant classes from correct modules 
import requests
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.tools import FunctionTool
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
import os

# Set environmental variables
os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxNwpOZ7M"
openai_api_key = os.environ["OPENAI_API_KEY"]

                    #Define 5 separate functions for the 4 API calls and 1 RAG system

# Define Function 1 for LcL API Call

def fetch_LcL_freight_rates(origin, destination, cargo_weight, cargo_type, weight, length, width, height, units):
    url = f"yourendpoint?origin={origin}&destination={destination}&cargoWeight={cargo_weight}&cargoType={cargo_type}&weight={weight}&length={length}&width={width}&height={height}&units={units}"
    response = requests.get(url)
    print("Request made")

    if response.ok:
        try:
            data = response.json()
            print("Response obtained")

            LcL_quote_details = []

            relevant_shipments = [
                quote for quote in data
                ]

            if relevant_shipments:
                print("LcL quote details:")
                for shipment in relevant_shipments:
                    shipment_dict = {
                        "quoteId": shipment["quoteId"],
                        "countryOfOrigin": shipment["countryOfOrigin"],
                        "portOfOrigin": shipment["portOfOrigin"],
                        "portOfOriginCode": shipment["portOfOriginCode"],
                        "countryOfDestination": shipment["countryOfDestination"],
                        "portOfDestination": shipment["portOfDestination"],
                        "portOfDestinationCode": shipment["portOfDestinationCode"],
                        "carrier": shipment["carrier"],
                        "rate": shipment["generalCargo"] if shipment["generalCargo"] else shipment["hazardousCargo"],
                        "validFrom": shipment["validFrom"],
                        "validTo": shipment["validTo"],
                        "terms": shipment["terms"],
                        "bookingLink": shipment["bookingLink"]
                    }
                    LcL_quote_details.append(shipment_dict)
                return LcL_quote_details
            else:
                print("No relevant shipments found.")
        except ValueError: 
            print(f"Response is not JSON. Response content: {response.text}")
    else:
        print(f"Error fetching data. Status code: {response.status_code}. Response content: {response.text}")

LcL_freight_quote = fetch_LcL_freight_rates("china", "kenya", 100, "general", 100, 10, 10, 10, "inches")

# Define Function 2 for FcL API Call

def fetch_FcL_freight_rates(origin, destination, container_type, number_of_containers):
    url = f"yourendpoint?origin={origin}&destination={destination}&containerType={container_type}&numberOfContainers={number_of_containers}"
    response = requests.get(url)
    print("Request made")

    if response.ok:
        try:
            data = response.json()
            print("Response obtained")

            FcL_quote_details = []
        
            relevant_shipments = [
                quote for quote in data
                ]

            if relevant_shipments:
                print("FcL quote details:")
                for shipment in relevant_shipments:
                    shipment_dict = {
                        "quoteId": shipment["quoteId"],
                        "countryOfOrigin": shipment["countryOfOrigin"],
                        "portOfOrigin": shipment["portOfOrigin"],
                        "portOfOriginCode": shipment["portOfOriginCode"],
                        "countryOfDestination": shipment["countryOfDestination"],
                        "portOfDestination": shipment["portOfDestination"],
                        "portOfDestinationCode": shipment["portOfDestinationCode"],
                        "carrier": shipment["carrier"],
                        "validFrom": shipment["validFrom"],
                        "validTo": shipment["validTo"],
                        "terms": shipment["terms"],
                        "bookingLink": shipment["bookingLink"]
                    }
                    FcL_quote_details.append(shipment_dict)
                return FcL_quote_details
            else:
                print("No relevant shipments found.")
        except ValueError: 
            print(f"Response is not JSON. Response content: {response.text}")
    else:
        print(f"Error fetching data. Status code: {response.status_code}. Response content: {response.text}")

FcL_freight_quote = fetch_FcL_freight_rates("china", "kenya", "20GP", 1)

# Define Function 3 for Air Freight API Call

def fetch_air_freight_rates(origin, destination, cargo_weight, cargo_type, length, width, height, units):
    url = f"http://yourendpoint?origin={origin}&destination={destination}&cargoWeight={cargo_weight}&cargoType={cargo_type}&length={length}&width={width}&height={height}&units={units}"
    response = requests.get(url)
    print("Request made")

    if response.ok:
        try:
            data = response.json()
            print("Response obtained")

            Air_quote_details = []

            relevant_shipments = [
                quote for quote in data
                ]

            if relevant_shipments:
                print("Air quote details:")
                for shipment in relevant_shipments:
                    shipment_dict = {
                        "quoteId": shipment["quoteId"],
                        "countryOfOrigin": shipment["countryOfOrigin"],
                        "originCityAirport": shipment["originCityAirport"],
                        "airportOfLoading": shipment["airportOfLoading"],
                        "airportOfOriginCode": shipment["airportOfOriginCode"],
                        "countryOfDestination": shipment["countryOfDestination"],
                        "destinationCityAirport": shipment["destinationCityAirport"],
                        "airportOfDischarge": shipment["airportOfDischarge"],
                        "airportOfDischargeCode": shipment["airportOfDischargeCode"],
                        "cargoType": shipment["cargoType"],
                        "carrier": shipment["carrier"],
                        "carrierCode": shipment["carrierCode"],
                        "travelTime": shipment["travelTime"],
                        "offerValidUntil": shipment["offerValidUntil"],
                        "termsConditions": shipment["termsConditions"],
                        "bookingLink": shipment["bookingLink"]
                    }
                    Air_quote_details.append(shipment_dict)
                return Air_quote_details
            else:
                print("No relevant shipments found.")
        except ValueError: 
            print(f"Response is not JSON. Response content: {response.text}")
    else:
        print(f"Error fetching data. Status code: {response.status_code}. Response content: {response.text}")

air_freight_quote = fetch_air_freight_rates("usa", "kenya", 100, "general", 10, 10, 10, "inches")


# Define Function 4 for RoRo Freight API Call

def fetch_RoRo_freight_rates(origin, destination, manufacturer, model, vehicle_type, fuel_type, weight, drive_type):
    url = f"http://yourendpoint?origin={origin}&destination={destination}&manufacturer={manufacturer}&model={model}&vehicleType={vehicle_type}&fuelType={fuel_type}&weight={weight}&driveType={drive_type}"
    response = requests.get(url)
    print("Request made")

    if response.ok:
        try:
            data = response.json()
            print("Response obtained")

            RoRo_quote_details = []

            relevant_shipments = [
                shipment for shipment in data
            ]

            if relevant_shipments:
                print("RoRo Freight rates quote:")
                for shipment in relevant_shipments:
                    shipment_dict = {
                        "quoteId": shipment["quoteId"],
                        "countryOfOrigin": shipment["countryOfOrigin"],
                        "portOfOrigin": shipment["portOfOrigin"],
                        "portOfOriginCode": shipment["portOfOriginCode"],
                        "countryOfDestination": shipment["countryOfDestination"],
                        "portOfDestination": shipment["portOfDestination"],
                        "portOfDestinationCode": shipment["portOfDestinationCode"],
                        "carrier": shipment["carrier"],
                        "validFrom": shipment["validFrom"],
                        "validTo": shipment["validTo"],
                        "terms": shipment["terms"],
                        "bookingLink": shipment["bookingLink"]
                    }
                    RoRo_quote_details.append(shipment_dict)
                return RoRo_quote_details
            else:
                print("No relevant shipments found.")
        except ValueError: 
            print(f"Response is not JSON. Response content: {response.text}")
    else:
        print(f"Error fetching data. Status code: {response.status_code}. Response content: {response.text}")

RoRo_freight_quote = fetch_RoRo_freight_rates("japan", "kenya", "audi", "a5", "coupe", "petrol", 1400, "2wd")

# Define Function 5 for RAG System Call

def get_rag_response(query):
    parser = LlamaParse(
        api_key="llx-4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxAlbGh7",
        result_type="text",
        language="en",
        varbose=True
    )

    documents = parser.load_data("C:\\Users\\user\\Documents\\Jan 2024\\Projects\\RAGs\\Files\\VehicleImport.pdf")

    index = VectorStoreIndex.from_documents(documents)

    index.set_index_id("vector_index")
    index.storage_context.persist("./storage")

    storage_context = StorageContext.from_defaults(persist_dir="storage")

    index = load_index_from_storage(storage_context, index_id="vector_index")

    query_engine = index.as_query_engine(response_mode="tree_summarize")
    response = query_engine.query("What is the age restriction for car that can be imported into Kenya?")
    return response

# Set up tools for the 5 Functions
LcL_freight_tool = FunctionTool.from_defaults(fn=fetch_LcL_freight_rates) 
FcL_freight_tool = FunctionTool.from_defaults(fn=fetch_FcL_freight_rates)
Air_freight_tool = FunctionTool.from_defaults(fn=fetch_air_freight_rates)
RoRo_freight_tool = FunctionTool.from_defaults(fn=fetch_RoRo_freight_rates)
rag_tool = FunctionTool.from_defaults(fn=get_rag_response)

# Set up a single agent and give it multiple functions to call depending on user query
openai_key ="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxOZ7M"
llm = OpenAI(api_key=openai_key, model = "gpt-3.5-turbo")
agent = OpenAIAgent.from_tools([rag_tool, LcL_freight_tool, FcL_freight_tool, Air_freight_tool, RoRo_freight_tool], llm=llm, verbose=True)

response = agent.chat("What is the age restriction for car that can be imported into Kenya? and What are the freight rates for RoRo freight cargo from Country Japan to Country Kenya for an Audi model a5 coupe for fuel type petrol and weighing 1400 for drive type 2wd?")
print("Final response:")
print(response)



#Demo Output

#Final response:
#The age restriction for cars imported into Kenya is that they must be less than eight years old from the year of first registration.

#The freight rates for RoRo freight cargo from Japan to Kenya for an Audi A5 Coupe with the specified details are as follows:
#- Quote ID: A7B8C9D
#- Country of Origin: Japan
#- Port of Origin: Chiba
#- Country of Destination: Kenya
#- Port of Destination: Mombasa Port
#- Carrier: CMA CGM
#- Valid From: 2024-01-22
#- Valid To: 2024-04-30
#- Terms: [Terms and Conditions](https://www.moosa.co.ke/terms-and-conditions)
#- Booking Link: [Shipment Booking Form](https://www.moosa.co.ke/shipmentbookingform)


# My Observations

# The single-turn multi-function calling approach with 1 agent and several tools seems to map the query to the correct tool for every run, 
# However, it retrieved slightly irrelevant responses like giving freight from china to kenya when asked to give those from Japan to kenya
# In production, I anticipate this approach to be easier to implement with fewer optimizations needed and to give more straight forward answers. 

