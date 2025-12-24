# server.py
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount, Host
import logging
import uvicorn
import os
from typing import Optional
from dotenv import load_dotenv
import argparse
import time
import json
import hmac
import hashlib
import requests

load_dotenv()

logging.basicConfig(level=logging.INFO)

# Create MCP server
mcp = FastMCP("CoinDCX MCP")

# Fetch environment variables
API_KEY = os.getenv('COINDCX_API_KEY')
API_SECRET = os.getenv('COINDCX_SECRET_KEY')
PORT = int(os.getenv('PORT', 8001))

# Validate environment variables
if not API_KEY or not API_SECRET:
    raise ValueError("COINDCX_API_KEY and COINDCX_SECRET_KEY must be set either in .env file or via command line arguments")

# Initialize CoinDCX APIs 
secret_bytes = bytes(API_SECRET, encoding='utf-8')
key = API_KEY

# MCP tools
# MCP tool to get user info
@mcp.tool()
def get_user_info() -> dict:
    """Get the user info. Use this to get the user info.

    Args:
        None

    Returns:
        dict: The user info
    """
    #Generating a timestamp
    timeStamp = int(round(time.time() * 1000))

    body = {
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/users/info"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    print(response.json())
    data = response.json();
    return data

# MCP tool to get user balance
@mcp.tool()
def get_user_balance() -> dict:
    """Get the user balance. Use this to get the user balance.

    Args:
        None

    Returns:
        dict: The user balance
    """
    #Generating a timestamp
    timeStamp = int(round(time.time() * 1000))

    body = {
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/users/balances"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    print(response.json())
    data = response.json();
    return data

# Run in stdio mode
if __name__ == "__main__":
    mcp.run(transport="http", port=PORT)

