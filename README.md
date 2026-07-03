# YouTube Downloader — MCP Server

An MCP (Model Context Protocol) server for downloading YouTube videos. This project exposes a simple MCP tool that AI assistants or other MCP-compatible clients can call to download videos using yt-dlp.

✨ Features

- Download YouTube videos using yt-dlp
- Exposes a tool via MCP protocol for easy integration
- Configurable output path and filename template
- Asynchronous and robust error handling
- Supports Unicode (including Chinese) in filenames

System requirements

- Python 3.8+
- Windows / Linux / macOS

Quick start

1. Install dependencies

Recommended (from repo):

```
pip install -r requirements.txt
```

Or install directly:

```
pip install yt-dlp mcp
```

2. Run the server

```
python mcp_server.py
```

You should see startup messages on stderr similar to:

```
stderr: 🚀 YouTube Downloader MCP Server starting...
stderr: 📡 Server is now running and ready to accept connections
stderr: ✓ Available tool: download_video(url, output_path)
```

MCP client API

Tool: `download_video`

- Parameters:
  - `url` (string, required): The YouTube video URL to download.
  - `output_path` (string, optional): Destination folder for the downloaded file. Default: `.` (current directory).

- Return value:
  - Success: `"Video downloaded successfully to {output_path}!"`
  - Failure: `"Error downloading video: {error_message}"`

Example MCP request (JSON-RPC):

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "download_video",
    "arguments": {
      "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
      "output_path": "./downloads"
    }
  }
}
```

Testing

1. Direct function test

```
python test_direct.py
```

2. MCP protocol test

```
python test_mcp.py
```

Project layout

```
mcp-youtube-download/
├── mcp_server.py        # MCP server implementation
├── test_direct.py       # Direct download tests
├── test_mcp.py          # MCP-based tests
├── requirements.txt     # Python dependencies
└── README.md            # Original README (Chinese)
```

Configuration

Edit `mcp_server.py` and adjust `ydl_opts` to change output format and download options. Example:

```python
ydl_opts = {
    'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    'format': 'best',
    'quiet': False,
}
```

Common yt-dlp options:

- `format`: choose video/audio format (e.g. `best`, `worst`, `best[ext=mp4]`).
- `quiet`: whether to suppress detailed output (True/False).
- `no_warnings`: disable warnings.
- `socket_timeout`: network timeout in seconds.

Logs

Startup and error messages are printed to stderr and do not interfere with MCP communications. Example:

```
stderr: 🚀 YouTube Downloader MCP Server starting...
```

Security recommendations

- Validate incoming URLs before downloading in production.
- Restrict allowed output paths to a safe directory.
- Add rate-limiting for download requests.
- Log errors for auditing and debugging.

Dependencies

- `yt-dlp`: YouTube downloader library (preferred)
- `mcp`: Model Context Protocol implementation

Contributing

Issues and pull requests are welcome.

Support / Troubleshooting

If something fails, check:
1. Python version is >= 3.8
2. All dependencies are installed
3. Network connectivity to YouTube
4. The provided YouTube URL is valid

License

Include an appropriate license file if you plan to publish this project publicly.
