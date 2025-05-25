# Windows 11 环境搭建指南

## 1. 系统准备

### 1.1 系统要求确认
- Windows 11 版本 21H2 或更高
- 至少8GB RAM
- 至少20GB可用磁盘空间
- 管理员权限

### 1.2 启用必要功能
1. **启用WSL2（Windows Subsystem for Linux）**
   ```powershell
   # 以管理员身份运行PowerShell
   wsl --install
   ```

2. **启用Hyper-V**
   ```powershell
   # 以管理员身份运行PowerShell
   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
   ```

## 2. 开发工具安装

### 2.1 Python安装
1. **下载Python**
   - 访问 https://www.python.org/downloads/
   - 下载Python 3.10+ Windows安装程序（64位）

2. **安装步骤**
   - 运行安装程序
   - 勾选"Add Python to PATH"
   - 选择"Customize installation"
   - 确保选中所有可选功能
   - 在高级选项中勾选：
     - Install for all users
     - Add Python to environment variables
     - Create shortcuts for installed applications
     - Add Python to PATH

3. **验证安装**
   ```powershell
   python --version
   pip --version
   ```

### 2.2 Docker Desktop安装
1. **下载Docker Desktop**
   - 访问 https://www.docker.com/products/docker-desktop
   - 下载Docker Desktop for Windows

2. **安装步骤**
   - 运行安装程序
   - 接受许可协议
   - 确保WSL 2后端已启用
   - 完成安装后重启电脑

3. **验证安装**
   ```powershell
   docker --version
   docker-compose --version
   ```

### 2.3 Node.js安装
1. **下载Node.js**
   - 访问 https://nodejs.org/
   - 下载LTS版本（16.x）

2. **安装步骤**
   - 运行安装程序
   - 接受许可协议
   - 选择安装位置
   - 确保选中"Automatically install the necessary tools"

3. **验证安装**
   ```powershell
   node --version
   npm --version
   ```

## 3. Cursor IDE配置

### 3.1 安装Cursor
1. **下载Cursor**
   - 访问 https://cursor.sh/
   - 下载Windows版本

2. **安装步骤**
   - 运行安装程序
   - 选择安装位置
   - 创建桌面快捷方式

### 3.2 配置扩展
1. **Python扩展**
   - 打开Cursor
   - 按`Ctrl+Shift+X`打开扩展面板
   - 搜索并安装：
     - Python
     - Pylance
     - Python Test Explorer
     - Python Docstring Generator

2. **Vue.js扩展**
   - 搜索并安装：
     - Volar
     - Vue Language Features
     - Vue VSCode Snippets

3. **Git配置**
   ```powershell
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

### 3.3 配置设置
1. **创建settings.json**
   - 按`Ctrl+Shift+P`
   - 输入"Preferences: Open Settings (JSON)"
   - 添加以下配置：
   ```json
   {
     "editor.formatOnSave": true,
     "editor.rulers": [80, 100],
     "editor.tabSize": 2,
     "files.trimTrailingWhitespace": true,
     "python.linting.enabled": true,
     "python.linting.pylintEnabled": true,
     "python.formatting.provider": "black",
     "python.testing.pytestEnabled": true,
     "terminal.integrated.defaultProfile.windows": "PowerShell"
   }
   ```

## 4. 项目初始化

### 4.1 创建项目目录
```powershell
# 创建项目目录
mkdir prompt_engine_prototype
cd prompt_engine_prototype

# 创建虚拟环境
python -m venv venv
.\venv\Scripts\activate

