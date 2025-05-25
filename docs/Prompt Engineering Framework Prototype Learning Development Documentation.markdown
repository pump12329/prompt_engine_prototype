# Prompt 工程框架原型学习开发文档

## 1. 学习目标

- **理解架构**: 学习微服务架构（Prompt Service、Data Service、API Gateway）、MongoDB/Redis 存储和插件系统。
- **掌握核心功能**: 实现 JSON 模板管理、多模型调用、XMind 节点编辑（AI Agent 辅助）和简单 UI。
- **实践本地开发**: 搭建本地环境，运行和调试原型。
- **熟悉工具**: 使用 Python、FastAPI、Vue.js、Docker Compose 和 pytest。
- **开发技能**: 学习 API 开发、异步编程、数据库交互和前端集成。

## 2. 项目概述

### 2.1 原型目标
开发一个简化的 Prompt 工程框架原型，用于学习 TRPG 叙事选项生成，支持 DeepSeek 和 OpenAI 模型、JSON 模板、XMind 集成（AI Agent 提供节点建议），提供 CLI 和 FastAPI Web UI，使用 MongoDB 存储和 Redis 缓存，优化本地开发体验。

### 2.2 简化功能
- **Prompt 管理**: 加载和渲染 JSON 模板（固定格式）。
- **多模型调用**: 支持 DeepSeek 和 OpenAI，轮询调用。
- **AI Agent**: 为 XMind 节点生成简单建议（新节点描述）。
- **数据管理**: MongoDB 存储模板和叙事，Redis 缓存结果。
- **接口**: CLI（生成选项）和 Web UI（模板编辑、XMind 预览）。
- **测试**: 基本单元测试，覆盖率 >50%.

### 2.3 技术栈
- **核心**: Python 3.10+, FastAPI, Pydantic, Motor, orjson, redis-py.
- **前端**: Vue.js 3, Tailwind CSS, Axios.
- **测试/工具**: pytest, loguru, black.
- **部署**: Docker Compose, Git.

## 3. 系统架构

### 3.1 架构图
```
+-------------------+       +-------------------+       +-------------------+
| CLI / FastAPI UI  |<----->| Prompt Service    |<----->| Data Service      |
+-------------------+       +-------------------+       +-------------------+
                                   |                            |
                                   v                            v
                            +-------------------+       +-------------------+
                            | API Gateway       |<----->| MongoDB / Redis   |
                            +-------------------+       +-------------------+
                                   |
                                   v
                            +-------------------+
                            | Plugins / AI Agent|
                            +-------------------+
```

### 3.2 模块说明
- **Prompt Service**: 加载/渲染 JSON 模板，调用 DeepSeek/OpenAI，评估选项（简单评分）。
- **Data Service**: 管理 MongoDB（模板、叙事状态）、Redis（缓存）、本地 XMind 文件。
- **API Gateway**: FastAPI 提供 API（`/generate`, `/xmind/edit`）和 Vue.js UI.
- **Plugins**: 扩展模型（DeepSeek, OpenAI）和服务（AI Agent）。
- **AI Agent**: 分析 XMind 节点，生成建议（新节点描述）。
- **CLI / FastAPI UI**: CLI 支持生成选项，Web UI 支持模板编辑和 XMind 预览。

