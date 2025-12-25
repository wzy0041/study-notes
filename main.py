import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# 从 GitHub Secrets 获取信息
api_id = int(os.environ['TG_API_ID'])
api_hash = os.environ['TG_API_HASH']
session_string = os.environ['TG_SESSION']

# ⚠️⚠️⚠️ 重点：请修改这里 ⚠️⚠️⚠️
# 打开你的 Telegram，点进那个机器人，看它的“用户名”(Username)
# 也就是带 @ 的那个名字（填的时候不要带 @）
# 根据你的截图，看起来像是 'SheerID_Verify_Bot'，请务必确认！
BOT_USERNAME = 'SheerID_Verify_Bot' 

async def main():
    print("正在登录 Telegram...")
    # GitHub 服务器在海外，不需要代理参数，直接连
    async with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
        print(f"登录成功！正在向 {BOT_USERNAME} 发送签到命令...")
        
        # 发送 /checkin
        await client.send_message(BOT_USERNAME, '/checkin')
        
        print("✅ 消息已发送！脚本执行完毕。")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
