# Prompt Engineering Framework Prototype

一个用于学习和开发Prompt工程框架的原型项目，支持TRPG叙事选项生成，集成DeepSeek和OpenAI模型，提供JSON模板管理和XMind节点编辑功能。

## 功能特点

- **多模型支持**: 集成DeepSeek和OpenAI模型，支持轮询调用
- **模板管理**: 支持JSON格式的Prompt模板加载和渲染
- **AI辅助**: 为XMind节点提供智能建议
- **数据存储**: 使用MongoDB存储模板和叙事状态，Redis缓存结果
- **用户界面**: 提供CLI和Web UI两种交互方式
- **插件系统**: 支持模型和服务扩展

## 快速开始

### 环境要求

- Python 3.10+
- Docker & Docker Compose
- Node.js 16+ (用于前端开发)

### 安装步骤

1. 克隆仓库
```bash
git clone <repository_url>
cd prompt_engine_prototype
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，填入必要的配置信息
```

4. 启动服务
```bash
docker-compose up -d
```

5. 运行应用
```bash
uvicorn api.endpoints:app --host 0.0.0.0 --port 8000
```

访问 http://localhost:8000 查看Web界面

## 项目结构

```
prompt_engine/
├── services/              # 服务模块
├── api/                   # API接口
├── plugins/              # 插件系统
├── models/               # 数据模型
├── tests/                # 测试文件
├── config/               # 配置文件
├── storage/              # 存储相关
└── docs/                 # 文档
```

## 文档

- [API文档](docs/api.md)
- [开发指南](docs/development.md)
- [部署指南](docs/deployment.md)
- [架构文档](docs/architecture.md)

## 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 联系方式

如有问题或建议，请提交 Issue 或 Pull Request。 