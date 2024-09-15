# Figma Design to Component Code Generator

## Overview

This project is a **Figma Design to Component Code Generator** that takes in a Figma design's JSON file along with images of the same design. It generates the corresponding code for the components present in the photo using OpenAI’s GPT models. The project integrates with the Figma API to fetch design data and uses OpenAI to create code based on the input image and design.

## Features

- **Figma API Integration**: Fetches the JSON data of a Figma file using the Figma API.
- **Image Encoding**: Encodes the provided design image to Base64 for API requests.
- **OpenAI API Integration**: Sends the Figma JSON data and the encoded image to OpenAI's GPT models to generate component code.
- **Component Extraction**: Extracts the components present in the image and design for generating code.
- **Conversation State**: Maintains a conversation history to ensure context-aware responses.

## Setup Instructions

### Requirements

- Python 3.10+
- Figma API Key
- OpenAI API Key

### Install Dependencies

Before running the project, install the necessary Python packages:

## Project Structure

├── python/
│   ├── GenAI.png              # Image of the Figma design
│   └── response.txt           # A file to store conversation history
├── figma_file_data.json       # JSON file generated after fetching Figma data
└── main.py                    # Main script that runs the project


