"""判断字符串中的括号是否匹配（支持 ()、[]、{}）"""

def is_bracket_matched(s: str) -> bool:
    """
    判断字符串中的括号是否成对匹配。
    支持小括号 ()、中括号 []、大括号 {}。
    """
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


# 示例测试
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("((()))", True),
        ("(()", False),
        ("", True),
        ("abc(def)ghi", True),
    ]

    print("测试结果：")
    for expr, expected in test_cases:
        result = is_bracket_matched(expr)
        status = "✓" if result == expected else "✗"
        print(f"  {status} \"{expr}\" -> {result} (期望: {expected})")

    # 用户输入测试
    user_input = input("\n请输入一个字符串，我来判断括号是否匹配: ")
    if is_bracket_matched(user_input):
        print("括号匹配！")
    else:
        print("括号不匹配！")