# API 文档

## 概述

本文档详细说明了Prompt Engineering Framework Prototype的API接口。所有API端点都遵循RESTful设计原则，使用JSON格式进行数据交换。

## 基础信息

- 基础URL: `http://localhost:8000`
- 所有请求和响应均使用JSON格式
- 认证方式: API Key (在请求头中设置 `X-API-Key`)

## 端点列表

### 1. 生成选项

#### POST /api/v1/generate

生成TRPG叙事选项。

**请求参数:**

```json
{
  "template_name": "string",
  "context": {
    "plot": "string",
    "character": {
      "name": "string",
      "hp": "number"
    }
  }
}
```

**响应:**

```json
{
  "options": [
    {
      "id": "number",
      "text": "string",
      "mechanics": {
        "roll": "string",
        "attribute": "string"
      }
    }
  ]
}
```

### 2. XMind节点编辑

#### POST /api/v1/xmind/edit

获取AI对XMind节点的建议。

**请求参数:**

```json
{
  "node_id": "string",
  "current_content": "string",
  "context": {
    "parent_nodes": ["string"],
    "sibling_nodes": ["string"]
  }
}
```

**响应:**

```json
{
  "suggestions": [
    {
      "node_id": "string",
      "content": "string",
      "confidence": "number"
    }
  ]
}
```

### 3. 模板管理

#### GET /api/v1/templates

获取所有可用的模板列表。

**响应:**

```json
{
  "templates": [
    {
      "name": "string",
      "version": "string",
      "metadata": {
        "models": ["string"],
        "language": "string"
      }
    }
  ]
}
```

#### POST /api/v1/templates

创建新的模板。

**请求参数:**

```json
{
  "name": "string",
  "version": "string",
  "content": {
    "context": "object",
    "instructions": ["string"],
    "output": {
      "format": "string",
      "example": "array"
    }
  }
}
```

## 错误处理

所有API错误都遵循以下格式：

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": "object"
  }
}
```

常见错误代码：

- `400`: 请求参数错误
- `401`: 未授权
- `403`: 禁止访问
- `404`: 资源不存在
- `500`: 服务器内部错误

## 速率限制

- 每个API Key每分钟最多100个请求
- 超过限制将返回429状态码

## 示例

### 生成选项示例

```bash
curl -X POST http://localhost:8000/api/v1/generate \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{
    "template_name": "trpg_fantasy",
    "context": {
      "plot": "冒险者在古老遗迹中探索",
      "character": {
        "name": "艾莉丝",
        "hp": 25
      }
    }
  }'
```

### XMind编辑示例

```bash
curl -X POST http://localhost:8000/api/v1/xmind/edit \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{
    "node_id": "node1",
    "current_content": "探索遗迹",
    "context": {
      "parent_nodes": ["冒险开始"],
      "sibling_nodes": ["休息", "返回城镇"]
    }
  }'
```

## 更新日志

### v1.0.0 (2024-03-20)
- 初始版本发布
- 支持基本的选项生成和XMind编辑功能

### v1.1.0 (计划中)
- 添加批量处理功能
- 优化响应时间
- 增加更多模板选项 