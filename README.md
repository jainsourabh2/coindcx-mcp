# CoinDCX MCP Server

A Python-based CoinDCX MCP server to help users manage their trading account.

## Features

- **Account Management**: Manage CoinDCX trading account, orders, and positions
- **MCP Integration**: Built on the Model Context Protocol for standardized communication
- **CoinDCX API Integration**: Uses CoinDCX's API to interact with the trading platform

## Tech Stack

- **Protocol**: [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
 
## Tools

- **Get User Balance**: Get user balance in the trading platform
- **Get User Profile**: Get user profile in the trading platform

## Prerequisites

- Python
- CoinDCX trading account with API access from [here](https://coindcx.com)
- CoinDCX API key and secret
- Gemini API key or Application Default Credentials (for Google ADK Agent)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jainsourabh2/coindcx-mcp.git
cd coindcx-mcp
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your credentials
```

5. Create a `.env` file with your configuration:

```env
# Server Configuration
COINDCX_API_KEY=your_api_key
COINDCX_SECRET_KEY=your_api_secret
PORT=8001
```

## Server Usage

The server provides a set of tools for interacting with the CoinDCX trading platform. To start the server:

1. Make sure your `.env` file is properly configured with your CoinDCX API credentials.

2. Start the server using one of the following methods:

```bash
# Using environment variables
python server.py

```

The server provides the following tools:

- `get_user_info`: Get user info
- `get_user_balance`: Get user balance

## Client Usage via gemini cli

1. Goto the folder from where gemini cli will be started.
2. Create a .gemini folder and within that settings.json file.
3. Put the below json in the settings.json file:

{
  "mcpServers": {
    "my-mcp-server": {
      "httpUrl": "http://127.0.0.1:8000/mcp/"
    }
  }
}

4. Start the gemini cli a nd run /mcp list to list all the tools provided by the server.


### Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using [Google ADK](https://google.github.io/adk-docs/)
- Uses [MCP](https://modelcontextprotocol.io/) for standardized communication

# coindcx-mcp
