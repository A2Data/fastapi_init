#!/usr/bin/env python3
# -*-coding:utf-8 -*
"""
-------------------------------------------------
# @File :status
# @Date :2023/7/20 16:22
# @Author : {{ cookiecutter.author_name }}
# @Desc： 状态码
-------------------------------------------------
"""

HTTP_SUCCESS = 200
HTTP_ERROR = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_403_FORBIDDEN = 403
HTTP_404_NOT_FOUND = 404

# 1xx Informational Responses
HTTP_CONTINUE = 100  # 客户端应继续其请求
HTTP_SWITCHING_PROTOCOLS = 101  # 服务器将切换到由 Upgrade 请求头字段指定的协议

# 2xx Successful Responses
HTTP_OK = 200  # 请求成功。依赖于请求方法，可能返回资源或描述行动结果的信息
HTTP_CREATED = 201  # 请求成功并创建了新资源
HTTP_ACCEPTED = 202  # 请求已被接受进行进一步处理，但是未完成
HTTP_NO_CONTENT = 204  # 服务器成功处理了请求，但没有返回任何内容

# 3xx Redirection Messages
HTTP_MOVED_PERMANENTLY = 301  # 请求的 URL 已永久更改
HTTP_FOUND = 302  # 请求的资源临时移动到由 Location 返回的 URL
HTTP_NOT_MODIFIED = 304  # 自从上次请求后，请求的网页未修改过

# 4xx Client Error Responses
HTTP_BAD_REQUEST = 400  # 服务器无法理解请求
HTTP_UNAUTHORIZED = 401  # 请求要求用户的身份认证
HTTP_FORBIDDEN = 403  # 服务器理解请求客户端的请求，但是拒绝执行此请求
HTTP_NOT_FOUND = 404  # 服务器无法找到请求的资源

# 5xx Server Error Responses
HTTP_INTERNAL_SERVER_ERROR = 500  # 服务器内部错误，无法完成请求
HTTP_NOT_IMPLEMENTED = 501  # 服务器不支持请求的功能
HTTP_BAD_GATEWAY = 502  # 服务器作为网关或代理，从上游服务器接收到无效响应
HTTP_SERVICE_UNAVAILABLE = 503  # 由于超载或维护，服务器暂时的无法处理请求


