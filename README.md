# Figma Design to Component Code Generator

## Overview

The **Figma Design to Component Code Generator** is an innovative tool that leverages the power of the Figma API and OpenAI’s GPT models to transform Figma designs into React component code. By combining design data with image recognition and generative AI, the project aims to enhance user productivity by automating the code generation process for UI components.

## Features

- **Figma API Integration**: Fetches the JSON data of a Figma file using the Figma API.
- **Image Encoding**: Converts the provided design image to Base64 for API requests.
- **OpenAI API Integration**: Sends the Figma JSON data and the encoded image to OpenAI's GPT models to generate component code.
- **Component Extraction**: Extracts the components present in the image and design for generating code.
- **Conversation State**: Maintains a conversation history to ensure context-aware responses.

## How It Works

1. **Figma API Integration**:
   - **Fetch Design Data**: The project utilizes the Figma API to retrieve the design data from a Figma file. This data is obtained in the form of a JSON file that includes detailed information about the design, such as component structure, styles, and layout.

2. **Image Processing**:
   - **Screenshot Upload**: A screenshot of the Figma design is taken to serve as a visual reference for the design.
   - **Base64 Encoding**: The screenshot is converted into Base64 format. This conversion allows the image to be included in API requests and sent to the generative AI model for analysis.

3. **OpenAI API Integration**:
   - **Data Submission**: Both the Figma JSON data and the Base64 encoded image are submitted to OpenAI’s GPT models. The AI uses this combined input to understand the design and generate code.
   - **Component Code Generation**: Users can specify prompts to indicate which parts of the design they want to generate code for. The GPT model processes these inputs and outputs the corresponding React component code.

4. **User Interaction**:
   - **Dynamic Code Generation**: Users can interact with the tool by specifying which components or parts of the design they wish to generate. The AI responds with React code that matches the requested design elements.

5. **Feedback and Improvement**:
   - **Iterative Refinement**: The AI model can refine the generated code based on user feedback. This iterative process helps in enhancing the accuracy and relevance of the generated components.

## Setup Instructions

### Requirements

- Python 3.10+
- Figma API Key
- OpenAI API Key

### Install Dependencies

Before running the project, install the necessary Python packages:

```bash
pip install -r requirements.txt

├── python/
│   ├── GenAI.png              # Image of the Figma design
│   └── response.txt           # A file to store conversation history
├── figma_file_data.json       # JSON file generated after fetching Figma data
└── main.py                    # Main script that runs the project


