# 开发指南

## 开发环境设置

### 1. 系统要求

- Python 3.10+
- Node.js 16+
- Docker & Docker Compose
- Git

### 2. 开发工具

推荐使用以下开发工具：

- VS Code
  - Python扩展
  - Volar (Vue.js)
  - ESLint
  - Prettier
  - Docker

### 3. 环境配置

1. 克隆仓库
```bash
git clone <repository_url>
cd prompt_engine_prototype
```

2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
cd api/static && npm install
```

4. 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件
```

## 开发流程

### 1. 代码规范

- 使用Black进行Python代码格式化
- 使用ESLint和Prettier进行前端代码格式化
- 遵循PEP 8规范
- 使用类型注解

### 2. 分支管理

- `main`: 主分支，保持稳定
- `develop`: 开发分支
- `feature/*`: 功能分支
- `bugfix/*`: 修复分支
- `release/*`: 发布分支

### 3. 提交规范

提交信息格式：
```
<type>(<scope>): <subject>

<body>

<footer>
```

类型(type)：
- feat: 新功能
- fix: 修复
- docs: 文档
- style: 格式
- refactor: 重构
- test: 测试
- chore: 构建过程或辅助工具的变动

### 4. 测试规范

1. 单元测试
```bash
pytest tests/unit/
```

2. 集成测试
```bash
pytest tests/integration/
```

3. 覆盖率报告
```bash
pytest --cov=services tests/
```

## 模块开发指南

### 1. Prompt Service

位置：`services/prompt/`

主要功能：
- 模板管理
- 模型调用
- 结果评估

开发步骤：
1. 创建新的模板类
2. 实现模板加载和渲染
3. 添加模型调用接口
4. 实现结果评估逻辑

### 2. Data Service

位置：`services/data/`

主要功能：
- MongoDB操作
- Redis缓存
- XMind文件处理

开发步骤：
1. 定义数据模型
2. 实现数据库操作
3. 配置缓存策略
4. 添加XMind处理逻辑

### 3. API Gateway

位置：`api/`

主要功能：
- 路由定义
- 请求处理
- 响应格式化

开发步骤：
1. 创建新的路由
2. 实现请求验证
3. 添加错误处理
4. 配置中间件

### 4. 前端开发

位置：`api/static/`

主要功能：
- 用户界面
- API调用
- 状态管理

开发步骤：
1. 创建Vue组件
2. 实现API集成
3. 添加状态管理
4. 优化用户体验

## 调试指南

### 1. 日志记录

使用loguru进行日志记录：
```python
from loguru import logger

logger.info("信息日志")
logger.error("错误日志")
```

### 2. 调试工具

- VS Code调试器
- Python调试器(pdb)
- Vue DevTools
- MongoDB Compass
- Redis Commander

### 3. 常见问题

1. MongoDB连接问题
- 检查连接字符串
- 确认MongoDB服务运行状态
- 验证认证信息

2. Redis缓存问题
- 检查Redis服务状态
- 验证缓存键格式
- 确认TTL设置

3. API调用问题
- 检查请求格式
- 验证认证信息
- 查看错误日志

## 性能优化

### 1. 数据库优化

- 创建适当的索引
- 使用批量操作
- 实现连接池

### 2. 缓存策略

- 设置合理的TTL
- 实现缓存预热
- 使用缓存失效策略

### 3. API优化

- 实现请求限流
- 使用异步处理
- 优化响应大小

## 发布流程

1. 版本号管理
- 遵循语义化版本
- 更新CHANGELOG.md
- 更新版本号

2. 测试
- 运行所有测试
- 进行性能测试
- 检查安全漏洞

3. 构建
```bash
docker-compose build
```

4. 部署
```bash
docker-compose up -d
```

## 贡献指南

1. Fork项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 资源链接

- [Python文档](https://docs.python.org/3/)
- [FastAPI文档](https://fastapi.tiangolo.com/)
- [Vue.js文档](https://vuejs.org/)
- [MongoDB文档](https://docs.mongodb.com/)
- [Redis文档](https://redis.io/documentation) 