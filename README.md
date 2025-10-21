# 🤖 Local AI Chat - Your Personal ChatGPT

[![Build APK](https://github.com/Jash-18/local-ai-chat/actions/workflows/build.yml/badge.svg)](https://github.com/Jash-18/local-ai-chat/actions/workflows/build.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Android-green.svg)](https://developer.android.com/)

A **ChatGPT-like mobile application** built with Python and Kivy that connects to your local **LM Studio server**. Chat with your personal AI assistant while keeping all your data completely private and local!

## ✨ Features

- 🤖 **ChatGPT-style interface** with user/AI message bubbles
- 📱 **Native Android APK** with touch-optimized UI
- 🔌 **Direct LM Studio integration** via OpenAI-compatible API
- 🏠 **Completely local** - no external servers or data transmission
- 🔄 **Real-time messaging** with non-blocking threaded API calls
- 🎨 **Modern Material Design** with blue/gray message styling
- 🔒 **Full privacy** - your conversations never leave your network

## 🚀 Quick Start

### 1. Download & Install APK

**Latest Release**: [Download APK from Releases](https://github.com/Jash-18/local-ai-chat/releases/latest)

1. Download the APK file to your Android device
2. Enable "Install from Unknown Sources" in Android settings
3. Install the APK by tapping the downloaded file
4. Grant necessary permissions (Internet access)

### 2. Setup LM Studio (On Your Laptop - IP: 10.95.151.162)

1. **Download LM Studio** from [https://lmstudio.ai/](https://lmstudio.ai/)
2. **Install and open** the application
3. **Download a model**:
   - Click "Discover" tab
   - Recommended: Llama 3.2, Mistral 7B, or DeepSeek
   - Click download on your preferred model
4. **Load the model**:
   - Go to "Chat" tab
   - Select your downloaded model
   - Wait for it to load (green indicator)
5. **Start API server**:
   - Go to "Developer" tab
   - Click "Start Server"
   - ✅ **Enable "Serve on Local Network"**
   - ✅ **Enable "CORS"** for mobile access
   - Server should show: `http://10.95.151.162:1234`

### 3. Connect & Chat

1. **Ensure both devices** are on the same Wi-Fi network
2. **Test server access** from mobile browser: `http://10.95.151.162:1234/v1/models`
3. **Open the Local AI Chat app** on your phone
4. **Start chatting** with your personal AI assistant!

## 🛠️ Technical Details

### Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Android App   │◄──►│   Local Wi-Fi    │◄──►│   LM Studio     │
│                 │    │   10.95.151.162  │    │   (Your Laptop) │
│   • Chat UI     │    │   Port: 1234     │    │                 │
│   • API Client  │    │   • HTTP/JSON    │    │   • Local LLM   │
│   • Threading   │    │   • CORS Enabled │    │   • API Server  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Built With

- **Python 3.9** - Core application language
- **Kivy 2.3.0** - Cross-platform UI framework
- **KivyMD 1.1.1** - Material Design components
- **Requests 2.31.0** - HTTP client for API calls
- **Buildozer** - Android APK packaging
- **GitHub Actions** - Automated CI/CD pipeline

### App Configuration

The app is pre-configured for your network:

```python
# API Configuration (main.py)
self.api_url = "http://10.95.151.162:1234/v1/chat/completions"
self.model_name = "local-model"

# Request Parameters
"max_tokens": 150,      # Response length limit
"temperature": 0.7      # Creativity (0.0-1.0)
```

## 🔧 Development

### Building from Source

```bash
# Clone repository
git clone https://github.com/Jash-18/local-ai-chat.git
cd local-ai-chat

# Install dependencies
pip install -r requirements.txt

# Test locally (requires Kivy desktop support)
python main.py

# Build APK using Buildozer
buildozer android debug
```

### Automated Building

**GitHub Actions automatically builds APK** on every push to main branch:

1. **Monitor progress**: [Actions Tab](https://github.com/Jash-18/local-ai-chat/actions)
2. **Download APK**: Actions → Latest run → Artifacts → `local-ai-chat-apk`
3. **GitHub Releases**: Automatic releases with version tagging

## 🚨 Troubleshooting

### Connection Issues

**"Connection failed" error**:
1. ✅ Verify LM Studio server shows "Server Started" (green)
2. ✅ Check both devices on same Wi-Fi network
3. ✅ Test in mobile browser: `http://10.95.151.162:1234/v1/models`
4. ✅ Disable laptop firewall temporarily to test
5. ✅ Restart LM Studio server if needed

**App connects but no response**:
1. ✅ Ensure model is loaded in LM Studio Chat tab
2. ✅ Check LM Studio logs for incoming requests
3. ✅ Verify model name matches (check `/v1/models` endpoint)
4. ✅ Try reducing `max_tokens` to 50-100 for faster responses

## 📊 Performance Tips

### For Faster Responses

**LM Studio Optimization**:
- Use GPU acceleration (NVIDIA/AMD cards)
- Choose smaller models (3B-7B parameters)
- Enable quantization (4-bit, 8-bit) in model settings
- Increase GPU memory allocation

**App Optimization**:
- Reduce `max_tokens` to 50-100 for quicker responses
- Lower `temperature` to 0.3-0.5 for more focused answers
- Close other apps to free mobile resources

## 🔐 Security & Privacy

### Complete Privacy
- ✅ **All data stays local** - no external services
- ✅ **No internet required** once connected to local network
- ✅ **No conversation logging** by default
- ✅ **Full control** over your data and AI model
- ✅ **No telemetry** or analytics

## 🤝 Contributing

Contributions welcome! Here's how you can help:

1. **Report Issues** - Found a bug? [Open an issue](https://github.com/Jash-18/local-ai-chat/issues)
2. **Suggest Features** - Have ideas? Share them in discussions
3. **Code Contributions** - Fork, improve, and submit pull requests
4. **Documentation** - Help improve setup guides and tutorials
5. **Testing** - Test on different devices and configurations

## 📄 License

**MIT License** - Free for personal and commercial use!

---

## 🎉 Ready to Chat!

**Your personal ChatGPT is ready!** 

1. 📱 **Download APK** from [Releases](https://github.com/Jash-18/local-ai-chat/releases)
2. 💻 **Start LM Studio** on your laptop (10.95.151.162)
3. 🔗 **Connect** both devices to same Wi-Fi
4. 💬 **Start chatting** with complete privacy!

**Built with ❤️ using Python, Kivy, and LM Studio**

---

*Last updated: October 2025 | Version 1.0*