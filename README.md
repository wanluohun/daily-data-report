# daily-data-report

用 Python + pandas 清洗数据、生成报表，并由 GitHub Actions 每天自动运行、自动把结果提交回来。

**目标**：不用自己的电脑开机，也能每天自动跑一次数据处理任务。

## 目前状态

- [x] 建好仓库并克隆到本地
- [ ] 写出 `clean.py`：读取 CSV → 清洗 → 生成 `report.md`
- [ ] 配置 GitHub Actions，让它每天自动运行

## 会用到什么

| 工具 | 用途 |
|---|---|
| Python 3.11 | 跑脚本 |
| pandas | 处理表格数据 |
| Git / GitHub | 版本管理 |
| GitHub Actions | 定时自动运行（公共仓库免费） |

## 本地运行

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pandas
python clean.py
```

（`clean.py` 在第 2 步完成，现在还没有。）

## 为什么要有这个仓库

练习把「一段能跑的脚本」变成「一个别人能看懂、能验证的项目」。
面试时能直接点开链接看代码和提交记录。
