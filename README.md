# 🔬 Deep Research Workflow

A comprehensive research automation system that combines **Linkup MCP** for deep web search and **Ollama DeepSeek** for intelligent research note generation.

## 🚀 Features

- **Deep Web Search**: Uses Linkup MCP server for comprehensive web research
- **AI-Powered Analysis**: Leverages Ollama with deepseek-r1:7b model for intelligent analysis
- **Automated Note Generation**: Creates professional research notes with structured format
- **File Management**: Automatically saves research notes to filestore using MCP filesystem
- **Flexible Search Depth**: Supports deep, medium, and quick search modes

## 📋 Prerequisites

1. **Ollama**: Install from [ollama.ai](https://ollama.ai/)
2. **Python 3.8+**: With pip package manager
3. **Linkup API Key**: Get from [Linkup](https://linkup.com/)
4. **uvx**: For running MCP servers (usually comes with uv)

## 🛠️ Setup

### 1. Run the Setup Script
```bash
python setup_research.py
```

This will:
- Check if Ollama is installed
- Install required Python packages
- Pull the deepseek-r1:7b model
- Create a .env template file

### 2. Configure Environment Variables
Edit the `.env` file and add your Linkup API key:
```env
LINKUP_API_KEY=your_actual_linkup_api_key_here
```

### 3. Verify Installation
```bash
# Check if Ollama is working
ollama list

# Check if the model is available
ollama show deepseek-r1:7b
```

## 🎯 Usage

### Basic Usage
```bash
python deep_research.py
```

You'll be prompted to enter:
- **Research Topic**: The subject you want to research
- **Search Depth**: deep/medium/quick (default: deep)

### Example Workflow
```
🔬 Deep Research Workflow with Linkup MCP + Ollama DeepSeek
============================================================
Enter research topic: artificial intelligence trends 2025
Enter search depth (deep/medium/quick) [default: deep]: deep

🚀 Starting deep research workflow for: artificial intelligence trends 2025
============================================================
🔍 Performing deep search for: artificial intelligence trends 2025
✅ Search completed. Found comprehensive results.

============================================================
📝 Generating research notes for: artificial intelligence trends 2025
✅ Research notes generated successfully.

============================================================
💾 Saving research notes for: artificial intelligence trends 2025
✅ Research notes saved to: research_notes_artificial_intelligence_trends_2025_20250713_131500.md

============================================================
🎉 Research workflow completed successfully!
📄 Research notes saved to: filestore/research_notes_artificial_intelligence_trends_2025_20250713_131500.md
```

## 📊 Output Format

The generated research notes include:

1. **Executive Summary** (2-3 paragraphs)
2. **Key Findings** (bullet points with explanations)
3. **Technical Analysis** (detailed technical insights)
4. **Market Trends** (current market analysis)
5. **Expert Opinions** (quotes and insights from authorities)
6. **Future Outlook** (predictions and trends)
7. **Recommendations** (actionable insights)
8. **Sources & References** (proper citations)

## 🔧 Configuration

### MCP Configuration (`multiserver_setup_config.json`)
```json
{
  "mcpServers": {
    "linkup": {
      "command": "uvx",
      "args": ["mcp-search-linkup"],
      "env": {
        "LINKUP_API_KEY": "${LINKUP_API_KEY}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "filestore"
      ]
    }
  }
}
```

### Ollama Model Configuration
- **Model**: deepseek-r1:7b
- **Temperature**: 0.3 (for consistent, focused output)
- **Max Steps**: 50 (for comprehensive research)

## 📁 File Structure
```
mcpuse_dir/
├── deep_research.py          # Main research workflow
├── setup_research.py         # Setup script
├── multiserver_setup_config.json  # MCP configuration
├── .env                      # Environment variables
├── filestore/                # Research notes output
│   └── research_notes_*.md   # Generated research files
└── RESEARCH_README.md        # This file
```

## 🎛️ Customization

### Modify Search Depth
Edit the `perform_deep_search` method in `deep_research.py`:
```python
async def perform_deep_search(self, query, search_depth="deep"):
    # Customize search parameters based on depth
    if search_depth == "deep":
        # Comprehensive search with multiple sources
    elif search_depth == "medium":
        # Balanced search with key sources
    elif search_depth == "quick":
        # Fast search with top results
```

### Customize Research Note Format
Edit the `generate_research_notes` method to modify the output structure:
```python
research_prompt = f"""
Based on the following search results, create comprehensive research notes for the topic: "{topic}"

# Add your custom sections here
1. **Custom Section 1**
2. **Custom Section 2**
...
"""
```

## 🐛 Troubleshooting

### Common Issues

1. **Ollama not found**
   ```bash
   # Install Ollama from https://ollama.ai/
   # Then restart your terminal
   ```

2. **Model not available**
   ```bash
   ollama pull deepseek-r1:7b
   ```

3. **Linkup API key error**
   - Verify your API key in the `.env` file
   - Check if the key has proper permissions

4. **MCP server connection issues**
   - Ensure `uvx` is installed
   - Check if the MCP server package is available

### Debug Mode
Add debug logging to see detailed information:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🔄 Advanced Usage

### Batch Research
Create a script to research multiple topics:
```python
topics = [
    "quantum computing 2025",
    "blockchain technology trends",
    "machine learning applications"
]

for topic in topics:
    result = await workflow.run_research_workflow(topic)
```

### Custom Research Templates
Create specialized research templates for different domains:
- Academic research
- Market analysis
- Technical documentation
- Competitive intelligence

## 📈 Performance Tips

1. **Use appropriate search depth**:
   - Quick: 1-2 minutes
   - Medium: 3-5 minutes
   - Deep: 5-10 minutes

2. **Optimize for specific topics**:
   - Technical topics: Use "deep" search
   - General topics: Use "medium" search
   - Quick overview: Use "quick" search

3. **Monitor file size**:
   - Research notes can be large (10-50KB)
   - Ensure sufficient disk space

## 🤝 Contributing

Feel free to contribute improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Researching! 🔬📚** 
