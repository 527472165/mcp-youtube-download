# YouTube Downloader MCP Server

一个基于 Model Context Protocol (MCP) 的YouTube视频下载服务器，允许AI助手和其他应用通过标准MCP接口下载YouTube视频。

## ✨ 功能特性

- 🎬 支持下载YouTube视频
- 📡 基于MCP协议，易于集成
- 🔧 可自定义输出路径
- ⚡ 异步处理，高效运行
- 🛡️ 完整的错误处理机制
- 📝 支持中文字符

## 📋 系统要求

- Python 3.8+
- Windows/Linux/macOS

## 🚀 快速开始

### 1. 安装依赖

**方式一：使用 requirements.txt（推荐）**

```bash
pip install -r requirements.txt
```

**方式二：直接安装**

```bash
pip install yt-dlp mcp
```

### 2. 运行服务器

```bash
python mcp_server.py
```

### 3. 查看启动信息

启动成功后会看到：
```
🚀 YouTube Downloader MCP Server starting...
📡 Server is now running and ready to accept connections
✓ Available tool: download_video(url, output_path)
```

## 📖 使用方法

### MCP 客户端接口

#### 工具: `download_video`

下载指定URL的YouTube视频。

**参数:**
| 参数 | 类型 | 必需 | 说明 | 默认值 |
|------|------|------|------|--------|
| url | string | ✅ | YouTube视频URL | - |
| output_path | string | ❌ | 输出文件夹路径 | `.` (当前目录) |

**返回值:**
- 成功: `"Video downloaded successfully to {output_path}!"`
- 失败: `"Error downloading video: {error_message}"`

**示例请求:**
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

## 🧪 测试

### 方法1: 直接测试下载功能

```bash
python test_direct.py
```

此方法直接调用下载函数，验证下载功能是否正常。

### 方法2: MCP协议测试

```bash
python test_mcp.py
```

此方法模拟MCP客户端，通过MCP协议测试服务器。

## 📁 项目结构

```
youtube-download/
├── download.py           # MCP服务器主文件
├── test_direct.py        # 直接测试脚本
├── test_mcp.py          # MCP协议测试脚本
└── README.md            # 本文件
```

## 🔧 高级配置

### 自定义输出格式

编辑 `download.py` 中的 `ydl_opts` 参数：

```python
ydl_opts = {
    'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    'format': 'best',  # 最高质量
    'quiet': False,     # 显示下载进度
}
```

#### 常用选项

- `format`: 指定视频格式 (如 `'best'`, `'worst'`, `'best[ext=mp4]'`)
- `quiet`: 是否显示详细信息 (true/false)
- `no_warnings`: 禁用警告 (true/false)
- `socket_timeout`: 连接超时时间 (秒)

更多选项详见 [yt-dlp官方文档](https://github.com/yt-dlp/yt-dlp#readme)


## 📝 日志输出

所有启动信息和错误信息输出到 stderr，不影响MCP协议通信。

```
stderr: 🚀 YouTube Downloader MCP Server starting...
stderr: 📡 Server is now running and ready to accept connections
stderr: ✓ Available tool: download_video(url, output_path)
```

## 🔐 安全建议

1. **URL验证**: 生产环境中应验证输入的YouTube URL
2. **路径限制**: 限制输出路径到特定目录
3. **速率限制**: 添加下载请求的频率限制
4. **错误日志**: 记录所有错误便于调试

## 📚 依赖说明

- **yt-dlp**: YouTube内容下载库（支持yt-dlp, youtube-dl等）
- **mcp**: Model Context Protocol协议库

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 📞 支持

如遇问题，请检查：
1. Python版本是否≥3.8
2. 所有依赖是否已正确安装
3. 网络连接是否正常
4. YouTube URL是否有效
