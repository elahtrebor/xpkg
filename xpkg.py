import urequests
import sys
REPO_LINK="https://raw.githubusercontent.com/elahtrebor/xpkg/main"

def fetch_index(repo_url):
    import urequests, json
    url = repo_url.rstrip("/") + "/index.json"
    r = urequests.get(url)
    try:
        if r.status_code != 200:
            raise Exception("HTTP %d" % r.status_code)
        return json.loads(r.text)
    finally:
        r.close()

def cmd_list(repo):
    idx = fetch_index(repo)
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


def install(pkg, repo):
    idx = fetch_index(repo)
    if pkg not in idx:
        return "xpkg: package not found\n"

    meta = idx[pkg]
    src = repo.rstrip("/") + "/" + meta["file"]
    dst = meta.get("install", "/lib/" + pkg + ".py")

    r = urequests.get(src)
    try:
        with open(dst, "w") as f:
            f.write(r.text)
    finally:
        r.close()

    return "installed %s\n" % pkg



def main(argv):
    cmdargs = argv.split(" ")
    cmd = cmdargs[0] 

    if cmd == "list":
      pkgname = cmdargs[1]
        
    return "ok\n"


main("list")