# 创建项目结构
mkdir api, services, models, tests, docs, config
mkdir api\endpoints
mkdir services\prompt
mkdir services\data
mkdir tests\unit
```

### 4.2 创建依赖文件
1. **创建requirements.txt**
   ```txt
   # Web框架
   fastapi==0.68.1
   uvicorn==0.15.0
   pydantic==1.8.2

   # 数据库
   motor==2.5.1
   redis==4.0.2

   # 工具
   python-dotenv==0.19.0
   loguru==0.5.3
   pytest==6.2.5
   httpx==0.23.0

   # 开发工具
   black==21.9b0
   pylint==2.11.1
   ```

2. **安装依赖**
   ```powershell
   pip install -r requirements.txt
   ```

### 4.3 创建配置文件
1. **创建.env文件**
   ```env
   # 应用配置
   APP_NAME=prompt_engine_prototype
   DEBUG=True
   ENVIRONMENT=development

   # 数据库配置
   MONGODB_URL=mongodb://localhost:27017
   REDIS_HOST=localhost
   REDIS_PORT=6379

   # API配置
   API_HOST=0.0.0.0
   API_PORT=8000
   ```

2. **创建config/settings.py**
   ```python
   from pydantic import BaseSettings
   from functools import lru_cache

   class Settings(BaseSettings):
       app_name: str
       debug: bool
       environment: str
       
       mongodb_url: str
       redis_host: str
       redis_port: int
       
       api_host: str
       api_port: int
       
       class Config:
           env_file = ".env"

   @lru_cache()
   def get_settings():
       return Settings()
   ```

## 5. 开发环境验证

### 5.1 测试Python环境
```powershell
# 验证Python版本
python --version

# 验证pip安装
pip list

# 验证虚拟环境
where python
```

### 5.2 测试Docker环境
```powershell
# 启动Docker Desktop
# 验证Docker运行状态
docker ps

# 测试Docker Compose
docker-compose --version
```

### 5.3 测试Node.js环境
```powershell
# 验证Node.js版本
node --version

# 验证npm安装
npm --version
```

## 6. 常见问题解决

### 6.1 Python相关问题
1. **PATH环境变量问题**
   - 打开系统属性 > 高级 > 环境变量
   - 检查Path变量是否包含Python安装路径
   - 典型路径：`C:\Users\YourUsername\AppData\Local\Programs\Python\Python310\`

2. **虚拟环境问题**
   ```powershell
   # 如果激活失败，尝试使用完整路径
   .\venv\Scripts\Activate.ps1
   ```

### 6.2 Docker相关问题
1. **WSL 2问题**
   ```powershell
   # 检查WSL版本
   wsl --list --verbose

   # 更新WSL
   wsl --update
   ```

2. **Docker服务问题**
   - 打开服务管理器（services.msc）
   - 检查Docker Desktop Service是否运行
   - 重启Docker Desktop

### 6.3 Cursor相关问题
1. **扩展加载问题**
   - 重启Cursor
   - 检查扩展兼容性
   - 更新Cursor到最新版本

2. **Python解释器问题**
   - 按`Ctrl+Shift+P`
   - 输入"Python: Select Interpreter"
   - 选择虚拟环境中的Python解释器

## 7. 开发工具使用技巧

### 7.1 Cursor快捷键
- `Ctrl+P`: 快速打开文件
- `Ctrl+Shift+F`: 全局搜索
- `F12`: 跳转到定义
- `Alt+F12`: 查看定义
- `Ctrl+Space`: 触发建议
- `F5`: 开始调试

### 7.2 PowerShell技巧
```powershell
# 设置执行策略
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# 创建别名
Set-Alias -Name py -Value python
Set-Alias -Name pip -Value pip3
```

### 7.3 Git使用技巧
```powershell
# 配置Git
git config --global core.autocrlf true
git config --global core.editor "code --wait"

# 常用命令
git init
git add .
git commit -m "Initial commit"
```

## 8. 学习资源

### 8.1 Windows特定资源
- [Windows 11开发环境配置](https://docs.microsoft.com/windows/dev-environment/)
- [WSL文档](https://docs.microsoft.com/windows/wsl/)
- [PowerShell文档](https://docs.microsoft.com/powershell/)

### 8.2 开发工具文档
- [Cursor文档](https://cursor.sh/docs)
- [Python Windows安装指南](https://docs.python.org/3/using/windows.html)
- [Docker Desktop for Windows](https://docs.docker.com/desktop/windows/) 