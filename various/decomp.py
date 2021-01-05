# Compression and Decompression
# https://techdevguide.withgoogle.com/paths/advanced/compress-decompression
# A recursive solution is at this link,
# let's implement a stack-based alternative.


def skip_substring(s, i):
    brackets = 0
    while i < len(s):
        if s[i] == "[":
            brackets += 1
        if s[i] == "]":
            brackets -= 1
        if brackets == 0:
            return i
        i += 1
    raise ValueError


def decomp(s):
    result = ""
    stack = []
    i = 0
    repeat = 0
    nums = set(map(str, range(10)))

    while i < len(s):
        if s[i] in nums:
            repeat = repeat * 10 + int(s[i])
        elif s[i] == "[":
            if repeat == 0:
                i = skip_substring(s, i)
            else:
                stack.append([i, repeat])
                repeat = 0
        elif s[i] == "]":
            if stack[-1][1] > 1:
                stack[-1][1] -= 1
                i = stack[-1][0]
            else:
                stack.pop()
        else:
            result += s[i]
        i += 1
    return result


if __name__ == "__main__":
    s = "c[]c2[3[a]b]d0[aa100[b]]15[i]f"
    sd = decomp(s)
    assert sd == "cc" + ("a" * 3 + "b") * 2 + "d" + "i" * 15 + "f"
    print(sd)
