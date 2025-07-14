# 🌐 Deep Research Workflow Web Application

A beautiful, modern web interface for the Deep Research Workflow powered by FastAPI and DaisyUI.

## ✨ Features

### 🎨 **Beautiful UI/UX**
- **DaisyUI Components**: Modern, accessible design system
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Gradient Backgrounds**: Eye-catching visual design
- **Smooth Animations**: Hover effects and transitions
- **Glass Morphism**: Modern glass-like effects

### 🔧 **Functionality**
- **Research Form**: Easy-to-use input form with topic and depth selection
- **Real-time Processing**: Live status updates during research
- **Results Display**: Beautiful presentation of research findings
- **File Download**: Direct download of research notes
- **Error Handling**: Graceful error pages with helpful suggestions

### 📊 **Research Capabilities**
- **Dual Model Approach**: 
  - Groq `llama-3.3-70b-versatile` for tool operations
  - Local `deepseek-r1:7b` for note generation
- **Deep Web Search**: Linkup MCP server integration
- **Structured Output**: Professional research notes with executive summaries
- **Multiple Formats**: Download as markdown, print, or share

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install FastAPI and web dependencies
pip install -r requirements.txt

# Or install individually
pip install fastapi uvicorn jinja2 python-multipart aiofiles
```

### 2. Set Up Environment Variables

Create or update your `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
LINKUP_API_KEY=your_linkup_api_key_here
BRAVE_API_KEY=your_brave_api_key_here
```

### 3. Run the Web Application

```bash
# Start the FastAPI server
python app.py

# Or use uvicorn directly
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Access the Application

Open your browser and navigate to:
```
http://localhost:8000
```

## 📁 Project Structure

```
mcpuse_dir/
├── app.py                 # Main FastAPI application
├── deep_research.py       # Research workflow logic
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template with DaisyUI
│   ├── index.html        # Home page with research form
│   ├── results.html      # Results display page
│   └── error.html        # Error handling page
├── static/               # Static assets
│   └── style.css         # Custom CSS styles
├── filestore/            # Research output directory
└── multiserver_setup_config.json  # MCP server configuration
```

## 🎯 Usage Guide

### 1. **Start Research**
- Navigate to the home page
- Enter your research topic in the text area
- Select search depth (Quick/Medium/Deep)
- Click "Start Research"

### 2. **Monitor Progress**
- Watch the real-time progress indicators
- The system will show which model is being used for each step
- Progress through: Search → Analysis → Save

### 3. **View Results**
- Beautiful results page with research summary
- Statistics about the research (word count, file size, etc.)
- Sidebar with quick actions and search results preview

### 4. **Download & Share**
- Download research notes as markdown file
- Print results directly from browser
- Copy to clipboard or share via URL
- Export as PDF using browser print

## 🎨 UI Components

### **Home Page Features**
- **Hero Section**: Eye-catching gradient background with app description
- **Research Form**: Clean, intuitive form with validation
- **Feature Cards**: Highlighting key capabilities
- **How It Works**: Step-by-step process visualization
- **Responsive Design**: Adapts to all screen sizes

### **Results Page Features**
- **Research Summary**: Key statistics and metadata
- **Action Buttons**: Download, print, and share options
- **Content Display**: Formatted research notes with syntax highlighting
- **Sidebar**: Quick actions and research statistics
- **Modal Views**: Full search results in expandable modal

### **Error Handling**
- **Graceful Errors**: User-friendly error messages
- **Solution Suggestions**: Helpful troubleshooting tips
- **Technical Details**: Expandable technical information
- **Recovery Options**: Easy ways to retry or go back

## 🔧 Configuration

### **Customizing the Theme**

Edit `templates/base.html` to change the DaisyUI theme:

```html
<html lang="en" data-theme="light">  <!-- Change to: dark, cyberpunk, etc. -->
```

### **Adding New Features**

1. **New Routes**: Add to `app.py`
2. **New Templates**: Create in `templates/` directory
3. **New Styles**: Add to `static/style.css`
4. **New Functionality**: Extend `deep_research.py`

### **Environment Variables**

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | API key for Groq LLM service | Yes |
| `LINKUP_API_KEY` | API key for Linkup search | Yes |
| `BRAVE_API_KEY` | API key for Brave search | Optional |

## 🚀 Deployment

### **Local Development**
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### **Production Deployment**
```bash
# Using Gunicorn
pip install gunicorn
gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker

# Using Docker
docker build -t deep-research-webapp .
docker run -p 8000:8000 deep-research-webapp
```

### **Environment Setup**
```bash
# Set production environment
export ENVIRONMENT=production
export GROQ_API_KEY=your_production_key
export LINKUP_API_KEY=your_production_key
```

## 🔍 API Endpoints

### **Web Routes**
- `GET /` - Home page with research form
- `POST /research` - Start research workflow
- `GET /results` - View current research results
- `GET /download/{filename}` - Download research file

### **API Endpoints**
- `GET /api/status` - Application status and health check

## 🎯 Advanced Features

### **Custom Research Prompts**
Modify the research prompts in `deep_research.py`:

```python
research_prompt = f"""
Custom research prompt for: {topic}
...
"""
```

### **Adding New MCP Servers**
Update `multiserver_setup_config.json`:

```json
{
  "mcpServers": {
    "new-server": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-new"],
      "env": {
        "API_KEY": "${API_KEY}"
      }
    }
  }
}
```

### **Custom Styling**
Add custom CSS to `static/style.css`:

```css
.custom-component {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 1rem;
    padding: 2rem;
}
```

## 🐛 Troubleshooting

### **Common Issues**

1. **ModuleNotFoundError: langchain_ollama**
   ```bash
   pip install langchain-ollama --force-reinstall
   ```

2. **GROQ_API_KEY not found**
   - Check your `.env` file
   - Ensure the key is properly set

3. **MCP servers not connecting**
   - Verify server configuration in `multiserver_setup_config.json`
   - Check if all required API keys are set

4. **Port already in use**
   ```bash
   # Change port
   uvicorn app:app --port 8001
   ```

### **Debug Mode**
```bash
# Enable debug logging
export LOG_LEVEL=DEBUG
python app.py
```

## 📈 Performance Optimization

### **Caching**
- Research results are cached in memory
- Consider Redis for production caching

### **Async Processing**
- All operations are async for better performance
- Consider background tasks for long research

### **Static Files**
- CSS and JS are served from CDN for speed
- Custom styles are minified

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **DaisyUI** for the beautiful component library
- **FastAPI** for the modern web framework
- **Tailwind CSS** for the utility-first CSS framework
- **Font Awesome** for the icons

---

**Happy Researching! 🔬✨** 