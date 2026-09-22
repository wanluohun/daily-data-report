"""读取 scores.csv → 分数转数字 → 丢掉分数无效的行 → 按整行去重。"""
import csv
import math
from pathlib import Path

CSV = Path(__file__).parent / "data" / "scores.csv"


def to_score(raw):
    """能转成有限数字就转，转不了（空、abc、inf、缺字段）一律返回 nan。"""
    try:
        s = float(raw)
    except (ValueError, TypeError):
        return math.nan
    return s if math.isfinite(s) else math.nan


# 1) 读原始数据
with CSV.open(encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    cols = reader.fieldnames
    rows = list(reader)
total = len(rows)

# 2) 分数转数字，转不了的是 nan
for r in rows:
    r["score"] = to_score(r["score"])

# 3) 丢掉分数无效的行（此刻 nan 已全部清空，下面才能安全比较）
good = [r for r in rows if not math.isnan(r["score"])]
bad_score = total - len(good)

# 4) 按所有列去重，保留首次出现的顺序
seen = set()
unique = []
for r in good:
    key = tuple(r[c] for c in cols)
    if key not in seen:
        seen.add(key)
        unique.append(r)
dups = len(good) - len(unique)

print(f"原始数据行: {total}")
print(f"丢弃·分数无效(空/abc): {bad_score}")
print(f"丢弃·整行重复: {dups}")
print(f"清洗后有效行: {len(unique)}")

# 自检：丢掉的 + 留下的 必须正好等于原始行数
assert len(unique) + bad_score + dups == total, "计数对不上，说明有行被重复归类或漏掉"

print("\n清洗后:")
for r in unique:
    print(f"  {r}")