### 3.3 目录结构
```
prompt_engine/
├── services/              # 服务模块
│   ├── prompt/            # Prompt 服务
│   │   ├── manager.py     # 模板管理和 API 调用
│   ├── data/              # 数据服务
│   │   ├── manager.py     # 数据管理
│   │   └── storage/       # 存储后端
│   │       ├── mongodb.py
│   │       └── redis.py
├── api/                   # FastAPI 应用
│   ├── endpoints.py       # API 端点
│   └── static/            # Vue.js 静态文件
├── plugins/               # 插件系统
│   ├── models/            # 模型插件
│   │   ├── deepseek.py
│   │   └── openai.py
│   └── ai_agent.py        # AI Agent
├── models/                # 数据模型
│   ├── prompt.py
│   └── response.py
├── tests/                 # 测试
│   ├── unit/
├── config/                # 配置
│   ├── settings.py
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

### 3.4 架构细节
- **Prompt Service**:
  - 加载 JSON 模板（`storage/templates/`）从 MongoDB `templates` 集合，渲染变量（Python dict）。
  - 调用 DeepSeek/OpenAI（轮询），缓存结果到 Redis（TTL 1 小时）。
  - 简单评估选项（检查是否包含“探索”或“休息”），存 MongoDB.
- **Data Service**:
  - MongoDB 集合：`templates`（`name`, `content`），`narrative_states`（`nodes`）。
  - XMind 文件（`storage/xmind/`）解析（`xmindparser`），同步到 MongoDB.
  - Redis 缓存：`prompt:{template_name}:{context_hash}`, `api:{model}:{prompt_hash}`.
- **API Gateway**:
  - API：`POST /generate`（生成选项），`POST /xmind/edit`（AI Agent 建议）。
  - UI：Vue.js 单页应用（`api/static/index.html`），支持模板编辑和 XMind 预览，Tailwind CSS 样式。
- **Plugins**:
  - 模型插件（DeepSeek, OpenAI）实现统一接口，异步调用。
  - AI Agent 作为插件，生成 XMind 节点建议（JSON 格式：`{"node_id": "node1", "suggestion": "添加探索遗迹"}`）。
- **CLI / FastAPI UI**:
  - CLI：命令 `generate`（生成选项）。
  - UI：文本框编辑 JSON 模板，显示 XMind 节点和 AI 建议。

## 4. 学习开发流程

### 4.1 项目初始化（2-3 天）
- **目标**: 搭建本地环境，熟悉工具。
- **步骤**:
  1. 克隆仓库：`git clone <repository_url> && cd prompt_engine`.
  2. 安装依赖：`pip install -r requirements.txt`, `cd api/static && npm install`.
  3. 创建 `.env`：
     ```bash
     MONGODB_URL=mongodb://localhost:27017/prompt_db
     REDIS_HOST=localhost
     DEEPSEEK_API_KEY=dummy_key
     OPENAI_API_KEY=dummy_key
     ```
  4. 启动 MongoDB/Redis：`docker run -d -p 27017:27017 --name mongodb mongo:6.0`, `docker run -d -p 6379:6379 --name redis redis:7.0`.
  5. 验证：运行 `uvicorn api.endpoints:app --host 0.0.0.0 --port 8000`, 访问 `http://localhost:8000`.
- **学习重点**:
  - 理解 Docker 容器运行 MongoDB/Redis。
  - 学习 `.env` 配置和 FastAPI 启动。
- **工具**: Git, Docker, VS Code (Volar, ESLint, Prettier).

### 4.2 Prompt Service 开发（5-7 天）
- **目标**: 实现 JSON 模板管理和模型调用。
- **步骤**:
  1. 创建 `services/prompt/manager.py`, `models/prompt.py`, `models/response.py`.
  2. 实现模板加载（MongoDB `templates`），渲染（dict），验证（Pydantic）。
  3. 实现模型调用（DeepSeek, OpenAI），使用 `aiohttp`，轮询模型，缓存到 Redis.
  4. 添加简单评估（检查关键词），存结果到 MongoDB.
  5. 编写单元测试（`tests/unit/test_prompt.py`）：测试模板渲染和 API 调用（mock）。
- **学习重点**:
  - 异步编程（`async/await`, `aiohttp`）。
  - MongoDB 查询（Motor）和 Redis 缓存（redis-py）。
  - Pydantic 模型验证。
- **工具**: MongoDB, Redis, FastAPI, Pydantic, pytest.

### 4.3 Data Service 和 AI Agent 开发（7-10 天）
- **目标**: 实现 MongoDB 数据管理和 XMind 节点编辑。
- **步骤**:
  1. 创建 `services/data/manager.py`, `storage/mongodb.py`, `storage/redis.py`, `plugins/ai_agent.py`.
  2. 实现 MongoDB 操作（`templates`, `narrative_states`），添加索引（`name`）。
  3. 实现 XMind 解析（`xmindparser`, `storage/xmind/`），同步到 MongoDB.
  4. 实现 AI Agent：调用 DeepSeek API，生成节点建议（JSON: `{"node_id": "node1", "suggestion": "探索遗迹"}`）。
  5. 编写测试（`tests/unit/test_data.py`）：测试 XMind 同步和 AI Agent 输出。
- **学习重点**:
  - MongoDB 异步操作（Motor）。
  - XMind 文件结构和解析（xmindparser）。
  - AI Agent 的 API 调用和 JSON 处理。
- **工具**: Motor, xmindparser, pytest.

