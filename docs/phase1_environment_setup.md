# 第一阶段：环境搭建与基础学习指南

## 1. 开发环境配置

### 1.1 系统要求

- **操作系统**
  - Windows 10/11
  - macOS 10.15+
  - Ubuntu 20.04 LTS+

- **硬件要求**
  - CPU: 双核及以上
  - 内存: 8GB及以上
  - 硬盘: 20GB可用空间

### 1.2 基础工具安装

#### Python安装
```bash
# Windows
1. 访问 https://www.python.org/downloads/
2. 下载Python 3.10+安装包
3. 运行安装程序，勾选"Add Python to PATH"
4. 验证安装：
   python --version
   pip --version

# macOS
brew install python@3.10

# Ubuntu
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip
```

#### Docker安装
```bash
# Windows
1. 下载Docker Desktop: https://www.docker.com/products/docker-desktop
2. 运行安装程序
3. 启动Docker Desktop
4. 验证安装：
   docker --version
   docker-compose --version

# macOS
brew install --cask docker

# Ubuntu
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
```

#### Node.js安装
```bash
# Windows
1. 访问 https://nodejs.org/
2. 下载LTS版本
3. 运行安装程序
4. 验证安装：
   node --version
   npm --version

# macOS
brew install node@16

# Ubuntu
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt install -y nodejs
```

### 1.3 Cursor IDE配置

#### 安装Cursor
1. 访问 https://cursor.sh/
2. 下载适合您操作系统的版本
3. 运行安装程序

#### 配置扩展
1. **Python扩展**
   - 打开Cursor
   - 进入扩展市场
   - 搜索并安装以下扩展：
     - Python
     - Pylance
     - Python Test Explorer
     - Python Docstring Generator

2. **Vue.js扩展**
   - 搜索并安装：
     - Volar
     - Vue Language Features
     - Vue VSCode Snippets

3. **Git集成**
   - 安装Git扩展
   - 配置Git用户信息：
     ```bash
     git config --global user.name "Your Name"
     git config --global user.email "your.email@example.com"
     ```

#### 配置设置
1. **编辑器设置**
   ```json
   {
     "editor.formatOnSave": true,
     "editor.rulers": [80, 100],
     "editor.tabSize": 2,
     "files.trimTrailingWhitespace": true
   }
   ```

2. **Python设置**
   ```json
   {
     "python.linting.enabled": true,
     "python.linting.pylintEnabled": true,
     "python.formatting.provider": "black",
     "python.testing.pytestEnabled": true
   }
   ```

### 1.4 Cline配置

#### 安装Cline
```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# 安装Cline
pip install cline

# 验证安装
cline --version
```

#### 初始化配置
```bash
# 创建配置文件
cline config init

# 配置项目设置
cline config set project.name "prompt_engine_prototype"
cline config set project.type "python"
cline config set project.framework "fastapi"
```

## 2. 项目初始化

### 2.1 创建项目结构

```bash
# 创建项目目录
mkdir prompt_engine_prototype
cd prompt_engine_prototype

# 创建基本目录结构
mkdir -p api/endpoints
mkdir -p services/prompt
mkdir -p services/data
mkdir -p models
mkdir -p tests/unit
mkdir -p docs
mkdir -p config
```

### 2.2 设置虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# 升级pip
pip install --upgrade pip
```

### 2.3 创建依赖文件

#### requirements.txt
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

#### 安装依赖
```bash
pip install -r requirements.txt
```

### 2.4 创建配置文件

#### .env
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

#### config/settings.py
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

## 3. 基础学习任务

### 3.1 Python基础

1. **异步编程**
   - 学习`async/await`语法
   - 理解事件循环
   - 实践异步函数

2. **类型注解**
   - 学习基本类型
   - 使用`typing`模块
   - 实践类型检查

### 3.2 FastAPI基础

1. **路由定义**
   - 学习路由装饰器
   - 理解路径参数
   - 实践查询参数

2. **请求处理**
   - 学习请求模型
   - 理解依赖注入
   - 实践中间件

### 3.3 数据库基础

1. **MongoDB**
   - 学习基本操作
   - 理解文档模型
   - 实践CRUD操作

2. **Redis**
   - 学习数据类型
   - 理解缓存策略
   - 实践基本操作

## 4. 实践项目

### 4.1 创建简单API

```python
# api/endpoints/items.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str

items = []

@router.post("/items/", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@router.get("/items/", response_model=List[Item])
async def read_items():
    return items
```

### 4.2 数据库连接

```python
# services/data/mongodb.py
from motor.motor_asyncio import AsyncIOMotorClient
from config.settings import get_settings

settings = get_settings()

class MongoDB:
    client: AsyncIOMotorClient = None
    
    async def connect(self):
        self.client = AsyncIOMotorClient(settings.mongodb_url)
        
    async def disconnect(self):
        if self.client:
            self.client.close()
            
    def get_database(self):
        return self.client.prompt_db
```

## 5. 测试与验证

### 5.1 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/unit/test_items.py

# 运行带覆盖率报告的测试
pytest --cov=api tests/
```

### 5.2 启动服务

```bash
# 启动开发服务器
uvicorn api.endpoints.items:router --reload --host 0.0.0.0 --port 8000
```

## 6. 常见问题解决

### 6.1 环境问题

1. **Python版本问题**
   - 确保使用Python 3.10+
   - 检查PATH环境变量
   - 验证虚拟环境

2. **依赖安装失败**
   - 检查网络连接
   - 更新pip
   - 使用国内镜像源

### 6.2 配置问题

1. **环境变量**
   - 检查.env文件
   - 验证变量加载
   - 确认配置正确

2. **数据库连接**
   - 检查服务状态
   - 验证连接字符串
   - 测试连接

## 7. 学习资源

### 7.1 文档
- [Python官方文档](https://docs.python.org/3/)
- [FastAPI文档](https://fastapi.tiangolo.com/)
- [MongoDB文档](https://docs.mongodb.com/)
- [Redis文档](https://redis.io/documentation)

### 7.2 教程
- FastAPI教程
- Python异步编程
- MongoDB基础
- Redis入门

### 7.3 工具
- [Cursor IDE文档](https://cursor.sh/docs)
- [Cline文档](https://cline.sh/docs)
- [Docker文档](https://docs.docker.com/)
- [Git文档](https://git-scm.com/doc) 