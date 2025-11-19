from flask import Flask
import os
import threading
import logging

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>GitHub Deployed Bot</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                text-align: center; 
                padding: 50px; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container { 
                max-width: 600px; 
                margin: 0 auto; 
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
            }
            .status { 
                color: #00ff00; 
                font-weight: bold;
                font-size: 24px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 Telegram Bot</h1>
            <p class="status">✅ Successfully Deployed!</p>
            <p>🚀 Deployed from GitHub</p>
            <p>📱 Made from Phone</p>
            <p>☁️ Running on Heroku</p>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy", "message": "Bot is running from GitHub"}

def run_bot():
    try:
        from bot import main
        main()
    except Exception as e:
        logging.error(f"Bot error: {e}")

if __name__ == '__main__':
    # Bot alag thread mein chalega
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Flask server
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)