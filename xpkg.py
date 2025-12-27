import urequests
import json
import sys

REPO_LINK="https://raw.githubusercontent.com/elahtrebor/xpkg/main"

def fetch_index(repo_url):
    url = REPO_LINK + "/index.json"
    r = urequests.get(url)
    try:
        if r.status_code != 200:
            raise Exception("HTTP %d" % r.status_code)
        return json.loads(r.text)
    finally:
        r.close()

def cmd_list():
    idx = fetch_index(REPO_LINK)
    out = []
    for name, meta in idx.items():
        if name in ("repo", "updated"):
            continue
        out.append("%-10s %s - %s" % (
            name,
            meta.get("version", "?"),
            meta.get("desc", "")
        ))
    return "\n".join(out) + "\n"


def cmd_install(pkg):
    repo = REPO_LINK
    idx = fetch_index(repo)
    if pkg not in idx:
        return "xpkg: package not found\n"

    meta = idx[pkg]
    src = repo + "/" + meta["file"]
    dst = meta.get("install", "/lib/" + pkg + ".py")

    r = urequests.get(src)
    try:
        with open(dst, "w") as f:
            f.write(r.text)
    finally:
        r.close()

    return "installed %s\n" % pkg


def main(argv):
    cmd = argv[0]

    if cmd == "list":
        return cmd_list()
    
    elif cmd == "install":
        pkg = argv[1]
        return cmd_install(pkg)
    return "ok\n"


