Overview:
This code provides a multi-function API interface for querying various services related to freight rates and information retrieval. 
It consists of functions for making API calls to different freight services and a system for retrieving information from documents using the RAG system.

Key Features:
Modular Design: The code is modularized, with separate functions for each API call and the RAG system.
API Integration: Integration with various freight APIs allows users to obtain quotes for LcL, FcL, Air, and RoRo freight.
RAG System Integration: Utilizes the RAG system for information retrieval from documents.
Environment Variables: Securely stores API keys using environment variables.
Tools Setup: Sets up tools for each function to facilitate ease of use and maintenance.

Setup:
API Keys: Set up your API keys as environment variables.
Function Definition: Each function defines a specific API call or information retrieval task. Parameters are provided for customization.
Tools Setup: Tools are configured for each function to streamline their usage.
Agent Configuration: An agent is configured to handle user queries and route them to the appropriate function.

Usage:
Query Input: Users input queries containing requests for freight rates or information retrieval.
Agent Processing: The agent processes the query and directs it to the relevant function.
Response: Responses are generated based on the query, including freight rates or information retrieved from documents using the RAG system.

Demo Output:
A sample demo output showcases the system's capabilities, including retrieving information about age restrictions for imported cars and providing freight rates for specific cargo details.
Observations are made regarding the system's performance and potential areas for optimization.

Observations and Future Improvements:
The system generally performs well in mapping queries to the correct tools but may require further optimization to eliminate irrelevant responses.
Future improvements may focus on refining the response accuracy and optimizing the multi-function calling approach for smoother user experiences.
