import asyncio
import yt_dlp

async def test_download():
    """直接测试下载功能"""
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    output_path = "./downloads"
    
    try:
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"正在下载: {url}")
            ydl.download([url])
        print(f"✓ 视频已成功下载到 {output_path}")
    except Exception as e:
        print(f"✗ 下载失败: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_download())
