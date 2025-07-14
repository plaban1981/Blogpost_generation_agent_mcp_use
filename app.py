from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import asyncio
import os
from datetime import datetime
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

load_dotenv()

app = FastAPI(title="MCP Blog Generator", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Global variable to store current blog results
current_blog = None

# Initialize MCP components
def get_mcp_agent():
    """Initialize MCP agent with OpenAI model"""
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        api_key=os.getenv("OPAPIKEY")
    )
    # llm = ChatGroq(
    #     model="llama-3.3-70b-versatile",
    #     api_key=os.getenv("GROQ_API_KEY")
    # )
    client = MCPClient.from_config_file("multiserver_setup_config.json")
    agent = MCPAgent(
        llm=llm,
        client=client,
        use_server_manager=False,
        max_steps=30
    )
    return agent

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page with blog topic form"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/search")
async def perform_web_search(
    request: Request,
    topic: str = Form(...)
):
    """Perform web search using MCP linkup server"""
    try:
        agent = get_mcp_agent()
        
        # Step 1: Perform web search
        print(f"🔍 Performing web search for: {topic}")
        search_result = await agent.run(
            f"Use the 'linkup' server to search for: {topic}"
        )
        
        if search_result:
            return templates.TemplateResponse(
                "search_results.html",
                {
                    "request": request,
                    "topic": topic,
                    "search_results": search_result,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            )
        else:
            raise HTTPException(status_code=500, detail="Search failed")
    except Exception as e:
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": str(e),
                "topic": topic
            }
        )

@app.post("/generate_blog")
async def generate_blog_post(
    request: Request,
    topic: str = Form(...),
    search_results: str = Form(...)
):
    """Generate blog post from search results and save to filestore"""
    global current_blog
    try:
        agent = get_mcp_agent()
        
        llm = ChatGroq(
            model="deepseek-r1-distill-llama-70b",
            temperature=0.7,
            api_key=os.getenv("GROQ_API_KEY")
        )
        # Step 2: Generate blog post
        print(f"📝 Generating blog post for: {topic}")
        blog_post = await llm.ainvoke(
            f"Write an engaging blog post about the topic: {topic} based on the search results: {search_results} Use emojis and make it interesting."
        )
        
        if blog_post:
            # Step 3: Save blog post to filestore
            print(f"💾 Saving blog post to filestore...")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"blog_{topic.replace(' ', '_').lower()}_{timestamp}.md"
            
            save_result = await agent.run(
                f"Use the tool `write_file` from the `filesystem` server and write filename: '{filename}' at filestore directory and save  content: {blog_post.content}"
            )
            
            result = {
                "topic": topic,
                "search_results": search_results,
                "blog_post": blog_post.content,
                "filename": filename,
                "save_result": save_result
            }
            current_blog = result
            
            return templates.TemplateResponse(
                "results.html",
                {
                    "request": request,
                    "blog": result,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            )
        else:
            raise HTTPException(status_code=500, detail="Blog generation failed")
    except Exception as e:
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": str(e),
                "topic": topic
            }
        )

@app.get("/results")
async def view_results(request: Request):
    global current_blog
    if not current_blog:
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse(
        "results.html",
        {
            "request": request,
            "blog": current_blog,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    )

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = f"filestore/{filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    from fastapi.responses import FileResponse
    return FileResponse(file_path, filename=filename)

@app.get("/api/status")
async def api_status():
    return {
        "status": "running",
        "timestamp": datetime.now().isoformat(),
        "has_blog": current_blog is not None
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000) 