# GitHub工具模块
# 用于处理与GitHub API相关的配置和功能

import requests
import time

# GitHub API 配置
GITHUB_REPO = "Hello-ABYDOS-27/EF-ADH-main"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}"
GITHUB_ISSUES_URL = f"{GITHUB_API_URL}/issues"

# 标签配置
LABELS = {
    "feedback": "feedback",          # 反馈标签
    "feature_request": "feature-request"  # 新功能请求标签
}

# 数据缓存
_data_cache = {
    "feedback": {"data": None, "timestamp": 0},
    "feature_request": {"data": None, "timestamp": 0}
}

# 缓存时长，单位：秒
CACHE_DURATION = 300


def get_github_data(data_type, params=None):
    """从GitHub API获取数据
    
    Args:
        data_type: 数据类型，'feedback'或'feature_request'
        params: 额外的请求参数
    
    Returns:
        list: 获取的数据列表
    """
    if params is None:
        params = {}
    
    # 检查缓存
    cache = _data_cache.get(data_type)
    current_time = time.time()
    
    if cache and cache["data"] and (current_time - cache["timestamp"] < CACHE_DURATION):
        return cache["data"]
    
    try:
        # 添加标签过滤
        if data_type in LABELS:
            params["labels"] = LABELS[data_type]
        
        # 发送请求
        response = requests.get(GITHUB_ISSUES_URL, params=params, timeout=5)
        
        if response.status_code == 200:
            issues = response.json()
            
            # 更新缓存
            _data_cache[data_type] = {
                "data": issues,
                "timestamp": current_time
            }
            
            return issues
        else:
            print(f"Failed to fetch {data_type} data: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching {data_type} data: {e}")
        return []


def get_feedback_data():
    """从GitHub获取反馈数据
    
    Returns:
        list: 处理后的反馈数据列表
    """
    issues = get_github_data("feedback", {
        "state": "all",
        "per_page": 20
    })
    
    # 处理数据，提取需要的字段
    feedback_data = []
    for issue in issues:
        feedback_data.append({
            "title": issue["title"],
            "body": issue["body"][:200] + "..." if len(issue["body"]) > 200 else issue["body"],
            "state": issue["state"],
            "created_at": issue["created_at"],
            "comments": issue["comments"]
        })
    
    return feedback_data


def get_feature_vote_data():
    """从GitHub获取新功能投票数据
    
    Returns:
        list: 处理后的功能投票数据列表
    """
    issues = get_github_data("feature_request", {
        "state": "open",
        "per_page": 20
    })
    
    # 处理数据，提取需要的字段
    feature_data = []
    for issue in issues:
        # 从issue的body中提取投票数量（假设使用特定格式）
        votes = 0
        if issue["body"]:
            # 简单的投票计数逻辑，假设body中包含"votes: N"格式
            if "votes:" in issue["body"]:
                try:
                    votes_line = [line for line in issue["body"].split("\n") if "votes:" in line][0]
                    votes = int(votes_line.split(":")[-1].strip())
                except:
                    votes = 0
        
        feature_data.append({
            "title": issue["title"],
            "body": issue["body"][:200] + "..." if len(issue["body"]) > 200 else issue["body"],
            "votes": votes,
            "created_at": issue["created_at"],
            "comments": issue["comments"]
        })
    
    # 按投票数排序
    feature_data.sort(key=lambda x: x["votes"], reverse=True)
    
    return feature_data


def clear_cache(data_type=None):
    """清除缓存
    
    Args:
        data_type: 可选，指定要清除的缓存类型，'feedback'或'feature_request'。
                   如果不指定，清除所有缓存。
    """
    if data_type:
        if data_type in _data_cache:
            _data_cache[data_type] = {"data": None, "timestamp": 0}
    else:
        for key in _data_cache:
            _data_cache[key] = {"data": None, "timestamp": 0}


def open_github_feedback():
    """获取GitHub反馈页面URL"""
    return f"https://github.com/{GITHUB_REPO}/issues/new?labels={LABELS['feedback']}"


def open_github_feature_request():
    """获取GitHub新功能请求页面URL"""
    return f"https://github.com/{GITHUB_REPO}/issues/new?labels={LABELS['feature_request']}"