# 架构文档

## 系统架构概述

Prompt Engineering Framework Prototype采用微服务架构，主要包含以下核心组件：

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

## 核心组件

### 1. Prompt Service

#### 功能职责
- 模板管理和渲染
- 模型调用和结果处理
- 选项评估和评分

#### 关键模块
- `TemplateManager`: 管理JSON模板
- `ModelCaller`: 处理模型调用
- `OptionEvaluator`: 评估生成选项

#### 数据流
1. 接收模板请求
2. 加载并渲染模板
3. 调用AI模型
4. 处理响应
5. 评估结果

### 2. Data Service

#### 功能职责
- 数据持久化
- 缓存管理
- XMind文件处理

#### 关键模块
- `MongoDBManager`: MongoDB操作
- `RedisManager`: Redis缓存
- `XMindProcessor`: XMind文件处理

#### 数据模型
```python
# 模板模型
class Template(BaseModel):
    name: str
    version: str
    metadata: Dict
    content: Dict

# 叙事状态模型
class NarrativeState(BaseModel):
    nodes: List[Dict]
    context: Dict
```

### 3. API Gateway

#### 功能职责
- 请求路由
- 认证授权
- 请求限流
- 响应格式化

#### 关键模块
- `Router`: 路由管理
- `AuthMiddleware`: 认证中间件
- `RateLimiter`: 限流器

#### API端点
- `POST /api/v1/generate`: 生成选项
- `POST /api/v1/xmind/edit`: 编辑XMind节点
- `GET /api/v1/templates`: 获取模板列表

### 4. 插件系统

#### 功能职责
- 模型扩展
- 服务扩展
- 动态加载

#### 插件类型
1. 模型插件
   - DeepSeek
   - OpenAI
   - 自定义模型

2. 服务插件
   - AI Agent
   - 自定义服务

#### 插件接口
```python
class ModelPlugin(ABC):
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        pass

class ServicePlugin(ABC):
    @abstractmethod
    async def process(self, data: Dict) -> Dict:
        pass
```

## 数据流

### 1. 选项生成流程

```
Client -> API Gateway -> Prompt Service -> Model Plugin -> Data Service -> Client
```

1. 客户端发送生成请求
2. API Gateway验证请求
3. Prompt Service加载模板
4. 调用模型插件生成选项
5. 存储结果到Data Service
6. 返回响应给客户端

### 2. XMind编辑流程

```
Client -> API Gateway -> AI Agent -> Data Service -> Client
```

1. 客户端发送编辑请求
2. API Gateway验证请求
3. AI Agent处理节点
4. 更新Data Service
5. 返回响应给客户端

## 技术栈

### 1. 后端技术
- Python 3.10+
- FastAPI
- Pydantic
- Motor (MongoDB)
- Redis-py
- Loguru

### 2. 前端技术
- Vue.js 3
- Tailwind CSS
- Axios
- Vue Router

### 3. 数据库
- MongoDB
- Redis

### 4. 部署工具
- Docker
- Docker Compose
- Nginx

## 安全架构

### 1. 认证授权
- API Key认证
- JWT令牌
- 角色基础访问控制

### 2. 数据安全
- 数据加密
- 安全传输
- 数据备份

### 3. 网络安全
- HTTPS
- CORS配置
- 防火墙规则

## 性能优化

### 1. 缓存策略
- Redis缓存
- 内存缓存
- 缓存预热

### 2. 数据库优化
- 索引优化
- 查询优化
- 连接池

### 3. 应用优化
- 异步处理
- 负载均衡
- 资源限制

## 扩展性设计

### 1. 水平扩展
- 无状态服务
- 负载均衡
- 数据库分片

### 2. 垂直扩展
- 资源优化
- 性能调优
- 代码重构

### 3. 功能扩展
- 插件系统
- 模块化设计
- 接口抽象

## 监控和日志

### 1. 监控系统
- 服务健康检查
- 性能指标
- 资源使用

### 2. 日志系统
- 应用日志
- 访问日志
- 错误日志

### 3. 告警系统
- 性能告警
- 错误告警
- 资源告警

## 部署架构

### 1. 开发环境
- 本地Docker
- 开发数据库
- 测试工具

### 2. 测试环境
- 独立服务器
- 测试数据库
- 自动化测试

### 3. 生产环境
- 集群部署
- 高可用配置
- 负载均衡

## 未来规划

### 1. 功能扩展
- 更多模型支持
- 高级模板功能
- 自定义插件

### 2. 性能优化
- 分布式部署
- 缓存优化
- 数据库优化

### 3. 架构升级
- 微服务拆分
- 容器编排
- 服务网格 