# Blogpost_generation_agent_mcp_use
Create a Deep Websearch Blogpost generation agent using mcp-use


<img width="1793" height="840" alt="image" src="https://github.com/user-attachments/assets/8435ddf9-2147-49be-a620-0ca02ff94612" />


<img width="1877" height="897" alt="image" src="https://github.com/user-attachments/assets/e042cc70-090c-435d-95a4-4eccd659facb" />

<img width="1662" height="840" alt="image" src="https://github.com/user-attachments/assets/64b032fa-2986-4dfc-804e-46633561a116" />


## Blopost Generated Saved at Filestore Directory

<img width="468" height="171" alt="image" src="https://github.com/user-attachments/assets/1386a057-6406-41ec-ae82-7da1a4b11f41" />


## Multiserver_setup.json


```
{
  "mcpServers": {
    "linkup": {
      "command": "uvx",
      "args": ["mcp-search-linkup"],
      "env": {
        "LINKUP_API_KEY": "9b4969ab-7c46-4fd9-aa0c-cbca49485e74"
      }
    },
    "filesystem": {
      "command": "C:\\Program Files\\nodejs\\npx.cmd",
      "args": [
        "@modelcontextprotocol/server-filesystem",
        "./filestore"
      ]
    }
  }
}


```


