import yt_dlp
import json
from mcp.server.fastmcp import FastMCP
import asyncio
import sys

# 创建MCP服务器
mcp = FastMCP("youtube-downloader")

@mcp.tool()
async def download_video(url: str, output_path: str = ".") -> str:
    """下载YouTube视频
    
    Args:
        url: YouTube视频URL
        output_path: 输出文件夹路径
    """
    try:
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return f"Video downloaded successfully to {output_path}!"
    except Exception as e:
        return f"Error downloading video: {str(e)}"

if __name__ == "__main__":
    print("🚀 YouTube Downloader MCP Server starting...", file=sys.stderr)
    print("📡 Server is now running and ready to accept connections", file=sys.stderr)
    print("✓ Available tool: download_video(url, output_path)", file=sys.stderr)
    mcp.run()