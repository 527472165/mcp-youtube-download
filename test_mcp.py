import asyncio
import subprocess
import sys
import json
import time

async def test_youtube_downloader():
    """测试YouTube下载MCP服务"""
    
    # 启动服务器进程，指定UTF-8编码
    process = subprocess.Popen(
        [sys.executable, "download.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8',
        errors='ignore',
        bufsize=1
    )
    
    try:
        # 等待服务器启动
        await asyncio.sleep(2)
        
        # 第一步：发送initialize请求
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            }
        }
        
        print("Sending initialize request...")
        process.stdin.write(json.dumps(init_request) + "\n")
        process.stdin.flush()
        
        # 读取初始化响应
        await asyncio.sleep(1)
        response = process.stdout.readline()
        print(f"Initialize Response: {response}")
        
        # 第二步：发送list tools请求
        list_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
            "params": {}
        }
        
        print("\nSending tools/list request...")
        process.stdin.write(json.dumps(list_request) + "\n")
        process.stdin.flush()
        
        await asyncio.sleep(1)
        response = process.stdout.readline()
        print(f"Tools List Response: {response}")
        
    except Exception as e:
        print(f"Test error: {e}")
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except:
            process.kill()

if __name__ == "__main__":
    asyncio.run(test_youtube_downloader())
