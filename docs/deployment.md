# 部署指南

## 部署环境要求

### 1. 系统要求

- Linux/Unix系统（推荐Ubuntu 20.04 LTS或更高版本）
- Docker 20.10+
- Docker Compose 2.0+
- 至少2GB RAM
- 至少20GB磁盘空间

### 2. 网络要求

- 开放端口：
  - 8000: FastAPI服务
  - 27017: MongoDB（可选，如果使用外部MongoDB）
  - 6379: Redis（可选，如果使用外部Redis）

## 部署步骤

### 1. 准备环境

1. 安装Docker和Docker Compose
```bash
# 安装Docker
curl -fsSL https://get.docker.com | sh

# 安装Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

2. 克隆代码
```bash
git clone <repository_url>
cd prompt_engine_prototype
```

### 2. 配置

1. 创建环境变量文件
```bash
cp .env.example .env
```

2. 编辑环境变量
```bash
# 编辑.env文件，设置必要的环境变量
nano .env
```

主要配置项：
```
# 数据库配置
MONGODB_URL=mongodb://localhost:27017/prompt_db
REDIS_HOST=localhost
REDIS_PORT=6379

# API密钥
DEEPSEEK_API_KEY=your_deepseek_api_key
OPENAI_API_KEY=your_openai_api_key

# 服务配置
API_HOST=0.0.0.0
API_PORT=8000
```

### 3. 构建和启动

1. 构建镜像
```bash
docker-compose build
```

2. 启动服务
```bash
docker-compose up -d
```

3. 检查服务状态
```bash
docker-compose ps
```

### 4. 验证部署

1. 检查API服务
```bash
curl http://localhost:8000/health
```

2. 检查数据库连接
```bash
docker-compose exec api python -c "from services.data.manager import check_connections; check_connections()"
```

## 生产环境配置

### 1. 安全配置

1. 配置防火墙
```bash
# 只开放必要端口
sudo ufw allow 8000/tcp
sudo ufw enable
```

2. 配置SSL/TLS
```bash
# 使用Nginx作为反向代理
sudo apt install nginx
sudo certbot --nginx -d your-domain.com
```

3. 配置API认证
- 启用API密钥认证
- 配置请求限流
- 启用CORS保护

### 2. 性能优化

1. MongoDB优化
```bash
# 创建索引
docker-compose exec mongodb mongo --eval 'db.templates.createIndex({"name": 1})'
```

2. Redis优化
```bash
# 配置Redis持久化
docker-compose exec redis redis-cli config set save "900 1 300 10 60 10000"
```

3. 应用优化
- 启用Gzip压缩
- 配置缓存策略
- 优化数据库查询

### 3. 监控配置

1. 日志收集
```bash
# 配置日志轮转
docker-compose exec api logrotate -f /etc/logrotate.d/prompt-engine
```

2. 性能监控
- 配置Prometheus
- 设置Grafana仪表板
- 配置告警规则

## 维护指南

### 1. 日常维护

1. 日志检查
```bash
# 查看应用日志
docker-compose logs -f api

# 查看数据库日志
docker-compose logs -f mongodb
```

2. 数据库备份
```bash
# MongoDB备份
docker-compose exec mongodb mongodump --out /backup/$(date +%Y%m%d)

# Redis备份
docker-compose exec redis redis-cli SAVE
```

### 2. 更新部署

1. 拉取最新代码
```bash
git pull origin main
```

2. 更新服务
```bash
docker-compose down
docker-compose build
docker-compose up -d
```

3. 数据库迁移
```bash
docker-compose exec api python -m alembic upgrade head
```

### 3. 故障处理

1. 服务无法启动
```bash
# 检查日志
docker-compose logs api

# 检查配置
docker-compose config
```

2. 数据库连接问题
```bash
# 检查MongoDB状态
docker-compose exec mongodb mongo --eval 'db.serverStatus()'

# 检查Redis状态
docker-compose exec redis redis-cli ping
```

3. 性能问题
```bash
# 检查容器资源使用
docker stats

# 检查数据库性能
docker-compose exec mongodb mongo --eval 'db.currentOp()'
```

## 扩展部署

### 1. 水平扩展

1. 配置负载均衡
```bash
# 使用Nginx作为负载均衡器
upstream prompt_engine {
    server api1:8000;
    server api2:8000;
    server api3:8000;
}
```

2. 扩展数据库
- 配置MongoDB副本集
- 设置Redis集群

### 2. 高可用配置

1. 配置数据库高可用
```bash
# MongoDB副本集配置
docker-compose exec mongodb mongo --eval 'rs.initiate()'
```

2. 配置应用高可用
- 使用Docker Swarm或Kubernetes
- 配置自动扩缩容
- 设置健康检查

## 备份和恢复

### 1. 备份策略

1. 数据库备份
```bash
# 创建备份脚本
#!/bin/bash
BACKUP_DIR="/backup/$(date +%Y%m%d)"
mkdir -p $BACKUP_DIR
docker-compose exec mongodb mongodump --out $BACKUP_DIR
docker-compose exec redis redis-cli SAVE
cp /var/lib/redis/dump.rdb $BACKUP_DIR/
```

2. 配置文件备份
```bash
# 备份配置文件
cp .env $BACKUP_DIR/
cp docker-compose.yml $BACKUP_DIR/
```

### 2. 恢复流程

1. 数据库恢复
```bash
# MongoDB恢复
docker-compose exec mongodb mongorestore /backup/20240320/

# Redis恢复
docker-compose exec redis redis-cli FLUSHALL
cp /backup/20240320/dump.rdb /var/lib/redis/
```

2. 配置恢复
```bash
# 恢复配置文件
cp /backup/20240320/.env .
cp /backup/20240320/docker-compose.yml .
```

## 常见问题

### 1. 部署问题

1. 端口冲突
- 检查端口占用：`netstat -tulpn | grep LISTEN`
- 修改端口配置：编辑`docker-compose.yml`

2. 内存不足
- 检查系统内存：`free -h`
- 调整容器内存限制：编辑`docker-compose.yml`

### 2. 运行问题

1. 服务无法访问
- 检查防火墙配置
- 验证网络连接
- 检查服务日志

2. 性能问题
- 检查资源使用情况
- 优化数据库查询
- 调整缓存策略

## 联系支持

如遇到问题，请通过以下方式获取支持：

1. 提交Issue
2. 发送邮件至：support@example.com
3. 查看文档：https://docs.example.com 