### 4.4 API Gateway 和 UI 开发（7-10 天）
- **目标**: 实现 FastAPI API 和 Vue.js UI。
- **步骤**:
  1. 创建 `api/endpoints.py`, `api/static/index.html`, `api/static/app.js`.
  2. 实现 API：`POST /generate`, `POST /xmind/edit`, 配置 CORS（`http://localhost:3000`）。
  3. 实现 Vue.js UI：文本框编辑 JSON 模板，显示 XMind 节点和 AI 建议，使用 Tailwind CSS.
  4. 创建 CLI（`cli/main.py`, click）：`generate` 命令。
  5. 编写测试（`tests/unit/test_api.py`）：测试 API 端点（httpx）。
- **学习重点**:
  - FastAPI 路由和 CORS 配置。
  - Vue.js 组件和 Axios 请求。
  - Tailwind CSS 样式应用。
- **工具**: FastAPI, Vue.js, Tailwind CSS, click, httpx.

### 4.5 插件系统和文档（3-5 天）
- **目标**: 实现模型扩展和编写文档。
- **步骤**:
  1. 创建 `plugins/models/deepseek.py`, `plugins/models/openai.py`, `plugins/__init__.py`.
  2. 定义模型插件接口，动态加载（importlib）。
  3. 编写测试（`tests/unit/test_plugins.py`）。
  4. 更新 `README.md`：环境搭建、运行步骤、示例模板。
- **学习重点**:
  - 插件化设计和动态加载。
  - 文档编写（Markdown）。
- **工具**: importlib, pytest, Markdown.

## 5. 调试与学习建议
- **调试技巧**:
  - 使用 `loguru` 查看日志（`logger.info`, `logger.error`），检查 API 调用和 MongoDB 操作。
  - 在 VS Code 中设置断点，调试 FastAPI 和 Vue.js.
  - 访问 FastAPI 文档（`http://localhost:8000/docs`）测试 `/generate`, `/xmind/edit`.
- **常见问题**:
  - **MongoDB 连接失败**: 确认 `MONGODB_URL` 和 Docker 容器运行（`docker ps`）。
  - **API 调用错误**: 检查 API 密钥，测试默认选项返回。
  - **XMind 解析失败**: 确保文件格式正确，查看 `xmindparser` 错误日志。
- **学习资源**:
  - FastAPI: https://fastapi.tiangolo.com/
  - Vue.js: https://vuejs.org/guide/introduction.html
  - MongoDB: https://www.mongodb.com/docs/
  - XMind Parsing: https://github.com/xmindltd/xmindparser

## 6. 时间规划
- **总计**: 4-5 周（适合初学者）。
- **阶段**:
  - 初始化: 2-3 天
  - Prompt Service: 5-7 天
  - Data Service & AI Agent: 7-10 天
  - API Gateway & UI: 7-10 天
  - Plugins & 文档: 3-5 天

## 7. 团队配置
- **1 开发者**: 学习 Python/FastAPI 和 Vue.js，负责全栈开发。
- **可选**: 1 导师/助手，指导调试和测试。

## 8. 工具与环境
- **开发**: VS Code (Volar, ESLint, Prettier).
- **版本控制**: Git (分支：`main`, `feature/*`).
- **测试**: pytest, httpx.
- **部署**: Docker Compose (MongoDB, Redis, FastAPI).

## 9. 示例模板 (`storage/templates/trpg_fantasy.json`)
```json
{
  "name": "trpg_fantasy",
  "version": "1.1",
  "metadata": {
    "models": ["deepseek-chat", "openai-gpt4"],
    "language": "zh"
  },
  "content": {
    "context": {
      "plot": "{plot_context}",
      "character": {
        "name": "{character.name}",
        "hp": "{character.hp}"
      }
    },
    "instructions": [
      "生成 3 个 TRPG 故事选项，神秘基调，含 d20 机制。",
      "若 HP < 30，优先生存选项。"
    ],
    "output": {
      "format": "json",
      "example": [
        {"id": 1, "text": "搜索遗迹", "mechanics": {"roll": "d20", "attribute": "智力"}},
        {"id": 2, "text": "对抗身影", "mechanics": {"roll": "d20", "attribute": "力量"}},
        {"id": 3, "text": "休息", "mechanics": {"effect": "恢复 10 HP"}}
      ]
    }
  }
}
```