import urequests
import json
import sys
import os

DEFAULT_REPO = "https://raw.githubusercontent.com/elahtrebor/xpkg/main"
CFG_PATH = "/lib/.xpkg/config.json"

def _ensure_dirs():
    try:
        os.mkdir("/lib/.xpkg")
    except:
        pass

def load_repo():
    _ensure_dirs()
    try:
        with open(CFG_PATH, "r") as f:
            cfg = json.loads(f.read())
        return cfg.get("repo", DEFAULT_REPO)
    except:
        return DEFAULT_REPO

def save_repo(url):
    _ensure_dirs()
    with open(CFG_PATH, "w") as f:
        f.write(json.dumps({"repo": url}))
    return "repo set to %s\n" % url

def fetch_index(repo_url):
    url = repo_url.rstrip("/") + "/index.json"
    r = urequests.get(url)
    try:
        if r.status_code != 200:
            raise Exception("HTTP %d" % r.status_code)
        return json.loads(r.text)
    finally:
        r.close()

def cmd_list(repo_url):
    idx = fetch_index(repo_url)
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

def _download_to_file(url, dst):
    # Stream to file to avoid big RAM usage
    r = urequests.get(url)
    try:
        if r.status_code != 200:
            return "download failed: HTTP %d\n" % r.status_code
        with open(dst, "wb") as f:
            while True:
                chunk = r.raw.read(512)
                if not chunk:
                    break
                f.write(chunk)
        return None
    finally:
        try: r.close()
        except: pass

def cmd_install(pkg, repo_url):
    idx = fetch_index(repo_url)
    if pkg not in idx:
        return "xpkg: package not found: %s\n" % pkg

    meta = idx[pkg]
    src = repo_url.rstrip("/") + "/packages/" + meta["file"]
    dst = meta.get("install", "/lib/" + pkg + ".py")

    err = _download_to_file(src, dst)
    if err:
        return err
    return "installed %s -> %s\n" % (pkg, dst)

def usage():
    return (
        "xpkg usage:\n"
        "  xpkg repo <url>\n"
        "  xpkg list\n"
        "  xpkg install <pkg>\n"
    )

def main(argv):
    if not argv:
        return usage()

    repo_url = load_repo()
    cmd = argv[0]

    if cmd == "repo":
        if len(argv) < 2:
            return "current repo: %s\n" % repo_url
        return save_repo(argv[1])

    if cmd == "list":
        return cmd_list(repo_url)

    if cmd == "install":
        if len(argv) < 2:
            return "xpkg: install requires a package name\n"
        return cmd_install(argv[1], repo_url)

    return usage()
